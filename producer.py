import sys
import pika


def queue_task(message = "Hello world"):

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='hello' , durable=True) #durable makes the queue stay even after server restart

    channel.basic_publish(exchange='' , routing_key='hello' , body=message , properties=
                          pika.BasicProperties(
                            delivery_mode = 2 # making the message persistent
                         ))

    print("Message:{} sent to the queue".format(message))

    connection.close()
