# First way to run a bunch of threads.  Note the .join() at the end
threads = []
x = threading.Thread(target=thread_function, args=(1,))
threads.append(x)
x = threading.Thread(target=thread_function, args=(2,))
threads.append(x)
x = threading.Thread(target=thread_function, args=(3,))
threads.append(x)
x.start()
threads[0].join()
threads[1].join()
threads[2].join()

# Second, better, way to run a bunch of threads.  NOte, no .join()
import concurrent.futures

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(thread_function, range(3))


## Race condition:  many threads access the same piece of data without locking it for read/write
