import logging
import threading
import time
import random
import concurrent.futures

SENTINEL = object()

def producer(pipeline):
    """Pretend we're getting a message from the network."""
    for index in range(10):
        message = random.randint(1,101)
        logging.info("Producer got message: %s", message)
        pipeline.set_message(message, "Producer")

    # Send a sentinel message to tell consumer we're done
    pipeline.set_message(SENTINEL, "Producer")

def consumer(pipeline):
    """Pretend we're saving a number in the database."""
    message = 0
    while message is not SENTINEL:
        message = pipeline.get_message("Consumer")
        if message is not SENTINEL:
            logging.info("Consumer storing message: %s", message)

class Pipeline:
    """
    Class to allow a single element pipeline between producer and consumer.
    """
    def __init__(self):
        self.message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire() # this locks the consumer out?  producer can add messages, but consumer can't read them yet

    def get_message(self, name):
        logging.debug("%s: about to acquire getlock", name)
        self.consumer_lock.acquire() # makes Consumer wait until a message is ready
        logging.debug("%s: has getlock", name)
        message = self.message
        logging.debug("%s: about to release setlock", name)
        self.producer_lock.release() # allows Producer to insert the next message into Pipeline
        logging.debug("%s: setlock released", name)
        return message

    def set_message(self, message, name):
        logging.debug("%s: about to acquire setlock", name)
        self.producer_lock.acquire()
        logging.debug("%s: has setlock", name)
        self.message = message
        logging.debug("%s: about to release getlock", name)
        self.consumer_lock.release()
        logging.debug("%s: getlock released", name)





if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # logging.getLogger().setLevel(logging.DEBUG)

    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)
