## Rabbit MQ

Data delivery, nonblocking operations, or push notifications. Pub/Sub, asynch processing, or work queues.
All these patterns form the *messaging* canvas.

**Messaging is a critical property it enables software applications to connect and scale**

Applications can connect to each other as components of a larger application, or to user devices and
data.

Messaging is essentially asynch in that it decouples applications by separating the sending and receiving
of data. **Scale is critical**

**Big Data**

**Data in Motion**

**RabbitMQ** is an open source message broker and queueing server that can be used to let disparate
applications share data via a common protocol by simple queue jobs

**Rabbit Queues to store jobs and let the broker perform the load balancing and job distribution**

**With RabbitMQ you can leverage message queuing to decouple your module from the authentication server.
with every page request, your authentication module is designed to place an authorization request message
into RabbitMQ.**

        The authentication server then listens to RabbitMQ queue that receivs that request message. Once
        the request is approved, the auth server puts a reply message back into RabbitMQ where it's routed
        to the queue that your module is listening to.



## Messing queueing is connecting your applications together with messages that are routed between them by a
## message broker like RabbitMQ

      What Teknekron’s TIB allowed application developers to do was establish a set
      of rules for describing message content. As long as the messages were published
      according to those rules, any consuming application could subscribe to a copy of the
      messages tagged with topics it was interested in.

      Producers and consumers of information
      could now be completely decoupled and flexibly mixed on-the-fly. Either side of
      the PubSub model (producer/consumer) was completely interchangeable without
      breaking the opposite side. The only thing that needed to remain stable was the TIB
      software and the rules for tagging and routing the information

      Except for Qpid, RabbitMQ is the only broker implementing the AMQP open
      standard.

**Clustering is ridiculously simple on RabbitMQ because of Erlang.**
