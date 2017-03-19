import json
import logging
import time
from twisted.internet import defer, reactor

from stompest.config import StompConfig
from stompest.protocol import StompSpec

from stompest.async import Stomp
from stompest.async.listener import SubscriptionListener
from zoolock.zoolockprocess import Zoolockprocess

class Consumer(object):
    QUEUE = '/queue/adtest'
    ERROR_QUEUE = '/queue/adtestConsumerError'

    def __init__(self, config=None):
        if config is None:
            config = StompConfig('tcp://localhost:61613')
        self.config = config

    @defer.inlineCallbacks
    def run(self):
        client = Stomp(self.config)
        yield client.connect()
        headers = {
            # client-individual mode is necessary for concurrent processing
            # (requires ActiveMQ >= 5.2)
            StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL,
            # the maximal number of messages the broker will let you work on at the same time
            'activemq.prefetchSize': '100',
        }
        client.subscribe(self.QUEUE, headers, listener=SubscriptionListener(self.consume, errorDestination=self.ERROR_QUEUE))

    def consume(self, client, frame):
        """
        NOTE: you can return a Deferred here
        """
        data = json.loads(frame.body.decode())
        print('Received frame with count %d' % data['count'])
        time.sleep(1)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    hosts = "c878jrn.int.thomsonreuters.com:2181, c965bhn.int.thomsonreuters.com:2181, c670ysk.int.thomsonreuters.com:2181"
    lock_name = "lock"
    process = Zoolockprocess(hosts, lock_name)
    Consumer().run()
    reactor.run()
    process.release_lock()

