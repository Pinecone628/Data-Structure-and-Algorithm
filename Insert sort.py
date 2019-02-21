
def inset_sort(alist):
    n = len(alist)
    for i in range(1, n):
        while i > 0:
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                i -= 1
            else:
                break

if __name__ == "__main__":
    li = [54, 2323, 26, 93, 17, 44, 22, 676,11111]
    print(li)
    inset_sort(li)
    print(li)
