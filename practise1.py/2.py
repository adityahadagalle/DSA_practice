    # nums = [1,5,4,2,9,9,9]
# k = 3

# left = 0
# freq = {}
# summ = 0
# best = 0

# for right in range(len(nums)):
#     freq[nums[right]] = freq.get(nums[right], 0) + 1
#     summ += nums[right]

#     if right - left + 1 == k:

#         if len(freq) == k:
#             best = max(best, summ)

#         summ -= nums[left]

#         freq[nums[left]] -= 1

#         if freq[nums[left]] == 0:
#             del freq[nums[left]]

#         left += 1

# print(best)




# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
# zeros=0
# best=0
# left=0
# for right in range(len(nums)):
#     if nums[right]==0:
#         zeros+=1
#     while zeros>k:
#         if nums[left]==1:
#             left+=1
#         else:
#             zeros-=1
#             left+=1
#     best=max(best,right-left+1)    
# print(best)            
            
            
            
            
# s = "abcdabcdebb"
# left=0
# freq={}
# best=0
# for right in range(len(s)):
#     freq[s[right]] = freq.get(s[right], 0) + 1
#     while freq[s[right]]>1:
#         freq[s[left]]-=1
#         if freq[s[left]] == 0:
#             del freq[s[left]]
#         left+=1    
            
#     best=max(best,right-left+1)
        
# print(best)                




# nums = [23,2,4,6,7]
# k = 13
# freq={0:-1} 
# pre=0
# for i in range(len(nums)):
#     pre+=nums[i]
#     rem=pre%k
#     if rem in freq:
#         if i-freq[rem]>=2:
#             print(True)
#             break
#     else:
#         freq[rem] = i
        
        
    
    
    
    
######################recursion#################################################recursion#################################################recursion#################################################recursion###########################

# def fun(count):
#     if count==3:
#         return
#     print("Adii")
#     count+=1
#     fun(count)
# fun(count=0)  



# def fun(i,n):
#     if i==6:
#         return
#     print(i)
#     fun(i+1,n)
# fun(i=1,n=6)  


# def fun(i,n):
#     if i<n:
#         return
#     print(i)
#     fun(i-1,n)
# fun(10,1)      
    
    
# def fun(n):
#     if n==1:
#         return 1
#     return n*fun(n-1)    

# print((fun(5)))


# def fun(n):
#     if n==1:
#         return 1
#     return n+fun(n-1)
# print(fun(10))
    
# i=0
# j=0  
# def fun(i,j,arr):

#     if i>=j:
#         return True
#     if arr[i]==arr[j]:
#         i+=1
#         j-=1
#     else:
#         return False
#     return fun(i,j,arr)
# print(fun(i=0,j=4,arr="madam") )   


# def fun(x,n):
#     if n==1:
#         return x
#     return x*fun(x,n-1)
# print(fun(2,5))




# def fun(n):
#     if n==0:
#         return 1
#     if n==1:
#         return 1
#     return fun(n-1)+fun(n-2)
# print(fun(5))

# def fun(n,m):
#     if n==1 or m==1:
#         return 1
#     return fun(n,m-1)+fun(n-1,m)
# print(fun(3,3))


# def fun(i,arr):
#     if i >= len(arr):
#         return 0
#     rob=arr[i]+fun(i+2,arr)
#     skip=fun(i+1,arr)
#     return max(rob,skip)
# print(fun(0,[2,7,9,3,1]))



# def fun(i,arr):
#     if i>=len(arr):
#         return 0
#     rob=arr[i]+fun(i+2,arr)
# #     skip=arr[i+1]
# #     return max(rob,skip)
# # print(fun(i=0,arr=[3,2,7,10]))

# ###########################backtracking#####################################################################
# "How many choices do I have at each recursive step?"

# If the answer is:

# 2 choices → Think Take/Skip.
# Many choices → Think Loop.



# def backtrack(index):

#     if index == len(nums):
#         ans.append(path[:])
#         return

