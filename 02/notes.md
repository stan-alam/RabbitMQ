## Rabbit MQ 02

## Think of Rabbit as a router for your software

## Rabbit MQ is focused on application-to-application messaging**

**PUB/SUB or Consumers and producers**

        Rabbit as a delivery service.
        Your app can send and receive packages. The server with the data you need can
        send and receive too. The role RabbitMQ plays is as the router between your app and
        the “server” it's talking to.

When an app connects to RabbitMQ, it will make a decision : **am I sending or receiving i.e.
am I a producer or a consumer**

## Producers create messages and publish them by sending them to a broker server(FIX) (rabbitMQ)

## A message has two parts: a payload and a label

## The Payload is the data to be transmitted

## Usually JSON, XML, ASCII, garbage in, garbage out

# label

## Describes the payload and how RabbitMQ will determine who should get a copy of the message

**unlike TCP/IP where the sender specifies a specific receiver, AMQP protocol only describes the
message with a label (an exchange name and optional tag)**

**RabbitMQ delegates the messages to the receiver depending on the label**

Think of this communication as fire and forget and one-directional.

**consumers attach to a broker server and subscribe to a** *queue*


          Think of a queue as a named mailbox. Whenever a message arrives in a particular
          mailbox, RabbitMQ sends it to one of the subscribed/listening consumers. By the
          time a consumer receives a message, it now only has one part: a payload. The labels
          attached to the message don’t get passed along with the payload when the message is
          routed. RabbitMQ doesn’t even tell you who the producer/sender was.

          From the outside it’s simple: producers create messages and consumers receive
          them. Your app can be a producer when it needs to send a message to another app, or
          it can be a consumer when it needs to receive. It can also switch between the two. But
          before it can do either it has to set up a channel.

## Important

Connect to rabbitMQ with TCP and authentication has taken place, the app then creates an **AMQP**
channel. This channel is a virtual connection inside the TCP, connection and its over the channel
that AMQP commands are sent over. **Every Channel has a unique ID assigned to it THE AMQP LIB will
delegate and store the IDs) When publishing a message, subscribing to a queue, or receiving a message
is done over this channel.**

## The significance of channels -- performance

Setting up a tcp connection is expensive for the OS. e.g. hundreds of concurrent threads/connections per second
at high load periods.

Channels allow you to use one TCP connection for all threads, but get the same privacy as giving each thread its
own connection on the existing connection and gets own private communication path to rabbitMQ without any additional
load on the OS's TCP stack

          As a result, you can create a channel hundreds or
          thousands of times a second without the OS without getting problems
**There is no limit to how many AMQP channels you can create over a TCP connection**

If you think of each channel as a bundle in a fiber optic cable, then each fiber can transmit just like the
channel. The cable has many fiber strands, allowing it all the connected threads to transmit and receive
simultaneously via multiple strands. A TCP connection is the cable and the AMQP channel is the individual strand.

**The important thing** -- remember that consumers and producers is they map to the ideas of sending and receiving
rather than Client/server **Think of this as a enhanced transport layer, i.e. the way these messages work, and AMQP**

There are three parts to any successful routing of an AMQP message: **exchanges, queues, and bindings**
queues are where the messages end up and are received by consumers and bindings  are how the messages get routed
from the exchange to particular queues.

**When talking about producers and consumers, queues are like named mailboxes. They're where messages end up and wait
to be consumed. Consumers receive messages from a particular queue in one of two ways:**

  1. By subscribing to a via the *basic.consume*  AMQP command. Sets the channel for receive use until unsubscribed from
  the queue. The channel will be set to receive mode until a unsubscribed from the queue. While subscribed,
  your consumer will automatically receive another message from the queue, after consuming (or rejecting) the last
  received message. Use the basic.consume if your consumer is processing many messages out of the queue and/or needs to
  automatically receive message from a queue as soon as they arrive.

  2. When not persistently subscribed. Requesting a single message from the queue is done by
  the (basic.get) **AMQP** command. This will cause the consumer to receive the next message in the queue and then not
  receive anymore messages until another basic.get is called. DON't USE basic.get in a loop as a substitute to
  basic.consume, **basic.get is resource intensive in comparison to basic.consume**

  When using RabbitMQ 2.x use the basic.reject AMQP command basic.reject allows the consumer to reject a message RabbitMQ
  has sent. Based on certain rules -- RabbitMQ will decide to which queue it should deliver the message. Those rules are
  called *routing keys*. A queue is said to be *bound* to an exchange by a routing key. When you send a message to the broker,
  it will have a routing key -- even a blank one -- which RabbitMQ will try to match to the routing keys used in the bindings
  If they match, the message will be delivered to the queue. If the routing message doesn't match any of binding patterns,
  it'll be black-holed. **both your producers and consumers should attempt to create the queues that will be needed**

  You can implement logic to allow for messages to be lost and a way to republish those messages.
  Queues are the foundational block of AMQP messaging :

    * They give you a place for messages to wait for consumption
    * Queues are great for load balancing. **you can attach many consumers and
    let RabbitMQ round-robin incoming messages evenly among them**
    * They're the final endpoint for any messages in RabbitMQ (unless they are black-holed)

## Exchange and bindings

AMQP bindings and exchanges. When a message is delivered to a queue, you do it by sending it to the exchange.
Then based on the rules/criteria of the routing RabbitMQ will decide to which queue it should deliver the message
A queue is said to be *bound* to an exchange by a routing key. By sending a message to the broker, it'll have a routing-key
Rules are like setting up junk-mail for email. Spam goes to junk-mail.

AMQP can accommodate cases when you can bind a queue to an exchange with no routing key and then every message with no routing key that
is sent will be to that particular exchange will be delivered to said queue just like email.

**Complex use cases that involve publish/subscribe or multicast can be achieved.**


          The publisher—the process that is sending messages to the
          broker—doesn’t have to care about the logic on the other side of the broker (the
          queues and consumers involved in processing the messages). As you’ll see, this can
          lead to interesting messaging scenarios that aren’t possible—or are very hard to
          Getting together: exchanges and bindings 21
          accomplish—with a broker that only
          allows you to publish directly to queues.


# There are four different exchanges provided by the protocol.

## Direct   

## Fanout

## Topic

## Headers
-------------------------------------------------------------------------------------------------------------------------------------------------
# Direct   

  * simple: if the routing key matches, then the message is delivered to the corresponding queues
