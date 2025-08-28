# largest element in array with and without sorting
temp = [1, 4,5,22,5,65,75,333]

temp1 = temp.sort() 
print(temp[-1])  

# without sorting

maxi = temp[0] 
for i in range(1,len(temp)):
    if temp[i] > maxi:
        maxi = temp[i]
print(maxi)

# Second largest element in array
largest_element = temp[0] 
second_largest = -1 

for i in range(1, len(temp)):
    if (temp[i] > largest_element):
        second_largest = largest_element
        largest_element = temp[i]

    # to handle the case where the largest element is at zero index : 
    elif (temp[i] > second_largest and temp[i] != largest_element):
        second_largest = temp[i]
        
print(second_largest)