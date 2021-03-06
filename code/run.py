from stompest.config import StompConfig
from stompest.protocol import StompSpec
from activemq_queue.consumer import Consumer
from activemq_queue.producer import Producer
from db import CassandraInstance
from time import time
import threading
import logging
logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] (%(threadName)-10s) %(message)s')

def producer_send(producer, message):
    producer.send(destination=QUEUE, body=message.encode())

def consumer_receive(consumer, cassandraInstance):
    frame = consumer.receiveFrame()
    consumer.ack(frame)
    cassandraInstance.write_one_row_from_queue("%s" % frame.body.decode())
    cassandraInstance.get_one_row()
    logging.debug('Exiting')

def consumer_receive_print(consumer):
    frame = consumer.receiveFrame()
    print("Get %s" % frame.info())
    consumer.ack(frame)

if __name__ == '__main__':
    start_time = int(round(time()))
    print("start=%s" % start_time)
    CONFIG = StompConfig(uri='tcp://pcdtcwf13d.emea1.cis.trcloud:61613', login="admin", passcode="admin")
    QUEUE = '/topic/adtest'

    consumer = Consumer(CONFIG)
    consumer.connect()
    consumer.subscribe(QUEUE, {StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL})

    cassandraInstance = CassandraInstance()
    cassandraInstance.connect_session('monitorkeyspace')

    producer = Producer(CONFIG)
    producer.connect()

    for i in range(0, 10):
        message = str(i) + "_" + str(round(time())*1000)
        producer_t = threading.Thread(target=producer_send, args=(producer, message))
        producer_t.start()

    i = 0
    while consumer.canRead:
        # consumer.canRead(0): Check that queue is empty.
        consumer_t = threading.Thread(name="Consumer_thread_" + str(i), target=consumer_receive, args=(consumer, cassandraInstance))
        consumer_t.setDaemon(True)
        consumer_t.start()
        consumer_t.join()
        i += 1
        end_time = int(round(time()))
        total_time = end_time-start_time
        print("total_time=%d" % total_time)

    producer.disconnect()
    print("producer disconnect")
    consumer.disconnect()
    print("consumer disconnect")

    end_time = int(round(time()))
    print("end=%s" % end_time)
    total_time = end_time-start_time
    print("total_time=%d" % total_time)



