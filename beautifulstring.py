""""
A string is beautiful if it has equal number of a,b,and c in it.
Example "abc" , "aabbcc" , "dabc" , "" are beautiful.
Given a string of alphabets containing only lowercase alphabets (a-z), output the number of non-empty beautiful sub string of the given string.

Input
The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows. Each test case consists of a line containing a string a length L.

Output
For each test case, output a single line containing the number of beautiful sub string.
Sample Input
1
abacbcba

Sample Output
5
 ("abacbc","bac",”acb”, ”acbcba”,"cba")
"""

str = input("string: ") 
n = len(str); 
#For holding all the formed substrings  
arr = []

#To store all unique characters
unique = []

for i in str:
    unique.append(i)
unique = list(set(unique))
n_unique = len(unique)
#This loop maintains the starting character  
for i in range(0,n):  
    #This loop will add a character to start character one by one till the end is reached  
    for j in range(i,n):  
        arr.append(str[i:(j+1)])  
solution = []
solution = set(solution)

#Prints all the subset  
for i in range(len(arr)):
    count=0
    temp = []
    for k in arr[i]:     #str = abb  temp=['a','b','b'] unique = ['a','b','c'] count = 3
        temp.append(k)
    #print(temp)
    for j in unique:
        for k in temp:
            if j==k:
                count+=1
    #print(count)
    
    '''
    # all() function
    
    check =  all(item in temp for item in unique)
    if check is True:
        if count%n_unique == 0:
            solution.append(arr[i])
    '''
    
    '''
    orignal idea but issue is print wrong value as well
    
    if count%n_unique == 0:
        solution.append(arr[i])
    ''' 
    
    # big brain logic
    l_count=0
    check =  all(item in temp for item in unique)  # check if all char in unique are present in temp
    if check is True:
        if count%n_unique == 0:
            if count == n_unique:
                solution.add(arr[i])
            else:
                for j in unique:
                    if temp.count(j)==2: # aabbcc  l_count = 3 # bacbcb l_count = 1
                        l_count+=1
                if l_count==n_unique:
                    solution.add(arr[i])
            
    
        
print(solution)
print(len(solution))
#print(arr)