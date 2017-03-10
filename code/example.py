# -*- coding: utf-8 -*-

import time
import sys

import stomp

class MyListener(stomp.ConnectionListener):
    def on_error(self, headers, message):
        print('received an error "%s"' % message)

    def on_message(self, headers, message):
        print('received a message "%s"' % message)

conn = stomp.Connection12(host_and_ports=[("c481vwy.int.thomsonreuters.com", 61613)])
conn.set_listener('MyListener', MyListener())
conn.start()
conn.connect('admin', 'password', wait=True, headers={'client-id': 'SampleClient'})

# conn.subscribe(destination='/topic/test', id=1, ack='auto')
conn.subscribe(destination='/topic/dtest', id=1, headers={'activemq.subscriptionName': 'SampleSubscription'})

for i in range(1, 5):
    message="I come to Oslo " + str(i) + " times!"
    conn.send(body=''.join(message), destination='/topic/dtest')

time.sleep(2)
conn.disconnect()
