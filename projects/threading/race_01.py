import time
import logging
import threading
import concurrent.futures


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.info("Thread %s: make local copy", name)
        local_copy = self.value
        logging.info("Thread %s: increment local copy", name)
        local_copy += 1
        time.sleep(0.1)
        logging.info("Thread %s: update database", name)
        self.value = local_copy
        logging.info("Thread %s: finishing update", name)

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.info("Thread %s about to lock", name)
        with self._lock:
            logging.info("Thread %s has lock", name)
            logging.info("Thread %s: make local copy", name)
            local_copy = self.value
            logging.info("Thread %s: increment local copy", name)
            local_copy += 1
            time.sleep(0.1)
            logging.info("Thread %s: update database", name)
            self.value = local_copy
            logging.info("Thread %s: now value is %d", name, self.value)
            logging.info("Thread %s about to release lock", name)
        logging.info("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            # executor.submit(database.update, index) # .submit() returns a 'future' object that has its own set of methods
            executor.submit(database.locked_update, index) # .submit() returns a 'future' object that has its own set of methods
    logging.info("Testing update. Ending value is %d.", database.value)
