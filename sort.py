#-*- coding: utf-8 -*-

def selectionSort(arr):
    """
    시간 O(n^2)
    공간 O(n)
    (현재위치에 값을 찾음)
    정렬되지 않은 리스트를 첫번째 index에서부터 시작
    해당 index값을 포함하여 그 뒤 값들과 비교하고 최소값과 위치를 바꾼다. (swap)
    """
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertionSort(arr):
    """
    시간 O(n^2) -> 정렬이 되어있는경우 O(n)
    공간 O(n)
    (현재위치에서 그 이전값들을 비교하여 맞는 자리에 삽입함)
    두번째 index부터 시작한다.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def bubbleSort(arr):
    """
    시간 O(n^2)
    공간 O(n)
    (매번 연속된 index를 비교하여 큰 값을 위로 올림)
    두번째 index부터 시작한다.
    """
    for i in range(0, len(arr)):
        for j in range(1, len(arr)-i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

def mergeSort(arr):
    """
    시간 O(NlogN)
    공간 O(2N)
    (Divide and conquer)
    Divide
    배열크기가 1일때까지 쪼갠다.
    conquer
    배열 2개 A, B를 앞에서부터 비교해서 새로운 배열 C에 넣는다.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(left, right):
    total = []
    while(len(left)>0 or len(right)>0):
        try:
            if left[0] < right[0]:
                total.append(left[0])
                left = left[1:]
            else:
                total.append(right[0])
                right = right[1:]
        except IndexError:
            if len(left) == 0:
                total.append(right[0])
                right = right[1:]
            else:
                total.append(left[0])
                left = left[1:]
    return total
        

def quickSort(arr):
    """
    시간 O(NlogN) 분할깊이 logN, 이미 정렬된 경우 최악 O(N^2) 분할깊이 N
    공간 O(N)
    (Divide and conquer)
    랜덤으로 pivot 값을 기준으로 right, left
    pivot 기준으로 left < pivot, pivot < right
    left, right에서 각각 pivot 또 선택, pivot 기준으로 값 정렬
    list의 변동이 없으면 끝
    """
    if len(arr) <= 1: 
        return arr
    pivot = arr[len(arr) // 2] # 그러나 여기서 만약 pivot 이 첫번째라면?? - 상관없
    left, right, equal = [], [], []
    for item in arr:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            equal.append(item)
    return quickSort(left) + equal + quickSort(right)

if __name__ == '__main__':
    sortedList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    sampleList = [1, 10, 3, 5, 7, 4, 6, 2, 9, 8, 0]
    if selectionSort(sampleList) != sortedList:
        print("selectionSort Error")

    sampleList = [1, 10, 3, 5, 7, 4, 6, 2, 9, 8, 0]
    if insertionSort(sampleList) != sortedList:
        print("insertionSort Error")

    sampleList = [1, 10, 3, 5, 7, 4, 6, 2, 9, 8, 0]
    if bubbleSort(sampleList) != sortedList:
        print("bubbleSort Error")

    sampleList = [1, 10, 3, 5, 7, 4, 6, 2, 9, 8, 0]
    if mergeSort(sampleList) != sortedList:
        print("mergeSort Error")

    sampleList = [1, 10, 3, 5, 7, 4, 6, 2, 9, 8, 0]
    if quickSort(sampleList) != sortedList:
        print("quickSort Error")