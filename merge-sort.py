import math

def merge_sort(l, r, seq):
    print(l, r)
    if l == r:
        return [seq[l]]
    
    m = (r + l) // 2
    n1 = m - l + 1 # [r, ..., m, m + 1, ..., l]
    n2 = r - m

    left = merge_sort(l, m, seq)
    right = merge_sort(m + 1, r, seq)
    left.append(math.inf)
    right.append(math.inf)

    i = 0
    j = 0
    k = 0

    result = []


    while (k != n1 + n2):
        print(result)
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
        k += 1

    return result


l = [8, 5, 2, 7, 3, 6, 4, 11, 9]
merge_sort(0, len(l) - 1, l)