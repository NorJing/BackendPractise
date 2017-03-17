from stompest.config import StompConfig
from activemq_queue.producer import Producer
from time import time
import threading
import logging
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

def producer_send(producer, message):
    producer.send(destination=QUEUE, body=message.encode())

if __name__ == '__main__':
    start_time = int(round(time()))
    print("start=%s" % start_time)
    CONFIG = StompConfig(uri='tcp://pcdtcwf13d.emea1.cis.trcloud:61613', login="admin", passcode="admin")
    QUEUE = '/topic/adtest'

    producer = Producer(CONFIG)
    producer.connect()

    for i in range(0, 1000):
        message = str(i) + "_" + str(round(time())*1000)
        producer_t = threading.Thread(name="Producer_thread_" + str(i), target=producer_send, args=(producer, message))
        producer_t.start()

    if not producer.send:
        producer.disconnect()
        print("producer disconnect")

    end_time = int(round(time()))
    print("end=%s" % end_time)
    total_time = end_time-start_time
    print("total_time=%d" % total_time)



