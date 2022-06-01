import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")

    threads = []
    x = threading.Thread(target=thread_function, args=(1,))
    threads.append(x)
    x.start()
    x = threading.Thread(target=thread_function, args=(2,))
    threads.append(x)
    x.start()
    x = threading.Thread(target=thread_function, args=(3,))
    threads.append(x)
    x.start()
    threads[0].join()
    threads[1].join()
    threads[2].join()
