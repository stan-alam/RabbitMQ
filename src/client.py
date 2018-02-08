/*

technical implementation tasks required by the NYSE street publisher to complete

1. Connect to the RabbitMQ server

2. Obtain a channel

3. Declare a queue

4. Bind the queue with the exchange

5. Consume the messages

6. Close the channel

7. Close the connection


*/

import pika
credentials = pika.PlainCredentials("stan", "guest")
conn_params = pika.ConnectionParameters("localhost",  credentials = credentials)
conn_broker = pika.BlockingConnection(conn_params)
channel.exchange_declare(exchange = "NYSE",
                        type="direct",
                        passive=False,
                        durable=True,
                        auto_delete=False)
channel.queue_declare(queue="client")
