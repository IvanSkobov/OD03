#сортировка выбором

a = [7, -2, 9, 4, 8, 6, 1, 5, 3, -10]

def selection_sort(arr):
   for i in range(len(arr)):
       min_index = i
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       arr[i], arr[min_index] = arr[min_index], arr[i]
selection_sort(a)

print(a)