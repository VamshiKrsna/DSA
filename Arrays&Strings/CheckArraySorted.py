# checks if a array is sorted or not 

#Method 1 : attempt 1 

temp = [1,2,3,4,5,6] 
temp1 = [34,54,12,1,0]

def method1(arr):
    flag = True 
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i+1]:
            flag = False 
            print("Array is not sorted")
            return 
    else: 
        print("Sorted")

if __name__ == "__main__": 
    (method1(temp))
    (method1(temp1))