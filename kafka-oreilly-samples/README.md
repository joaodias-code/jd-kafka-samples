# jd-kafka-samples
 Practicing kafka using some examples from Kafka guide O'Reilly. I modified the code for practicing. 

 Requirements:
 1. Install Java SDK
 2. Install Zookeeper:
    + Download: https://www.apache.org/dyn/closer.cgi/zookeeper/
    + Extract the files and rename the file /conf/zoo_sample.cfg to zoo.cfg
    + Open the file zoo.cfg and set the "dataDir=" with the directory of zookeeper
    + Open the file zkServer.cmd or .sh (windows or linux), and
    + Set the variable %JAVA% with the correct name of the system variable java in your computer
    + Set the system variable ZOOKEEPER_HOME with the directory of Zookeeper.
    + Open command and try zkserver to start.
 3. Install kafka:
    + Download:
    + Extract the files
    + Go to your Kafka config directory. Example: C:\dev\kafka_2.11-0.9.0.0\config
    + Edit the file “server.properties.”
    + Find and edit the line log.dirs=/tmp/kafka-logs” to “log.dir= C:\kafka_2.11-0.9.0.0\kafka-logs.
    + Verify in the server.properties the port of zookeeper (zookeeper.connect=)
    + Start running: .\bin\windows\kafka-server-start.bat .\config\server.properties
