def bubble_sort(arr):
    """
    Perform optimized bubble sort on a list, ignoring non-numeric elements.

    :param arr: List of elements to be sorted.
    :return: Sorted list with only numeric elements sorted.
    """
    # 过滤出数字元素
    numeric_elements = [x for x in arr if isinstance(x, (int, float))]
    n = len(numeric_elements)
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if numeric_elements[j] > numeric_elements[j+1]:
                numeric_elements[j], numeric_elements[j+1] = numeric_elements[j+1], numeric_elements[j]
                swapped = True
        if not swapped:
            break
    
    # 将非数字元素添加回原数组位置
    sorted_arr = []
    num_index = 0
    for element in arr:
        if isinstance(element, (int, float)):
            sorted_arr.append(numeric_elements[num_index])
            num_index += 1
        else:
            sorted_arr.append(element)
    
    return sorted_arr
