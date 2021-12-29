def majority_element_rec(arrrayVal, lo, hi):
    # base case; the only element in an array of size 1 is the majority
    # element.
    if lo == hi:
        return arrrayVal[lo]

        # recurse on left and right halves of this slice.
    mid = (hi-lo)//2 + lo
    left = majority_element_rec(arrrayVal, lo, mid)
    right = majority_element_rec(arrrayVal, mid+1, hi)

    # if the two halves agree on the majority element, return it.
    if left == right:
        return left

    # otherwise, count each element and return the "winner".
    left_count = 0
    right_count = 0
    for i in range(lo, hi+1):
        if arrrayVal[i] == left:
            left_count = left_count + 1
    for j in range(lo, hi+1):
        if arrrayVal[j] == left:
            right_count = right_count + 1

    print("LC", left_count)
    print("RC", right_count)

    if left_count > right_count:
        print(left)
        return left
    elif right_count > left_count:
        print(right)
        return right
    else:
        return right


def main():
    valueTest = majority_element_rec([3, 2, 3, 4], 0, 3)
    print(valueTest)


if __name__ == "__main__":
    main()
