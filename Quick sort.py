def quick_sort(alist, start, end):
    if start >= end:
        return
    mid_value = alist[start]
    low = start
    high = end

    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value
    quick_sort(alist, start=start, end=low-1)
    quick_sort(alist, start=low+1, end=end)

if __name__ == "__main__":
    li = [54, 26, 93, 17, 44, 22, 676]
    print(li)
    quick_sort(li, start=0, end=len(li)-1)
    print(li)