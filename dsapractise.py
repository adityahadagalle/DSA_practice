nums = [1,2,1,1,1]
k = 3
dict={}
pre=0
maxindex=0
for i in range(len(nums)):
    pre+=nums[i]
    val=pre-k
    if pre == k:
        max_len = i + 1
    if val in dict:
        index=i-dict[val]
        maxindex=max(maxindex,index)
    else:
        dict[pre] = dict.get(pre,0) + 1
print(maxindex)


nums = [23,2,6,4,7]
k = 6
dict={}
pre=23
found=False
for i in range(1,len(nums)):
    pre+=nums[i]
    val=pre%k 
    if val in dict:
        if i-dict[val]>1:
            found=True
            print("true")
            break
    else:
        dict[val] = i
if found!=True:
    print(False)
    
    
nums = [4,5,0,-2,-3,1]
k = 5
dictt={0:1}
pre=0
count=0
for i in range(len(nums)):
    pre+=nums[i]
    val=pre%k
    if val in dictt:
        count+=dictt[val]
    
    dictt[val]=dictt.get(val,0)+1  
        
print(count)