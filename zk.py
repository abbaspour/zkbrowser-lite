from kazoo.client import KazooClient

class ZooKepperConnection:
    def __init__(self, host, root = "/"):
        self.zk = KazooClient(hosts='127.0.0.1:2181')
        self.zk.start()
        self.root = root

    def disconnect(self):
        self.zk.stop()

    def children(self, path):
        p = self.root + path
        return self.zk.get_children(p)

    def raw_data(self, path):
        return self.zk.get(self.root + path)
