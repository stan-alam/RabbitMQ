"""

technical implementation tasks required by the NYSE street publisher to complete for client

1. Connect to the RabbitMQ server

2. Obtain a channel

3. Declare a queue

4. Bind the queue with the exchange

5. Consume the messages

6. Close the channel

7. Close the connection


"""

import pika
credentials = pika.PlainCredentials("stan", "stan123") 
conn_params = pika.ConnectionParameters("localhost",  credentials = credentials) #create connection string to broker 
conn_broker = pika.BlockingConnection(conn_params) # get channel
channel.exchange_declare(exchange = "NYSE",
                        type="direct",
                        passive=False,
                        durable=True,
                        auto_delete=False)
channel.queue_declare(queue="client")
channel.queue_bind(queue="client", exchange = "NYSE", routing_key="hola!")

def msg_consumer(channel, method, header, body):
	channel.basic_ack(delivery_tag=method.delivery_tag)
	if body == "quit":
		channel.basic_cancel(consumer_tag="NYSE-consumer")
		channel.stop_consuming()
	else:
		print body
	return
channel.basic_consume(msg_consumer, queue="client", consumer_tag="client-hello")
channel.start_consuming()