#     # Take
#     path.append(nums[index])
#     backtrack(index+1)

#     # Undo
#     path.pop()

#     # Skip
#     backtrack(index+1)


# nums = [1,2,3]

# ans = []
# path = []

# backtrack(0)

# print(ans)         


# def backtrack(index):

#     if index == len(nums):  
#         ans.append(path[:])
#         return

#     # Take
#     if path[-1]!=path[:]:
#         path.append(nums[index])
#     backtrack(index+1)

#     # Undo
#     path.pop()

#     # Skip
#     backtrack(index+1)


# nums = [1,2,2]

# ans = []
# path = []

# backtrack(0)

# print(ans)  







# nums=[1,2,3]
# def backtrack(index):

#     if index == len(nums):  
#         ans.append(path[:])
#         return
#     for index in range(len(nums)):
    
#         path.append(nums[index])
#     backtrack(index+1)
    
#     path.pop()
#     backtrack(index+1)
# # nums = [1,2,2]

# ans = []
# path = []

# backtrack(0)

# print(ans)  

    
# ans = []
# path = []
# used = [False, False, False]    
# nums=[1,2,3]
# def backtrack(index):
#     if len(path)==len(nums):
#         ans.append(path[:])
#         return
#     for i in range(len(nums)):
#         if not used[i]:
#             used[i]=True
#             path.append(nums[i])
#             backtrack(index+1) 
#             path.pop()
#             used[i]=False
# backtrack(0)    
# print(ans)

# 1. Backtracking is about making choices

# Before today, you were trying to think:

# "How do I generate all answers?"

# Now you think:

# "What choices do I have from the current state?"

# For this problem, the choices are:

# (
# )
# 2. Not every choice is valid

# This is the first problem where you had to prune.

# Before exploring a branch, ask:

# Can I place "(" ?

# Can I place ")" ?

# If not, don't recurse.

# This is a huge backtracking concept.

# 3. State matters

# You discovered that recursion needs information about the current state.

# Here the state is:

# path
# open
# close

# Without this information, the recursive call cannot continue correctly.

# 4. Choose → Explore → Undo

# You finally wrote the classic pattern:

# path.append(...)

# backtrack(...)

# path.pop()

# This is the heart of backtracking.

# 5. The template became real

# Earlier you asked about this template:

# Base case

# Choices

# Check validity

# Choose

# Recurse

# Undo

# Today you actually filled it.

# Template	Generate Parentheses
# Base case	len(path)==2*n
# Choices	( and )
# Invalid	open==n or close>=open
# Choose	path.append()
# Recurse	backtrack(...)
# Undo	path.pop()

# This is probably the biggest thing you learned.

# 6. Not every backtracking problem needs a loop

# This is something new.

# Earlier:

# Permutations:

# for choice in choices:

# Today:

# if can_place_open:
#     ...

# if can_place_close:
#     ...

# There are still two choices, but they don't have to come from a loop.

# 7. Different problems need different state

# Compare everything you've learned so far:

# Subsets

# State:

# index
# path
# Permutations

# State:

# path
# used
# Generate Parentheses

# State:

# path
# open
# close

# This is a really important realization:

# Every backtracking problem asks, "What information do I need to describe my current state?"

# Once you know the state, the recursion becomes much easier to write.
# ans = []
# path = []
# open=0
# close=0
# def backtrack(n,open,close):
#     if len(path)==n*2:
#         ans.append(path[:])
#         return
   
#     for i in ["(",")"]:

#             if i=="(" and open<n:
#                 path.append("(")
#                 backtrack(n,open+1,close)
#                 path.pop()
         
#             if i==")":
#                 if close<n:
#                     if close<open:
#                             path.append(")") 
#                             backtrack(n,open,close+1)
#                             path.pop()
# backtrack(2,0,0)      
# print(ans)                        

                                    

        
        
# ans = []
# path = []

# def backtrack(tar, nums, summ, start):
#     if summ == tar:
#         ans.append(path[:])
#         return

#     for i in range(start, len(nums)):
#         if summ + nums[i] <= tar:

