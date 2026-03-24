# #list pratiece questions
# num =[10,20,40,30,50]
# print(num)
# num.append(60)
# print(num)
# num.insert(1,70)
# print(num)
# num.remove(70)
# print(num)

# for i in num:
#     print(i)

# #find largest number

# nums=num.copy()

# nums.insert(1,70)
# largest =nums[0]

# for i in nums:
#     if i > largest:
#         largest = i

# print("largest:",largest)


# #find smallest
# nums.append(5)
# smallest=-nums[0]


# for i in nums:
#     if i < smallest:
#         smallest =i

# print("smallest no:",smallest)


# #count no of evens

# even = [x for x in nums if x % 2 == 0 ]
# print(even)

# # using loop
# evens=[]
# for i in nums:
#     if i % 2 == 0:
#         evens.append(i)

# print(len(evens))

# # reverse a string using loops

# print(nums)
# nums.reverse()
# print(nums)

# # ascending 

# nums.sort()
# print(nums)

# #duplicates remove
# nums.append(10)
# nums.append(20)
# print(nums)

# dup =[]
# for i in nums:
#     if i not  in dup:
#         dup.append(i)

# print(dup)



# #find the secopnd largets element 

# nums =[10,30,50,20,70,60,40]
# nums.sort()
# print(nums)
# secLargest = nums[len(nums)-2]
# print(secLargest)

id =[1,2,3,4,5,6]
names=["ram","sam","chin","gop","sop"]
size =len(names)
print(size)
data =[]
for i in range(0,size-1):
    info = {
       " id":id[i],
        "name":names[i]
    }
    data.append(info)

print(data)
