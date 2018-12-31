import pikli
from threading import Thread

from worker import start_worker
from producer import queue_task

def run_worker(arg):
    workers = pikli.get_int("workers")
    for i in range(workers):
        Thread(target=start_worker , args=(i+1,)).start()

    print("{} Workers are waiting for tasks".format(workers))

def run_task(arg):
    msg = pikli.get_str("message")
    queue_task(msg)


root = pikli.Command(
    use = "rabbit",
    short = "rabbit is a cli app",
    long = "rabbit is a cli app to demonstrate the use of pika & rabbitmq",

)

worker = pikli.Command(
    use = "worker",
    short = "the consumers/workers to execute tasks",
    run = run_worker
)

worker.flags().intp("workers" , "w" , 2 , "the number of workers")

root.add_command(worker)

task = pikli.Command(
    use = "task",
    short = "The task to queue",
    run = run_task
)

task.flags().stringp("message" , "m" , "Hello World" , "the message in string")

root.add_command(task)