#             path.append(nums[i])

#             backtrack(tar, nums, summ + nums[i], i)

#             path.pop()

# backtrack(7, [2,3,6,7], 0, 0)
# print(ans) 
# 1. State is everything ⭐⭐⭐⭐⭐

# Before coding, ask:

# What information does the next recursive call need?

# For this problem, the state is:

# start
# remaining target (or sum)
# path

# Every backtracking problem has a different state.

# 2. The start parameter

# This is the biggest lesson.

# start means:

# "The next recursive call is only allowed to choose from this index onward."

# It serves two purposes:

# ✅ Allows reusing the current element.
# ✅ Prevents duplicate combinations like:
# 2 3
# 3 2
# 3. Think in terms of choices

# Every recursive call asks:

# "What can I choose next?"

# Not:

# "What is the whole answer?"

# That mindset shift is huge.

# 4. Choose → Recurse → Undo

# Every backtracking problem follows:

# Choose

# Recurse

# Undo

# You finally got comfortable with this pattern.

# 5. Don't plan ahead

# This was your biggest confusion.

# You kept asking:

# "How many times should I choose 2?"

# Now you know:

# The algorithm never knows.

# It simply keeps exploring until it succeeds or fails.

# 6. Parent and child calls have different state

# This is subtle but important.

# Parent:

# path = [2]

# Child:

# path = [2,2]

# Each recursive call has its own view of the problem.

# 7. Parameters describe the current world

# This is a mental model I want you to keep forever.

# Instead of thinking:

# "Parameters are inputs."

# Think:

# "Parameters describe the world that this recursive call lives in."

# For example:

# backtrack(start=1, target=4)

# means:

# "I'm in a world where I have 4 left to make, and I'm only allowed to choose from index 1 onward."

# That way of reading recursive calls makes them much easier to understand.

# 8. You don't modify everything

# Instead of doing:

# summ += nums[i]
# ...
# summ -= nums[i]

# you learned it's often cleaner to pass the updated value directly:

# backtrack(..., summ + nums[i], ...)

# This keeps the parent's state untouched.

# 9. The same template, different state

# Look at your journey:

# Problem	State
# Subsets	index, path
# Permutations	used, path
# Generate Parentheses	open, close, path
# Combination Sum	start, remaining target, path

# Notice something?

# The template never changed.

# Only the state changed.

# ⭐ The biggest lesson of all

# If there's one thing I hope you take away, it's this:

# Backtracking isn't about writing recursion. It's about identifying the right state.         

# s = "aab"
# path=[]
# ans=[]
# end=0
# def ispalin(s):
#     return s==s[::-1]
        
# def backtrack(start):
#     if start == len(s):
#         ans.append(path[:])
#         return
#     for end in range(start,len(s)):
#         piece=s[start:end+1]
#         if ispalin(piece):
#             path.append(piece)
#             backtrack(end+1)
#             path.pop()

 
# backtrack(0)
# print(ans  )   


 
# path=[]
# ans=[]
# s="25525511135"
# def backtrack(start):
#     if start == len(s):
#         if len(path) == 4:
#             ans.append(path[:])
#             return
#     for end in range(start, min(start+3,len(s))):
#         peace = s[start:end + 1]
#         if int(peace)<=255:
#             continue
        
            
#         path.append(peace)
#         backtrack(end+3)
#         path.pop()
# backtrack(0)
# print(ans)            
            
        
      


# path = []
# ans = []

# def backtrack(start, s, k):
#     if start == len(s):
#         return

#     first = s[start]

#     for i in range(len(k)):
#         path.append(first)
#         path.append(k[i])

#         ans.append("".join(path))

#         path.pop()
#         path.pop()

#     backtrack(start + 1, s, k)

# backtrack(0, "abc", "def")
# print(ans)
      
      
      
