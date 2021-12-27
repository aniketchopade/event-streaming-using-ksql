CREATE STREAM txn_stream
    WITH (KAFKA_TOPIC='trans',
        VALUE_FORMAT='AVRO');
--------------
CREATE STREAM atm_transactions_stream
WITH (
KAFKA_TOPIC = 'atm_transactions',
VALUE_FORMAT = 'AVRO'
) AS SELECT
*
FROM txn_stream
WHERE description = 'ATM';
---------------------------------
CREATE STREAM imps_transactions_stream
WITH (
KAFKA_TOPIC = 'imps_transactions',
VALUE_FORMAT = 'AVRO'
) AS SELECT
*
FROM txn_stream
WHERE description = 'IMPS';
---------------------------------
CREATE STREAM cash_transactions_stream
WITH (
KAFKA_TOPIC = 'cash_transactions',
VALUE_FORMAT = 'AVRO'
) AS SELECT
*
FROM txn_stream
WHERE description = 'Cash';