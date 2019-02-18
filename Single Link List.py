class SingleNode(object):
    """The node of single link list"""

    def __init__(self, item):
        # _item is the data saved in this note
        # _next is the index of next note
        self.item = item
        self.next = None


class SingleLinkList(object):
    """Single Link List"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """Judge if it is empty"""
        return self._head is None

    def length(self):
        """Return the length of the Single Link list"""
        cur = self._head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """travel the Single Link list"""
        cur = self._head

        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """Add item  in the head"""
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """Add item at the end of the Single Link list"""
        node = SingleNode(item)
        if self._head is None:
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
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
        cur = self._head
        while cur is not None:
            if cur.item == item:
                return True
            else:
                cur = cur.next
        return False

    def remove(self, item):
        """Remove the item"""
        cur = self._head
        pre = None

        while cur is not None:
            if cur.item == item:
                if pre is None:
                    self._head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


if __name__ == "__main__":
    sl = SingleLinkList()
    sl.append(1)
    print(sl.search(1))
    sl.append(2)
    sl.add(3)
    sl.insert(2, 4)
    sl.travel()
    sl.remove(4)
    print(sl.search(6))
    sl.travel()