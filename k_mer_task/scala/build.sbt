lazy val commonSettings = Seq(
 organization := "group4",
 version := "1.0",
 scalaVersion := "2.11.12"
)
lazy val root = (project in file(".")).
 settings(commonSettings: _*).
 settings(
   name := "kmer",
// https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-core
libraryDependencies += "org.apache.hadoop" % "hadoop-core" % "1.2.1"
)
libraryDependencies += “org.apache.spark” % “spark-core_2.10” % “2.1.1”
assemblyMergeStrategy in assembly := {
 case PathList("META-INF", xs @ _*) => MergeStrategy.discard
 case x => MergeStrategy.first
}
