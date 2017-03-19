import logging
logging.basicConfig(level=logging.DEBUG)
from kazoo.client import KazooClient
from kazoo.recipe.lock import Lock
import os, time

class Zoolockprocess(object):
    def __init__(self, hosts, lock_name):
        self.hosts = hosts
        self.lock_name = lock_name
        self.path = os.path.join("/adlock/" + lock_name)
        self.lock = None

        self.process_lock()

    def process_lock(self):
        zk_client = KazooClient(hosts=self.hosts)
        logging.info("create zk client")
        zk_client.start()
        logging.info("start zk client")
        zk_client.ensure_path(path=self.path)
        self.lock = Lock(client=zk_client, path=self.path)
        logging.info("create lock")
        self.lock.acquire(blocking=True, timeout=None)
        logging.info("get lock")
        # self.do_something()
        # lock.release()
        # logging.info("release lock")

    def release_lock(self):
        self.lock.release()

    def do_something(self):
        for i in range(20):
            print(i)
            time.sleep(1)

if __name__ == "__main__":
    hosts = "c878jrn.int.thomsonreuters.com:2181, c965bhn.int.thomsonreuters.com:2181, c670ysk.int.thomsonreuters.com:2181"
    lock_name = "lock"

    process = Zoolockprocess(hosts, lock_name)
    for i in range(50):
        print(i)
        time.sleep(1)
    process.release_lock()
