"""

technical implementation tasks required by the NYSE street publisher 
1. Connect to the RabbitMQ server

2. Obtain a channel

3. Declare the exchange

4. Create a message

5. Publish the message

6. Close the channel

7. Close the connection


"""

import pika
import sys

credentials = pika.PlainCredentials("stan", "stan123")
conn_params = pika.ConnectionParameters("localhost", credentials = credentials)
conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()

channel.exchange_declare(exchange=NYSE")