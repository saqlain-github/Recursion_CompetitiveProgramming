def generateAllSubsequenceSumK(array,n,k):
    subSeqArray = []
    s = 0
    solve(0,array,n ,subSeqArray,s,k) 
  
  
# O(2^n)    
def solve(index,array,n, subSeqArray,s,k):
    #base condition
    #doing out of bound
    
    if index >= n:
        if s == k:
            print(subSeqArray)
        return #back tracking
    
    #i have 2 option 
    # 1 pick the current element : array[index]
    subSeqArray.append(array[index])
    s = s+ array[index]
    #recursively call for the next index of the array
    solve(index+1, array,n , subSeqArray,s,k)
    # when i come back from above function call
    #consider not to pick the current element
    subSeqArray.pop()
    s = s-array[index]
    #recursively call for the next index
    solve(index+1, array, n, subSeqArray,s,k)
    
if __name__ == '__main__':
    A = [3,8,5]
    generateAllSubsequenceSumK(A,len(A),8)