# ans=[]
# path=[]
# k=0
# def backtrack(start,target,nums,summ):
#     global k
#     nums.sort()
#     if summ==target:
#         ans.append(path[:])
#         return
#     for i in range(start,len(nums)):
#         if summ+nums[i]>target:
#             continue
#         if nums[i]!=k:
#             path.append(nums[i])
#             backtrack(i+1,target,nums,summ+nums[i])
#             k=path.pop()
# backtrack(0,4,[1,1,2,2],0)            
# print(ans)


# ans=[]
# path=[]
# def backtrack(start,nums,k,summ):
#     nums.sort()
#     cond=sum(nums)//k
#     if summ==cond:
#         ans.append(path[:])
#         return
#     for i in range(start,len(nums)):
#         if summ+nums[i]<=cond:
#             path.append(nums[i])
#             backtrack(i+1,nums,k,summ+nums[i])
#         if path:            
#             path.pop()
#             summ-=nums[i]
# backtrack(0,[1,1,2,2,3,3],3,0)
# print(ans      
            
            
#trees########################################################   ############################   ############################   ############################   ############################   ############################   ############################   ############################   ############################               


# from collections import deque
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# root = Node(1)

# root.left = Node(2)
# root.right = Node(3)

# root.left.left = Node(4)
# root.left.right = Node(5)

# root.right.left = Node(6)
# root.right.right = Node(7)

# root.left.left.left = Node(8)
# root.left.left.right = Node(9)

# root.right.left.right = Node(10)

# queue = deque([root])
# ans = []
# used=True
# while queue:

#     level = []

#     size = len(queue)

#     for _ in range(size):

#         node = queue.popleft()

#         level.append(node.val)
            
#         if node.left:
#                 queue.append(node.left)

#         if node.right:
#                 queue.append(node.right)

                
#     if used:    
#         ans.append(level)
#         used=False
#     else:
#         level.reverse()
#         ans.append(level)
#         used=True   

# print(ans)



# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# root = Node(1)

# root.left = Node(2)
# root.right = Node(2)

# root.left.left = Node(3)
# root.left.right = Node(4)

# root.right.left = Node(4)
# root.right.right = Node(3)
# def sameTree(root1, root2):

#     # 1)
#     if root1 is None and root2 is None:
#         return True

#     # 2)
#     if root1 is None or root2 is None:
#         return False

#     # 3)
#     if root1.val != root2.val:
#         return False

#     # 4)
#     left = sameTree(root1.left, root2.right)

#     # 5)
#     right = sameTree(root1.right, root2.left)

#     # 6)
#     if left == True and right == True:
#         return True

#     # 7)
#     return False
# def sym(root):
#     return sameTree(root.left,root.right)

# print(sym(root))





# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# root = Node(4)

# root.left = Node(2)
# root.right = Node(7)

# root.left.left = Node(1)
# root.left.right = Node(3)

# root.right.left = Node(6)
# root.right.right = Node(9)
# def sameTree(root1):
#     if root1 is None:
#         return 

#     root1.left, root1.right = root1.right, root1.left
    
#     sameTree(root1.left)

#     sameTree(root1.right)



from collections import deque
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# root = Node(3)

# root.left = Node(9)
# root.right = Node(20)

# root.right.left = Node(15)
# root.right.right = Node(7)
# queue = deque([root])
# ans = []
# used=True
# summ=0
# while queue:

#     level = []
#     size = len(queue)

#     for _ in range(size):

#         node = queue.popleft()

#         level.append(node.val)
#         if node.left:
#                 queue.append(node.left)

#         if node.right:
#                 queue.append(node.right)
#     for i in range(len(level)):
#         summ+=level[i]
#     total=summ/len(level)
#     ans.append(total)
#     summ=0
# print(ans)     



# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# root = Node(1)

# root.left = Node(2)
# root.right = Node(3)

# root.left.left = Node(4)
# root.right.right = Node(5)

# x = 4
# y = 5       
# from collections import deque

# queue = deque([root])

# while queue:

#     level = []
#     size = len(queue)

#     for _ in range(size):

#         node = queue.popleft()

#         level.append(node.val)

