class SingleNode(object):
    """The node of single link list"""

    def __init__(self, item):
        # _item is the data saved in this note
        # _next is the index of next note
        self.item = item
        self.next = None


class SingleCycleLinkList(object):
    """Single Link List"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """Judge if it is empty"""
        return self._head is None

    def length(self):
        """Return the length"""

        if self.is_empty():
            return 0
        count = 1
        cur = self._head
        while cur.next is not self._head:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """travel the  list"""
        if self.is_empty():
            return
        cur = self._head
        while cur.next is not self._head:
            print(cur.item, end=" ")
            cur = cur.next
        print(cur.item)

    def add(self, item):
        """Add item  at the head of list"""
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next is not self._head:
                cur = cur.next
            node.next = self._head
            self._head = node
            cur.next = node

    def append(self, item):
        """Add item at the end"""
        node = SingleNode(item)
        if self._head is None:
            self._head = node
            node.next = node
        else:
            cur = self._head
            while cur.next is not self._head:
                cur = cur.next
            node.next = self._head
            cur.next = node

    def insert(self, pos, item):
        """Add item at the pos"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            pre = self._head
            while count < (pos-1):
                count += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def search(self, item):
        """Find the whether the item exists in the list, return True or False"""
        if self.is_empty():
            return False
        cur = self._head
        while cur.next is not self._head:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        if cur.item == item:
            return True
        return False

    def remove(self, item):
        """Remove the item"""
        if self.is_empty():
            return
        cur = self._head
        pre = None
        while cur.next is not self._head:
            if cur.item == item:
                if pre is None:
                    rear = self._head
                    while rear.next is not self._head:
                        rear = rear.next
                    self._head = cur.next
                    rear.next = self._head
                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next
        if cur.item == item:
            if cur == self._head:
                self._head = None
            else:
                pre.next = cur.next

if __name__ == "__main__":
    sl = SingleCycleLinkList()
    sl.append(1)
    print(sl.search(1))
    sl.append(2)
    sl.add(3)
    sl.insert(2, 4)
    sl.travel()
    sl.remove(2)
    print(sl.search(6))
    sl.travel()