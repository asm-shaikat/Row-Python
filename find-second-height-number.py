n = int(input("How many array elements:"))
ary = []
for i in range(n):
    x1 = int(input("Enter array elements:"))
    ary.append(x1)
if(ary[0]<ary[1]):
    largest = ary[1]
    second_largest = ary[0]
else:
    largest = ary[0]
    second_largest = ary[1]
for i in range(1, len(ary)):
    if(ary[i]>largest):
        second_largest = largest
        largest = ary[i]
    elif(ary[i]>second_largest and ary[i]!=largest):
        second_largest = ary[i]

print("Second largest is ",second_largest)