#         if node.left and node.right:

#             if node.left.val == x and node.right.val == y:
#                 print(False)
#                 exit()

#             if node.left.val == y and node.right.val == x:
#                 print(False)
#                 exit()

#         if node.left:
#             queue.append(node.left)

#         if node.right:
#             queue.append(node.right)

#     if x in level and y in level:
#         print(True)
#         break

#     if (x in level) != (y in level):
#         print(False)
#         break



# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# root = Node(10)

# root.left = Node(5)
# root.right = Node(15)

# root.left.left = Node(3)
# root.left.right = Node(7)

# root.right.left = Node(12)
# root.right.right = Node(18)

# root.left.right.left = Node(6)

# root.right.left.right = Node(13)

# root.right.right.left = Node(17)
# queue = deque([root])
# ans = []
# while queue:

#     level = []

#     size = len(queue)

#     for _ in range(size):

#         node = queue.popleft()

#         level.append(node.val)
            
#         if node.left:
#                 queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     ans.append(level[-1])                
# print(ans)                



# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.next = None


# root = Node(1)

# root.left = Node(2)
# root.right = Node(3)

# root.left.left = Node(4)
# root.left.right = Node(5)

# root.right.left = Node(6)
# root.right.right = Node(7)
# queue = deque([root])
# ans = []
# ans1=[]
# while queue:

#     level = []

#     size = len(queue)

#     for _ in range(size):

#         node = queue.popleft()

#         level.append(node.val)
#         if node.left:
#                 queue.append(node.left)
#                 ans.append(node.left.val)
#                 if node.right:
#                     root.left.next = root.right
#                     ans.append(root.left.next.val)
#                 else:
#                     ans.append("#")
#         if node.right:
#             queue.append(node.right)
    

# print(ans)



# nums = [1,5,4,2,9,9,9]
# k = 3

# left=0
# summ=0
# best=0
# freq={}

# for right in range(len(nums)):
#     summ+=nums[right]
#     freq[nums[right]] = freq.get(nums[right], 0) + 1
#     while right-left+1>k:
#         summ-=nums[left]
#         if freq[nums[right]]>1:
#                 freq[nums[left]] -= 1

#         if freq[nums[left]] == 0:
#             del freq[nums[left]]

#         left += 1
        
#     best=max(best,summ)
# print(best)    


# target = 7
# nums = [2,3,1,2,4,7]
# left=0
# summ=0
# best = float('inf')
# for right in range(len(nums)):
#     summ+=nums[right]
#     while summ>=target:
#         best=min(best,right-left+1)
#         summ-=nums[left]
#         left+=1
# print(best)
# nums=[1,1,1]
# curr=0
# freq={0:1}
# count=0
# k=2
# for i in range(len(nums)):
#     curr+=nums[i]
#     now=curr-k
#     if now in freq:
#         count+=freq[now]
#     freq[curr]=freq.get(curr,0)+1
# print(count)    
# print(freq)

# nums = [1, -1, 5, -2, 3]
# k = 3

# summ = 0
# best = 0
# freq = {0: -1}

# for i in range(len(nums)):
#     summ += nums[i]
#     now = summ - k

#     if now in freq:
#         best = max(best, i - freq[now])

#     if summ not in freq:
#         freq[summ] = i

# print(best)   


# nums = [4,5,0,-2,-3,1]
# k = 5
# pre=0
# freq={0:1}
# best=0
# count=0
# for i in range(len(nums)):
#     pre+=nums[i]
#     rem=pre%k
#     if rem in freq:
#         count+=freq[rem]
#     freq[rem]=freq.get(rem,0)+1    
# print(count)    



# nums = [23,2,4,6,7]
# k = 6
# pre=0
# freq={0:1}
# best=0
# count=0
# for i in range(len(nums)):
#     pre+=nums[i]
#     rem=pre%k
#     if rem in freq:
#         if i-freq[rem]>=2:
#             print(True)
#             break
#     freq[rem]=i   



# nums = [6,7,8,1,2,3,4,5]
# target = 8
# nums = [6,7,8,1,2,3,4,5]
# target = 3
# left=0
# right=len(nums)-1
# while left<=right:
#     mid=left+(right-left)//2
    
#     if nums[mid] == target:
#         print(mid)
#         break

#     elif nums[mid]<nums[right]:
#         if nums[mid]<target<=nums[right]:
#             left=mid+1
#         else:
#             right=mid-1

    
#     elif nums[left]>nums[mid]:
#         if nums[left]<=target<nums[mid]:
#             right=mid-1
#         else:
#             left=mid+1



# nums = [1,2]
# left=0
# right=len(nums)-1
# while left<right:
#     mid=left+(right-left)//2
  
#     if nums[mid-1]<nums[mid]>nums[mid+1]:
#         print(mid)
#         break
#     if nums[mid]<nums[mid+1]:
#         left=mid+1
#     else:
#         right=mid
        
        
# nums=[1,1,1,2,2,3,3]
# i=0
# j=i+1
# while j<len(nums):
#     if nums[i]==nums[j]:
#         j+=1
#     else:
#         nums[i+1],nums[j]=nums[j],nums[i+1]
#         i+=1
#         j+=1
# print(nums)
    
# a = [-1, 0, 1, 2, -1, -4]
# a.sort()
# i=0
# result=[]
# n=len(a)
# for i in range(n - 2):

#     if i > 0 and a[i] == a[i - 1]:
#         continue

#     left = i + 1
#     right = n - 1
#     sum = -1 * a[i]

#     while left < right:
#         s = a[left] + a[right]

#         if s == sum:
#             result.append([a[i], a[left], a[right]])

#             left += 1
#             right -= 1

#             while left < n and a[left] == a[left - 1]:
#                 left += 1

#             while right > 0 and a[right] == a[right + 1]:
#                 right -= 1

#         elif s < sum:
#             left += 1
#         else:
#             right -= 1
# print(result)
# print(a)

  
  
    
# a = [-1, 0, 1, 2, -1, -4]
# a.sort()
# i=0
# result=[]
# n=len(a)
# for i in range(n - 2):
#     if i>0 and a[i]==a[i-1]:
#         continue
#     left=i+1
#     right=n-1
#     sum=-1*a[i]
    
#     while left<right:
#         s=a[left]+a[right ]
#         if s==sum:
#             result.append([a[i],a[left],a[right ]])
#             left+=1
#             right-=1
#             while (left<n and a[left ]==a[left - 1]):
#                 left+=1
#             while (right>0 and a[right ]==a[right - 1]):
            
#                 right+=1                      
#         elif s<sum:
#             left+=1
#         else:
#             right-=1  
# print(result)            



    
# a = [-1, 0, 1, 2, -1, -4]
# a.sort()
# i=0
# result=[]
# n=len(a)
# for i in range(n - 2):

#     if i > 0 and a[i] == a[i - 1]:
#         continue

#     left = i + 1
#     right = n - 1
#     sum = -1 * a[i]

#     while left < right:
#         s = a[left] + a[right]

#         if s == sum:
#             result.append([a[i], a[left], a[right]])

#             left += 1
#             right -= 1

#             while left < n and a[left] == a[left - 1]:
#                 left += 1

#             while right > 0 and a[right] == a[right + 1]:
#                 right -= 1

#         elif s < sum:
#             left += 1
#         else:
#             right -= 1
# print(result)
# print(a)


# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()

#         result_sum = nums[0] + nums[1] + nums[2]
#         max_diff = abs(result_sum - target)

#         for i in range(len(nums) - 2):

#             left = i + 1
#             right = len(nums) - 1

#             while left < right:

#                 sum = nums[i] + nums[left] + nums[right]

#                 diff = abs(sum - target)

#                 if diff < max_diff:
#                     max_diff = diff
#                     result_sum = sum

#                 if sum < target:
#                     left += 1

#                 elif sum > target:
#                     right -= 1

#                 else:
#                     return sum

