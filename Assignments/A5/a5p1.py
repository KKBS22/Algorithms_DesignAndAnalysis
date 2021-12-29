import math
unsorted_array = [1, 2, 3, 4, 5, 6, 8]
a = [0, 1, 2, 3, 1, 1, 1, 1]


def main():
    #merge_sort(unsorted_array, 1, len(unsorted_array))
    majority_element_rec(0, len(unsorted_array)-1)
    print(f(a, 0, len(a) - 1))
    #ele = max_ele(unsorted_array)
    # print(ele)
    # merge_sort_two(unsorted_array)
    # print(unsorted_array)
    pass


def merge_sort_two(inp_arr):
    size = len(inp_arr)
    if size > 1:
        middle = size // 2
        left_arr = inp_arr[:middle]
        right_arr = inp_arr[middle:]

        merge_sort_two(left_arr)
        merge_sort_two(right_arr)
        merge(inp_arr, left_arr, right_arr)


def merge(inp_arr, left_arr, right_arr):
    p = 0
    q = 0
    r = 0

    left_size = len(left_arr)
    right_size = len(right_arr)
    while p < left_size and q < right_size:
        if left_arr[p] < right_arr[q]:
            inp_arr[r] = left_arr[p]
            p += 1
        else:
            inp_arr[r] = right_arr[q]
            q += 1
        r += 1

    while p < left_size:
        inp_arr[r] = left_arr[p]
        p += 1
        r += 1

    while q < right_size:
        inp_arr[r] = right_arr[q]
        q += 1
        r += 1


def max_element(array_val, low, high):
    g_list = []
    if(low == high):
        temp_list = []
        return temp_list.append(array_val[low])
    else:
        mid = math.floor((low+high)/2)
        left = max_element(array_val, low, mid)
        right = max_element(array_val, mid+1, high)
        for a in left:
            for b in right:
                if a == b:
                    g_list.append(a)

    pass


def f(arr, low, high):
    if low == high:
        return arr[low]

    if low + 1 == high:
        return arr[low] if arr[low] == arr[high] else None

    n = high - low + 1
    mid = (low + high) // 2

    l = f(arr, low, mid)
    r = f(arr, mid + 1, high)

    if (l == r):
        return l

    counts = [0, 0]

    for i in range(low, high + 1):
        print(low, "Running", high)
        if arr[i] == l:
            counts[0] = counts[0] + 1
        if arr[i] == r:
            counts[1] = counts[1] + 1

    return (counts[0] > (n//2) or counts[1] > (n//2))

# def main():
   # a = [14,46,43,27,57,41,45,21,70]
    count = 0
    #nlist = [14,46,43,27,57,41,45,21,70]
    #mergeSort(nlist, 7)
    #a = [5, 9, 3, 5, 5, 21, 5, 7, 17, 5, 5, 5]
    # print(majorityElement(a))
    print(f(a, 0, len(a) - 1))
    #f(nlist, 0,5)
    # print(nlist)
    # print(count)


def max_ele(array):
    i = 1
    count = 1
    n = len(array)
    while (i < len(array)):
        while ((i < n) and (array[i] == array[i-1])):
            i = i + 1
            count = count + 1
        if (count > n/2):
            return array[i-1]
        count = 1
        i = i + 1
    return -1


def majorityElement(nums, lo=0, hi=None):
    def majority_element_rec(lo, hi):
        # base case; the only element in an array of size 1 is the majority
        # element.
        if lo == hi:
            return nums[lo]

            # recurse on left and right halves of this slice.
        mid = (hi-lo)//2 + lo
        left = majority_element_rec(lo, mid)
        right = majority_element_rec(mid+1, hi)

        # if the two halves agree on the majority element, return it.
        if left == right:
            return left

            # otherwise, count each element and return the "winner".
        left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

        return left if left_count > right_count else right


if __name__ == "__main__":
    main()
