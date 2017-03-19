import logging
logging.basicConfig(level=logging.DEBUG)
from kazoo.client import KazooClient
from kazoo.recipe.lock import Lock
import os, time

if __name__ == "__main__":
    hosts = "c878jrn.int.thomsonreuters.com:2181, c965bhn.int.thomsonreuters.com:2181, c670ysk.int.thomsonreuters.com:2181"
    lock_name = "lock"
    path = os.path.join("/adlock/" + lock_name)

    zk_client = KazooClient(hosts=hosts)
    logging.info("create zk client")
    zk_client.start()
    logging.info("start zk client")
    zk_client.ensure_path(path=path)
    lock = Lock(client=zk_client, path=path)
    logging.info("create lock")
    lock.acquire(blocking=True, timeout=None)
    logging.info("get lock")
    for i in range(20):
        print(i)
        time.sleep(1)
    lock.release()
    logging.info("release lock")