#         return result_sum
    

# a = [-4, -1, 2, 5]
# target = 3
# a.sort()
# i=0
# n=len(a)
# res=a[0]+a[1]+a[2]
# max_diff=abs(target-res)
# for i in range(n - 2):
#     left = i + 1
#     right = n - 1
    

#     while left < right:
#         s = a[i]+a[left] + a[right]    
#         diff=abs(target-s)
#         if diff<max_diff:
#             max_diff=diff
#             res=s
            
#         if s<target:
#             left+=1
#         else:
#             right-=1
# print(res)
        


# a = [-3, -1, 0, 2, 4]
# target = 2
# count=0
# n=len(a)

    
# for i in range(n-2):
#     left=i+1
#     right=n-1
    
#     while left<right:
#         sum=a[i]+a[left]+a[right]
#         print(a[i],a[left],a[right])
#         if sum<target:
#             count+=right-left
#             left+=1


#         else:
#             right-=1
        
# print(count)
# # [-3, -1, 4] → 0 < 2
# # [-3,  0,  2] → -1 < 2
# # [-3,  0,  4] → 1 < 2
# # [-1,  0,  2] → 1 < 2



# a = [1, 2, 3, 4, 5, 7, 8]
# limit = 5
# n=len(a)
# count=0
# for i in range(n-2):
#     left=i+1
#     right=n-1
    
#     while left < right:
#         if a[right]-a[left]<limit:
#             print(a[i],a[left],a[right])
#             count+=right-left
#             left+=1
#         else:
#             right-=1
# print(count)            
        
        
        
# ##########BACKTRACKING REVISION####################################################################################################################################################   
# nums = [1, 2, 3]
# res=[]
# path=[]
# def backtrack(nums,start):
#     res.append(path[:])
#     for i in range(start,len(nums)):
#         path.append(nums[i])
#         backtrack(nums,i+1)
#         path.pop()
# backtrack([1,2,3],0)
# print(res)        
# nums = [1, 2, 3]

# res = []
# path = []
  


    



# nums = [1, 2, 3, 4]
# k = 2
# path=[]
# res=[]
# def backtrack(nums,start):
#     if len(path)==2:
#         res.append(path[:])
#         return
        
    
#     for i in range(start,len(nums)):
#         path.append(nums[i])
#         backtrack(nums,i+1)
#         path.pop()
# backtrack(nums,0)
# print(res)          

# s="aab"

# path=[]
# res=[]
# def backtrack(nums,start):
#     if start == len(s):
#         res.append(path[:])
#         return
#     for end in range(start,len(nums)):
#         part=s[start:end+1]
#         if part==part[::-1]:
            
#             path.append(part)
#             backtrack(nums,end+1)
#             path.pop()
# backtrack(s,0)   
# print(res)     


# nums=[1,2,3]
# res=[]
# path=[]
# used = [False] * len(nums)
# def backtrack(nums):
#     if len(path)==len(nums):
#         res.append(path[:])
#         return
#     for i in range(len(nums)):
#         if not used[i]:
            
#             path.append(nums[i])
#             used[i]=True
#             backtrack(nums)
#             path.pop()
#             used[i]=False
# backtrack(nums)
# print(res)
        
        
# nums=[0,1,2,0,1,2]
# i=0
# mid=0
# j=len(nums)-1
# while mid<=j:
#     if nums[mid]==1:
#         mid+=1
#     elif nums[mid]==0:
#         nums[mid],nums[i]=nums[i],nums[mid]
#         mid+=1
#         i+=1
#     else:
#         nums[mid],nums[j]=nums[j],nums[mid]
#         j-=1
# print(nums)          


#trees###########################################################################################################################################################
# from collections import deque

# from collections import deque

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# # Create tree
# root = Node(3)

# root.left = Node(9)
# root.right = Node(20)

# root.right.left = Node(15)
# root.right.right = Node(7)


# # Level Order Traversal
# queue = deque([root])
# res=[]
# while queue:
#     level=[]
    
