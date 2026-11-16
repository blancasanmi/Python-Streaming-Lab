"""
pipeline.py
----------------
This file launches BOTH producer and consumer using Python threads to simulate
a real streaming pipeline.

"""

import threading
from queue import Queue
from producer import CSVProducer
from consumer import Consumer

def main():
    """
    TODO:
    - Create the shared queue.
    - Instantiate the producer and consumer.
    - Create a thread for each.
    - Start both threads.
    - Optionally join them so the program runs continuously.

    The students should run:
        python pipeline.py
    and observe live streaming behavior.
    """

    q = Queue()
    producer = CSVProducer("transactions.csv", q)
    consumer = Consumer(q)
    
    print("Creating the threads...")
    t_prod = threading.Thread(target = producer.start)
    t_cons = threading.Thread(target = consumer.start)

    threads = [t_prod, t_cons]

    print("Starting the threads...")
    t_prod.start()
    t_cons.start()
    #for t in threads: 
     #   t.start()

    t_prod.join()
    t_cons.join()
     

if __name__ == "__main__":
    print("Starting the Python Streaming Pipeline...")
    main()
