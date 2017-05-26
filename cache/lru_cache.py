class LRUCacheNode:
  def __init__(self, k, v):
      self.key = k
      self.value = v
      self.prev = None
      self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = LRUCacheNode(None, 'head')
        self.tail = LRUCacheNode(None, 'tail')
        self.head.next = self.tail # tail being most recent
        self.tail.prev = self.head # head being oldest
        self.data = {}

    def deleteNode(self,node):
        assert(node is not self.head and node is not self.tail)
        del self.data[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def get(self,key):
        if key not in self.data:
            return -1
        node = self.data[key]
        # take the node out
        node.prev.next = node.next
        node.next.prev = node.prev
        # insert into most recent position
        self.insertNew(node)
        return node.value

    def put(self, key, value):
        # remove old value if present
        if key in self.data:
            self.deleteNode(self.data[key])

        # create new node
        newNode = LRUCacheNode(key,value)
        self.data[key] = newNode

        # if over limit, delete oldest node
        if len(self.data) > self.capacity:
            self.deleteNode(self.head.next)

        self.insertNew(newNode)

    def insertNew(self,newNode):
        # insert new node into last position    
        last = self.tail.prev
        last.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = last