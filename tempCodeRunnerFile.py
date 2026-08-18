nums = [1,0,1]
i=0
j=i+1
while j<len(nums):
    if nums[j]!=0:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1

    j+=1
print(nums)   