package vyxal

import org.scalatest.funsuite.AnyFunSuite
import VyxalToken.*

class LexerTests extends AnyFunSuite:
  test("Does the lexer recognise numbers?") {
    assert(Lexer("123") == Right(List(Number("123"))))
    assert(Lexer("6.") == Right(List(Number("6."))))
    assert(Lexer("3.4ı1.2") == Right(List(Number("3.4ı1.2"))))
    assert(Lexer("3.4ı1.") == Right(List(Number("3.4ı1."))))
    assert(Lexer("3.4ı.2") == Right(List(Number("3.4ı.2"))))
    assert(Lexer("3.4ı.") == Right(List(Number("3.4ı."))))
    assert(Lexer(".ı.") == Right(List(Number(".ı."))))
    assert(Lexer("3.4ı") == Right(List(Number("3.4ı"))))
    assert(Lexer(".4") == Right(List(Number(".4"))))
    assert(Lexer(".") == Right(List(Number("."))))
  }

  test("Does the lexer recognise strings?") {
    assert(
      Lexer(""" "Hello, Vyxal!" """) == Right(List(Str("Hello, Vyxal!")))
    )
    assert(
      Lexer(""" "Hello, Vyxal!" """) == Right(List(Str("Hello, Vyxal!")))
    )

    assert(
      Lexer(""" "Vyxal is what \"you\" want!" """) == Right(
        List(Str("Vyxal is what \"you\" want!"))
      )
    )

    assert(
      Lexer(""" k"vy """) == Right(
        List(Digraph("k\""), MonadicModifier("v"), Command("y"))
      )
    )
  }

  test("Does the lexer recognise a basic series of tokens?") {
    assert(
      Lexer("1 1 +") == Right(
        List(Number("1"), Number("1"), Command("+"))
      )
    )
  }

  test("Does the lexer differentiate between strings and dictionary strings?") {
    assert(
      Lexer(""" "Hello, Vyxal!" """) == Right(List(Str("Hello, Vyxal!")))
    )
    assert(
      Lexer(""" "Hello, Vyxal!” """) == Right(
        List(DictionaryString("Hello, Vyxal!"))
      )
    )
  }

  test("Does the lexer recognise comments?") {
    assert(
      Lexer("1 1 + ##Hello, Vyxal!") == Right(
        List(Number("1"), Number("1"), Command("+"), Comment("##Hello, Vyxal!"))
      )
    )
  }

  test("Does the lexer recognise monadic modifiers?") {
    assert(
      Lexer("1 2 3W +/") == Right(
        List(
          Number("1"),
          Number("2"),
          Number("3"),
          Command("W"),
          Command("+"),
          MonadicModifier("/")
        )
      )
    )
  }

  test("Does the lexer recognise variable digraphs?") {
    assert(
      Lexer("3 #$my_var +") === Right(
        List(Number("3"), GetVar("my_var"), Command("+"))
      )
    )

    assert(Lexer("42 #=answer") === Right(List(Number("42"), SetVar("answer"))))
  }
end LexerTests