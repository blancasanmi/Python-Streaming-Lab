"""
consumer.py
----------------
This file contains the logic for a Consumer that continuously reads messages
from the queue and processes them.

The Consumer runs forever, just like a streaming system.
"""

import time
from queue import Queue

class Consumer:
    def __init__(self, q):
        """
        PARAMETERS:
        - q : the shared queue (simulated topic)

        TODO:
        - Store the queue.
        - Initialize any state variables you may want later,
          e.g. a running total for stateful computations.
        """
        self.q = q
        state = "initializing"
        

    def start(self):
        """
        Main loop of the consumer.

        TODO:
        - Continuously call q.get() to receive events.
        - Print the event received.
        - Pass it to the process() function.
        """
        while True: 
            event = self.q.get()
            print(f"Event received: {event}")
            # self.process(event)
    

    def process(self, event):
        """
        TODO:
        - Simulate some processing time using time.sleep().
        - Transform fields (e.g., convert amount to float).
        - Implement optional filtering conditions.
        - Update any state (example: running total).
        """
        time.sleep(5)
        for value in event: 
            if type(value) == "int":
                value = float(value)
                

            if type(value) == "str" and len(value) < 10:
                print("Short string ! I'll make it even shorter")
                value = value / 2


# Debugging test

if __name__ == "__main__":
    """
    Run this alone to see consumer behavior.

    Note: It will block waiting for messages since no producer is running.
    """
    from queue import Queue
   
    q = Queue()
   
    print("Adding test data to queue\n"
          )
    q.put({'id': '1', 'name': 'Alice', 'amount': '150'})
    q.put({'id': '2', 'name': 'Bob', 'amount': '75'})
    q.put({'id': '3', 'name': 'Charlie', 'amount': '200'})
    consumer = Consumer(q)
    consumer.start()
