package vyxal

import vyxal.impls.Elements

import VNum.given

object Interpreter:
  def execute(code: String)(using ctx: Context): Unit =
    Parser.parse(code) match
      case Right(ast) =>
        if ctx.settings.logLevel == LogLevel.Debug then
          println(s"Executing '$code' (ast: $ast)")
        execute(ast)
        // todo implicit output according to settings
        if !ctx.isStackEmpty && ctx.settings.endPrintMode == EndPrintMode.Default
        then println(ctx.peek)
      case Left(error) =>
        println(s"Error while executing $code: $error")
        ???

  def execute(ast: AST)(using ctx: Context): Unit =
    if ctx.settings.logLevel == LogLevel.Debug then
      println(s"Executing AST $ast, stack = ${ctx.peek(5)}")
    ast match
      case AST.Number(value) => ctx.push(value)
      case AST.Str(value)    => ctx.push(value)
      case AST.Lst(elems) =>
        val list = collection.mutable.ListBuffer.empty[VAny]
        for elem <- elems do
          given elemCtx: Context = ctx.makeChild()
          execute(elem)
          list += ctx.pop()
        ctx.push(VList(list.toList*))
      case AST.Command(cmd) =>
        Elements.elements.get(cmd) match
          case Some(elem) => elem.impl()
          case None       => throw RuntimeException(s"No such command: '$cmd'")
      case AST.Group(elems, _) =>
        elems.foreach(Interpreter.execute(_))
      case AST.CompositeNilad(elems) =>
        elems.foreach(Interpreter.execute(_))
      case AST.If(thenBody, elseBody) =>
        if MiscHelpers.boolify(ctx.pop()) then execute(thenBody)
        else if elseBody.nonEmpty then execute(elseBody.get)
      case AST.While(None, body) =>
        val loopCtx = ctx.makeChild()
        loopCtx.contextVarN = ctx.settings.rangeStart
        loopCtx.contextVarM = 1
        while true do
          execute(body)(using loopCtx)
          loopCtx.contextVarN = loopCtx.contextVarN.asInstanceOf[VNum] + 1
      case AST.While(Some(cond), body) =>
        execute(cond)
        given loopCtx: Context = ctx.makeChild()
        loopCtx.contextVarN = ctx.settings.rangeStart
        loopCtx.contextVarM = ctx.peek
        while MiscHelpers.boolify(ctx.pop()) do
          execute(body)
          execute(cond)
          loopCtx.contextVarN = loopCtx.contextVarN.asInstanceOf[VNum] + 1

      case AST.For(None, body) =>
        val iterable =
          ListHelpers.makeIterable(ctx.pop(), Some(true))(using ctx)
        var index = 0
        given loopCtx: Context = ctx.makeChild()
        for elem <- iterable do
          loopCtx.contextVarN = elem
          loopCtx.contextVarM = index
          index += 1
          execute(body)(using loopCtx)

      case AST.For(Some(name), body) =>
        val iterable =
          ListHelpers.makeIterable(ctx.pop(), Some(true))(using ctx)
        var index = 0
        given loopCtx: Context = ctx.makeChild()
        for elem <- iterable do
          loopCtx.setVar(name, elem)
          loopCtx.contextVarN = elem
          loopCtx.contextVarM = index
          index += 1
          execute(body)(using loopCtx)

      case lam: AST.Lambda      => ctx.push(VFun.fromLambda(lam))
      case AST.FnDef(name, lam) => ctx.setVar(name, VFun.fromLambda(lam))
      case AST.GetVar(name)     => ctx.push(ctx.getVar(name))
      case AST.SetVar(name)     => ctx.setVar(name, ctx.pop())
      case AST.AugmentVar(name, op) =>
        ctx.push(ctx.getVar(name))
        op match
          case lam: AST.Lambda => ctx.push(executeFn(VFun.fromLambda(lam)))
          case _               => execute(op)
        ctx.setVar(name, ctx.pop())
      case AST.UnpackVar(names) =>
        MiscHelpers.unpack(names)
      case AST.ExecuteFn =>
        ctx.pop() match
          case fn: VFun => ctx.push(executeFn(fn))
          case _        => ???
      case _ => throw NotImplementedError(s"$ast not implemented")
    end match
    if ctx.settings.logLevel == LogLevel.Debug then
      println(s"res was ${ctx.peek}")
  end execute

  /** Execute a function and return what was on the top of the stack, if there
    * was anything
    *
    * @param args
    *   Custom arguments (instead of popping from the stack)
    * @param popArgs
    *   Whether to pop the arguments from the stack (instead of merely peeking)
    */
  def executeFn(
      fn: VFun,
      contextVarM: Option[VAny] = None,
      contextVarN: Option[VAny] = None,
      args: Option[Seq[VAny]] = None,
      popArgs: Boolean = true
  )(using ctx: Context): VAny =
    val VFun(impl, arity, params, origCtx) = fn
    // println(s"Executing function with arity $arity")
    given fnCtx: Context =
      Context.makeFnCtx(origCtx, ctx, arity, params, args, popArgs)

    contextVarM.foreach { m => fnCtx.contextVarM = m }
    contextVarN.foreach { n => fnCtx.contextVarN = n }

    impl()(using fnCtx)

    fnCtx.pop()
  end executeFn
end Interpreter