import random
import threading
import time
import logging


class MyThread(threading.Thread):

    def run(self):
        """thread worker function"""
        pause = random.randint(1, 5)
        logging.debug('sleeping %0.2f', pause)
        time.sleep(pause)
        logging.debug('ending')


logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)

for i in range(3):
    t = MyThread(daemon=True)
    t.start()

for t in threading.enumerate():
    logging.debug('Alive %s : %s' % (t.getName(), t.isAlive()))

    if t is threading.main_thread():
        continue

    if t.isAlive():
        logging.debug('joining %s', t.getName())
        t.join()