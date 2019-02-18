class SingleNode(object):
    """node"""

    def __init__(self, item):
        # _item is the data saved in this note
        # _next is the index of next note
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """Double Link List"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """Judge if it is empty"""
        return self._head is None

    def length(self):
        """Return the length of the Double Link list"""
        cur = self._head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """travel the Double Link list"""
        cur = self._head

        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """Add item  in the head"""
        node = SingleNode(item)
        if self._head is None:
            self._head = node
        else:
            node.next = self._head
            self._head = node
            self._head.prev = node

    def append(self, item):
        """Add item at the end"""
        node = SingleNode(item)
        if self._head is None:
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """Add item at the pos"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            node = SingleNode(item)
            count = 0
            cur = self._head
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.prev = cur
            node.next = cur.next
            cur.next.prev = node
            cur.next = node

    def search(self, item):
        """Find the whether the item exists, return True or False"""
        cur = self._head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        """Remove the item"""
        if self.is_empty():
            return
        else:
            cur = self._head
            while cur is not None:
                if cur.item == item:
                    if cur == self._head:
                        self._head = cur.next
                        if cur.next is not None:
                            cur.next.prev = None
                    else:
                        cur.prev.next = cur.next
                        if cur.next:
                            cur.next.prev = cur.prev
                    break
                else:
                    cur = cur.next


if __name__ == "__main__":
    ll = DoubleLinkList()
    ll.add(200)
    ll.append(3)
    ll.insert(2, 4)
    ll.append(5)
    print("length:",ll.length())
    ll.travel()
    print(ll.search(3))
    print(ll.search(4))
    ll.remove(200)
    print("length:",ll.length())
    ll.travel()
