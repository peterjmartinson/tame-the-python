## Using a Queue and threading.Event

import logging
import threading
import time
import random
import concurrent.futures
import queue

SENTINEL = object()

def producer(pipeline, event):
    """Pretend we're getting a message from the network."""
    # for index in range(10):
    while not event.is_set():
        message = random.randint(1,101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer we're done
    # pipeline.set_message(SENTINEL, "Producer")

    logging.info("Producer received EXIT event. Exiting")

def consumer(pipeline, event):
    """Pretend we're saving a number in the database."""
    message = 0
    # while message is not SENTINEL:
    while not event.is_set() or not pipeline.empty():
        message = pipeline.get_message("Consumer")
        logging.info("Consumer storing message: %s  (queue size=%s)", message, pipeline.qsize())
        # if message is not SENTINEL:
            # logging.info("Consumer storing message: %s", message)
        time.sleep(1)
    logging.info("Consumer received EXIT event. Exiting")

class Pipeline(queue.Queue):
    """
    Class to allow a single element pipeline between producer and consumer.
    """
    def __init__(self):
        super().__init__(maxsize=10)
        # self.message = 0
        # self.producer_lock = threading.Lock()
        # self.consumer_lock = threading.Lock()
        # self.consumer_lock.acquire() # this locks the consumer out?  producer can add messages, but consumer can't read them yet

    def get_message(self, name):
        # logging.debug("%s: about to acquire getlock", name)
        # self.consumer_lock.acquire() # makes Consumer wait until a message is ready
        # logging.debug("%s: has getlock", name)
        # message = self.message
        # logging.debug("%s: about to release setlock", name)
        # self.producer_lock.release() # allows Producer to insert the next message into Pipeline
        # logging.debug("%s: setlock released", name)
        # return message
        logging.debug("%s: about to get from queue", name)
        value = self.get()
        logging.debug("%s: got %d from queue", name, value)
        return value

    # def set_message(self, message, name):
    def set_message(self, value, name):
        # logging.debug("%s: about to acquire setlock", name)
        # self.producer_lock.acquire()
        # logging.debug("%s: has setlock", name)
        # self.message = message
        # logging.debug("%s: about to release getlock", name)
        # self.consumer_lock.release()
        # logging.debug("%s: getlock released", name)
        logging.debug("%s: about to add %d to queue", name, value)
        self.put(value)
        logging.debug("%s: added %d to queue", name, value)





if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()
