## Using a Queue and threading.Event

import logging
import threading
import time
import random
import concurrent.futures
import queue

SENTINEL = object()

def producer(queue, event):
    """Pretend we're getting a message from the network."""
    while not event.is_set():
        message = random.randint(1,101)
        logging.info("Producer got message: %s", message)
        queue.put(message)
    logging.info("Producer received EXIT event. Exiting")

def consumer(queue, event):
    """Pretend we're saving a number in the database."""
    message = 0
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info("Consumer storing message: %s  (queue size=%s)", message, pipeline.qsize())
        # time.sleep(1)
    logging.info("Consumer received EXIT event. Exiting")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.getLogger().setLevel(logging.DEBUG)

    # pipeline = Pipeline()
    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
