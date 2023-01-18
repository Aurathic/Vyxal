addSbtPlugin("org.portable-scala" % "sbt-scalajs-crossproject" % "1.1.0")
addSbtPlugin("org.scala-js" % "sbt-scalajs" % "1.10.0")
addSbtPlugin("ch.epfl.scala" % "sbt-scalajs-bundler" % "0.20.0")
// For making an uber JAR
addSbtPlugin("com.eed3si9n" % "sbt-assembly" % "2.0.0")
// For auto-formatting
addSbtPlugin("org.scalameta" % "sbt-scalafmt" % "2.4.3")
// For linting
addSbtPlugin("ch.epfl.scala" % "sbt-scalafix" % "0.10.4")