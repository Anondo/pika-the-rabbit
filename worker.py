import pika
import time



def start_worker(worker_no):

    def callback(ch , method , properties , body):
        print("Receiving: {}".format(body))
        time.sleep(body.count(b'.')) #pretending to be busy
        print("Worker:{} have successfully received message:{}".format(worker_no , body))

        ch.basic_ack(delivery_tag = method.delivery_tag) #send a ack for requeuing a message whenever a message is not delivered to a worker


    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    channel = connection.channel()

    channel.queue_declare(queue='hello' , durable=True)

    channel.basic_qos(prefetch_count=1) # unless 1 task is completed, no new task will be assigned to the worker

    channel.basic_consume(callback , queue='hello')

    channel.start_consuming()

    print("Worker:{} just died".format(worker_no))
