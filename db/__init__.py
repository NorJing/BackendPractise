# import logging
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)

import time

from cassandra.cluster import Cluster

class CassandraInstance():
    def __init__(self):
        self.server = "pcdtccas05t.emea1.cis.trcloud"
        self.cluster = Cluster(['pcdtccas05t.emea1.cis.trcloud'], port=9042)
        self.session = None

    def connect_session(self, keyspace):
        self.session = self.cluster.connect(keyspace)

    def get_all_rows(self):
        rows = self.session.execute('select id, time from monitortable')
        for row in rows:
            print(row.id, row.time)

    def get_one_row(self):
        rows = self.session.execute("select id, time from monitortable where id='2'")
        for row in rows:
            print("id=%s" % row.id, "time=%s" % row.time)

    def write_one_row_to_cassandra(self):
        millis = str(round(time.time()))
        self.session.execute(
            """
            INSERT INTO monitortable (id, time)
            VALUES (%s, %s)
            """,
            ("2", millis)
        )

    def write_one_row_from_queue(self, time):
        self.session.execute(
            """
            INSERT INTO monitortable (id, time)
            VALUES (%s, %s)
            """,
            ("2", time)
        )

"""
if __name__ == "__main__":
    cassandraInstance = CassandraInstance()
    cassandraInstance.connect_session('monitorkeyspace')
    # cassandraInstance.write_one_row_to_cassandra()
    cassandraInstance.get_one_row()
"""
