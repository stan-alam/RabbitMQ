## intro notes

Messages are not published directly to a queue, instead, the producer sends the messages to an exchange.
An exchange is responsible for the routing of the messages to the different queues.
**An exchange accepts messages from the producer application and routes them to message queues with the help of bindings and routing keys**.

1. The producer publishes a message to an exchange. When you create the exchange, you have to specify the type of it.

2. The exchange receives the message and is now responsible for the routing of the message. **The exchange takes different message attributes into account,
such as routing key, depending on the exchange type.

3. Bindings have to be created from the exchanges to queues. **The exchange routes the message into the queues, depending on message attributes.**

4. The messages stay in the queue until they are handled by a consumer.

5. The consumer handles the message.


## Types of exchanges

**Direct** A direct exchange delivers messages to queues based on a message routing key. In a direct exchange, the message is routed to the queues whos
binding key exactly matches the routing key of the message. If the queue is bound to the exchange with the binding key **i_m__a_process** , a message
published to the exchange with a routing key such as **i_m__a_process** will be routed to that queue.

**Fan out** A fanout exchange routes messages to all of the queues that are bound to it.

**Topic** The topic exchange does a wildcard match between the routing key and the routing pattern specified in the bindding.

**Headers** Headers exchanges use the message header attributes for routing.

# RabbitMQ and server concepts

Understand the default Virtual host, the default user, and the default permissions ---

## Producer aka pub :

**application that receives the messages**

## Consumer aka sub :

**Application that receives the message**

## Queue :

**Buffer that stores messages**

## Message :

**Information that is sent from the producer to a consumer through RabbitMQ**

## Connection:

**is a TCP connection between the application and the RabbitMQ broker**

## Channel :

**A connection is a virtual connection inside a connection. When the app is pub/sub-ing messages to a queue, it is done through a CHANNEL**

## Exchange :

**Exchange receives messages from producers and pushes them to queues depending on rules defined by the exchange type**
**In order to receive messages, a queue needs to be bound to at least one exchange**

## Binding :

**A binding is a link between a queue and an exchange.**

## Routing Key:

**The routing key is a key that the exchange looks at to decide how to route the messages to queues. The routing key is like the ADDRESS for the message**

## AMQP :

**Advanced Message Queuing Protocol** is the main protocol used by RabbitMQ

## Users :

**usernames and passwords can be assigned to RMQ with the ability for privileges/rights within instances.**

## Vhost, virtual host :

**A virtual host provides a way to segregate applications using the same RMQ instance** Different users can have different access privileges to different
hosts, queues, exchanges all on a vhost.