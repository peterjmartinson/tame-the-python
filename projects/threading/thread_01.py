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
    x = threading.Thread(target=thread_function, args=(1,))
    # x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")




## Running NOT as a Daemon
## 08:48:28: Main    : before creating thread
## 08:48:28: Main    : before running thread
## 08:48:28: Thread 1: starting
## 08:48:28: Main    : wait for the thread to finish
## 08:48:28: Main    : all done
## 08:48:30: Thread 1: finishing  ## < note, program has finished, but execution must wait for the thread to complete

## Running as a Daemon
## 09:03:21: Main    : before creating thread
## 09:03:21: Main    : before running thread
## 09:03:21: Thread 1: starting
## 09:03:21: Main    : wait for the thread to finish
## 09:03:21: Main    : all done  ## < note, program finishes, and kills the daemon thread
