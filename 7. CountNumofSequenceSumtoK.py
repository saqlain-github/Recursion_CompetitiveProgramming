def generateAllSubsequenceSumK(array,n,k):
    idx = 0
    s = [0]
    print(solve(array,n ,idx,s,k))
  
  
# O(2^n)   
'''
#global variable and once = 0
once = 0 
option1 
'''
def solve(array,n, idx,s,k):
    #base condition
    #doing out of bound
    
    if idx == n:
        if s[0] == k:
            return 1
        return 0 #back tracking
    
    #i have 2 option 
    # 1 pick the current element : array[index]
    #subSeqArray.append(array[idx])
    s[0] += array[idx]
    #recursively call for the next index of the array
    firstCall = solve(array,n , idx+1,s,k)
    # when i come back from above function call
    #consider not to pick the current element
    #subSeqArray.pop()
    s[0] -= array[idx]
    #recursively call for the next index
    secondCall = solve(array, n, idx+1,s,k)
    return firstCall+secondCall
    
if __name__ == '__main__':
    A = [3,8,5]
    generateAllSubsequenceSumK(A,len(A),8)