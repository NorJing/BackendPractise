# import logging
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)

from stompest.sync import Stomp

class Base(Stomp):
    def __init__(self, config):
        super(Base, self).__init__(config)
