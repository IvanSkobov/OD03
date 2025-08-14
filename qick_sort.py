#быстрая сортировка
def quick_sort(s):
    if len(s) <= 1:
        return s
    element = s[0]
    left = list(filter(lambda i: i < element, s))
    right = list(filter(lambda i: i > element, s))
    center = list(filter(lambda i: i == element, s))
    return quick_sort(left) + center + quick_sort(right)

print(quick_sort([7, 2, 9, 4, 8, 6, 1, 5, 3, 10]))