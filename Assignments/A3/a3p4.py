def main():
    #sorted_array = Iterative_insertion_sort([6, 5, 4, 3, 2, 1])
    # print(sorted_array)
    Iterative_insertion_sortTest([5, 4, 3, 2, 1])


def Iterative_insertion_sort(ArrayList):
    C1 = 0
    C2 = 0
    for i in range(1, (len(ArrayList))):
        C1 = C1 + 1
        for j in range(1, (i+1)):
            if ArrayList[i] < ArrayList[j]:
                tmp = ArrayList[i]
                for k in range(i, j+1, -1):
                    ArrayList[k] = ArrayList[k - 1]
                ArrayList[j] = tmp
    return ArrayList


def Iterative_insertion_sortTest(A):
    n = 0
    n1 = 0
    n2 = 0
    for i in range(2, (len(A) + 1)):
        print("1st loop")
        n1 = n1 + 1
        for j in range(1, (i - 1 + 1)):
            print("2nd loop")
            n2 = n2 + 1
            #print("j: ", j)
            # print("A[i]: ", A[i-1])
            # print("A[j]: ", A[j-1])
            if A[i-1] < A[j-1]:
                print("3rd loop")
                tmp = A[i-1]
                #print("Tmp: ", tmp)
                for k in range(i, j, -1):
                    n = n + 1
                    #print("K: ", k)
                    # print("A[K]: ", A[k-1])
                    A[k-1] = A[k - 1 - 1]
                    # print("A[K-1]: ", A[k- 1 - 1])
                    # print("A[K]': ", A[k - 1])
                A[j-1] = tmp
                # print("A[j]': ", A[j - 1])
        print("n3: ", n)
        print("n2: ", n2)
        print("n1: ", n1)
    return A


if __name__ == '__main__':
    main()
