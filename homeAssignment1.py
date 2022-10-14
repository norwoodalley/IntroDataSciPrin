#defining function and dividing list into two parts
def mergeSort(alist):
    if len(alist) > 1:
        left_alist = alist[:len(alist)//2]
        right_alist = alist[len(alist)//2:]

        #recursion part 
        mergeSort(left_alist)
        mergeSort(right_alist)

        # merging part
        # left_alist
        l = 0
        #right_alist
        r = 0
        #merged_alist
        m = 0
        while l < len(left_alist) and r < len(right_alist):
            if left_alist[l] < right_alist[r]:
                alist[m] = left_alist[l]
                l += 1
                m += 1
            else:
                 alist[m] = right_alist[r]
                 r += 1
                 m += 1
        while l < len(left_alist):
            alist[m] = left_alist[l]
            l += 1
            m += 1
        while r < len(right_alist):
            alist[m] = right_alist[r]
            r += 1
            m += 1

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)