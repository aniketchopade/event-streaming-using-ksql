# Event streaming using KSQL

This project runs Kafka with KSQL DB cluster. Use this project to demonstrate how to use KSQL query to stream events.

## Spin up Kafka-cluster
    - run `cd kafka && docker-compose up`
    - By default this will spin up KSQL in interactive mode.
  
### Create MongoDb database
   - Create account on atlas mongodb
   - Create a database cluster and obtain its connection string   
   - In your cluster database with name bank and collection name as transactions.
   - set environment variable $CONNECTION_STRING. Example export CONNECTION_STRING=mongodb+srv://<id>:<pw>@<cluster-id>/<dbname>. 

### Define Avro schema 
    - Sample records are in `kafka-ops\data\btrecs*.csv`
    - Create Avro schema files in `kafka-ops\avro` folder.     
    - For this example data is taken in this format 
        `Date,Description,Deposits,Withdrawls,Balance
        20-Aug-2020,NEFT,"23,237.00",00.00,"37,243.31"
        20-Aug-2020,NEFT,00.00,"3,724.33","33,518.98"`

### Run program
    - `cd kafka-ops`
    - `python3 send_record.py --topic <topic-name> --schema-file <filename-without-avro-preix> --collection-name <mongo-collection-name>`      
    - This will start producing messages to topic 
  
### Interacting with KSQL
    - KSQL UI - use control center
    - KSQL CLI -  `docker exec -it ksqldb-cli ksql http://ksqldb-server:8088`
    - Example queries in `kafka\ksqldb-config\queries.sql`
     
### Event streaming
    - After you execute queries in KSQL UI/ shell
    - All cash transactions will be streamed to cash_transactions and so on..    