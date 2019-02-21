class stack(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        """Add item at the end"""
        self.__list.append(item)

    def pop(self):
        """pop the item at the list"""
        return self.__list.pop()

    def peek(self):
        """return the last item"""
        if self.__list:
            self.__list[-1]
        else:
            return None

    def is_empty(self):

        return self.__list == []

    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    s = stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())