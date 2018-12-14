import threading
import time
import logging

def worker():
    """thread worker function"""
    print('Worker')

def worker_n(n):
    """thread worker function"""
    print('Worker %s' % n)
    time.sleep(3)
    print('Ending Worker %s' % n)


def worker_name():
    logging.debug(threading.current_thread().getName() + ' Starting')
    time.sleep(0.2)
    logging.debug(threading.current_thread().getName() + ' Exiting')

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    #t.start()

    t = threading.Thread(target=worker_n, args=[i])
    threads.append(t)
    #t.start()

def my_service():
    logging.debug(threading.current_thread().getName() +  ' Starting')
    time.sleep(0.3)
    logging.debug(threading.current_thread().getName() + ' Exiting')


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
)

t = threading.Thread(target=my_service, name='my_service')
w = threading.Thread(target=worker_name, name='worker_name')
w2 = threading.Thread(target=worker_name)  # use default name

w.start()
t.start()
w2.start()