#     for _ in range(len(queue)):
#         node=queue.popleft()
#         level.append(node.val)
        
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     res.append(level)
# print(res)



# from collections import deque

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# # Create tree
# root = Node(3)

# root.left = Node(9)
# root.right = Node(20)

# root.right.left = Node(15)
# root.right.right = Node(7)


# # Level Order Traversal
# queue = deque([root])
# res=[]
# while queue:
#     level=[]
    
#     for _ in range(len(queue)):
#         node=queue.popleft()
#         level.append(node.val)
        
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     a=sum(level)/len(level)
#     res.append(a)
# print(res)

from collections import deque

# from collections import deque

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.next = None


# root = Node(1)

# root.left = Node(2)
# root.right = Node(3)

# root.left.left = Node(4)
# root.left.right = Node(5)

# root.right.left = Node(6)
# root.right.right = Node(7)



# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.next = None
# queue=deque([root])

# while queue :
#     level=[]
#     prev=None
#     for i in range(len(queue)):
#         node = queue.popleft()
#         if prev:
#             prev.next=Node
#         prev=Node
        
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
            
            
            
            
        
# from collections import deque

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# # Create tree
# root = Node(3)

# root.left = Node(9)
# root.right = Node(20)

# root.right.left = Node(15)
# root.right.right = Node(7)


# # Level Order Traversal
# queue = deque([root])
# res=[]
# while queue:
#     level=[]
    
#     for _ in range(len(queue)):
#         node=queue.popleft()
#         level.append(node.val)
        
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#     res.append(level)
# res.reverse()
# print(res)    




# from collections import deque

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# # Create tree
# root = Node(10)

# root.left = Node(6)
# root.right = Node(15)

# root.left.left = Node(2)
# root.left.right = Node(8)

# root.right.right = Node(20)


# # Level Order Traversal
# queue = deque([root])
# res=[]
# best=0
# while queue:
#     level=[]
    
#     for _ in range(len(queue)):
#         node=queue.popleft()
        
        
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
            
#         best=max(best,node.val)
#     res.append(best)    
#     best=0
        
# print(res)    


# from collections import deque

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# root = Node(1)

# root.left = Node(2)
# root.right = Node(3)

# root.left.right = Node(5)
# root.right.right = Node(4)

# # Level Order Traversal
# queue = deque([root])
# res=[root.val]
# best=0
# while queue:
#     level=[]
    
#     for i in range(len(queue)):
#         node=queue.popleft()

#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#         if i==len(queue)-1:
#             res.append(node.val)


# print(res)    



# from collections import deque

# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None


# root = Node(1)

# root.left = Node(2)
# root.right = Node(3)

# root.left.right = Node(5)
# root.right.right = Node(4)

# # Level Order Traversal
# queue = deque([root])
# res=[root.val]
# best=0
# while queue:
#     level=[]
    
#     for i in range(len(queue)):
#         node=queue.popleft()

#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)
#         if i==len(queue)-1:
#             res.append(node.val)
# print(res)    
#######################stack###################################################################################################################################stack############################################################################################################

# nums = [2, 1, 5, 3, 4]
# stack=[]
# res=[-1]*len(nums)
# for i in range(len(nums)):
#     while stack and nums[i]>nums[stack[-1]]:
#         j=stack.pop()
#         res[j]=nums[i]
        
#     stack.append(i)
# print(res)



# nums = [2, 1, 5, 3, 4]
# stack=[]
# res=[-1]*len(nums)
# for i in range(len(nums)):
#     while stack and nums[i]>nums[stack[-1]]:
#         j=stack.pop()
#         res[j] =nums[i]

#     stack.append(i)
# print(res)



nums = [73, 74, 75, 71, 69, 72, 76, 73]
stack=[]
res=[0]*len(nums)

for i in range(len(nums)):
    while stack and nums[i]>nums[stack[-1]]:
        res[stack[-1]]=i-stack[-1]
        stack.pop()
    stack.append(i)
print(res)    
        
        
        