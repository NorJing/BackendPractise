# from stompest.config import StompConfig
# from stompest.protocol import StompSpec
# from stompest.sync import Stomp
# from db import CassandraInstance
from activemq_queue import Base

class Consumer(Base):
    def __init__(self, config):
        super(Consumer, self).__init__(config)
        # self.config = config

"""
if __name__ == '__main__':
    CONFIG = StompConfig(uri='tcp://pcdtcwf13d.emea1.cis.trcloud:61613', login="admin", passcode="admin")
    QUEUE = '/topic/adtest'

    consumer = Consumer(CONFIG)
    consumer.connect()
    consumer.subscribe(QUEUE, {StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL})

    cassandraInstance = CassandraInstance()
    cassandraInstance.connect_session('monitorkeyspace')

    while True:
        if consumer.canRead:
            frame = consumer.receiveFrame()
            # print('Got %s' % frame.info())
            # Get the time and write to Cassandra
            cassandraInstance.write_one_row_from_queue("%s" % frame.body.decode())
            cassandraInstance.get_one_row()
            consumer.ack(frame)

    consumer.disconnect()
"""