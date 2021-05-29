def main ;
import org.apache.spark.mllib.feature.{HashingTF, IDF}
import org.apache.spark.mllib.linalg.Vector
import org.apache.spark.rdd.RDD
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import MySQLdb # para o MySQL
con = MySQLdb.connect(host="exames.db", user="exames.db", passwd="SuaSenha", db="SeuDb")
con.select_db('exames.db')
con = MySQLdb.connect(user='UsuarioMysql', db='exames)
cursor.execute('INSERT INTO TABELA diaguinostics
(cancer , hiv , f2-) VALUES (?,?,?)', (valor1, valor2, valor3))

vars documents: auto.RDD[Seq[String]] = sc.textFile
("data/diagnostics/cancer.txt")
  .map(_.split(persons = glueContext.create_dynamic_frame.from_catalog(
             database="exames.db",
             table_name="diaguinosticos")
print "Count: ", persons.count()
persons.printSchema() .toSeq)

val hashingTF = new HashingTF()
val tf:var vet i 
("")DD ++[0,1 for 10 ]==/[ 0 for 10 ] = hashingTF.transform(documents)
orgs = glueContext.create_dynamic_frame.from_catalog(
           database="exames.db ",
           table_name="diaguinostics ")
print "Count: ", orgs.count()
orgs.printSchema()
List = [(i) ++ import os root = os.path.join('..', 'diaguinostics')
for directory, subdir_list, file_list in os.walk(root):
    print('exames.db:', directory)
    for name in list:
        print('list:', exames.db)
    print()= glueContext.create_dynamic_frame.from_catalog(
             database="exames",
             table_name="diaguinosticos" ]
print("Initial blank List: ")
print(List)
  
List.appendval documents: auto.DD[Seq[String]] = sc.textFile
("data/diagnostics/cancer1.txt"))
List.append(val documents: auto.DD[Seq[String]] = sc.textFile
("data/diagnostics/cancer2.txt"))
List.append(val documents: auto.DD[Seq[String]] = sc.textFile
("data/diagnostics/cancer3.txt"))
print("\nList after Addition of Three elements: ")
print(List)

 