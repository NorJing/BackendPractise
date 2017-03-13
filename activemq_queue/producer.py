# import logging
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)

# from stompest.config import StompConfig
from stompest.sync import Stomp
# from time import time, sleep

class Producer(Stomp):
    def __init__(self, config):
        super(Producer, self).__init__(config)

"""
if __name__ == '__main__':
    CONFIG = StompConfig(uri='tcp://pcdtcwf13d.emea1.cis.trcloud:61613', login="admin", passcode="admin")
    QUEUE = '/topic/adtest'

    producer = Producer(CONFIG)
    producer.connect()

    for i in range(1, 50):
        message = str(round(time())*1000)
        sleep(0.01)
        producer.send(destination=  QUEUE, body=message.encode())

    producer.disconnect()
"""