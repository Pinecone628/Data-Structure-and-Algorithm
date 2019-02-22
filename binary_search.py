

def binary_search(alist, item):
    """recursive"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)

    return False


def binary_search2(alist, item):
    """not recursive"""
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False




if __name__ == "__main__":
    li = [1,4,346,6346,765]
    print(binary_search2(li, 346))
    print(binary_search2(li, 5))