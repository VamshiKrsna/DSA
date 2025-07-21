test = [20,12,10,15,2] # testing array for sorting

def selection_sort(arr: list[int]):
    arr_len = len(arr)
    for step in range(arr_len):
        minimum = step
        for i in range(step+1, arr_len):
            if (arr[i] < arr[minimum]):
                minimum = i
    (arr[step], arr[minimum]) = (arr[minimum], arr[step])

    return arr
# code dry runs :
# Logic
# - first element as minimum
# - compare next with the minimum, if found less, update it as minimum
# - go on until last element
# - every iteration places minimum in front of unsorted list

for step in range(len(test)):
    minimum = step
    for i in range(step+1, len(test)):
        if test[i] < test[minimum]:
            minimum = i
    (test[step], test[minimum]) = (test[minimum],test[step])

print(test)
print(selection_sort(test))
