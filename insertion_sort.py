#сортировка вставками
a = [7, -2, 9, 4, 8, 6, 1, 5, 3, -10]

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insert_sort(a)
print(a)