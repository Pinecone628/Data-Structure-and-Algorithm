class queue(object):

    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        """Add"""
        self.__list.append(item)

    def dequeue(self):
        return self.__list.pop(0)

    def is_empty(self):
        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    s = queue()
    s.enqueue(1)
    s.enqueue(2)
    s.enqueue(3)
    s.enqueue(4)
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())
    print(s.dequeue())