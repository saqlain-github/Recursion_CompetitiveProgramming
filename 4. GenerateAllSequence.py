def generateAllSubsequence(array,n):
    subSeqArray = []
    solve(0,array,n ,subSeqArray) 
  
  
# O(2^n)    
def solve(index,array,n, subSeqArray):
    #base condition
    #doing out of bound
    if index >= n: 
        print(subSeqArray)
        return #back tracking
    
    #i have 2 option 
    # 1 pick the current element : array[index]
    subSeqArray.append(array[index])
    #recursively call for the next index of the array
    solve(index+1, array,n , subSeqArray)
    # when i come back from above function call
    #consider not to pick the current element
    subSeqArray.pop()
    #recursively call for the next index
    solve(index+1, array, n, subSeqArray)
    
if __name__ == '__main__':
    A = [1,2,3]
    generateAllSubsequence(A,len(A))