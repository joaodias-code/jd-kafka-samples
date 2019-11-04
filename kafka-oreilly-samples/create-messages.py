# start kafka
cd dev\kafka_2.12-2.3.1\bin\windows
kafka-server-start.bat c:\dev\kafka_2.12-2.3.1\config\server.properties

# create topic
cd dev\kafka_2.12-2.3.1\bin\windows
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic testejoao

# describe topic
cd dev\kafka_2.12-2.3.1\bin\windows
kafka-topics.bat --zookeeper localhost:2181 --describe --topic testejoao

# produce messages
cd dev\kafka_2.12-2.3.1\bin\windows
kafka-console-producer.bat --broker-list localhost:9092 --topic testejoao
teste mensagem 1

# consume messages
cd dev\kafka_2.12-2.3.1\bin\windows
kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic testejoao