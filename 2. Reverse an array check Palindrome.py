def reverse(A,start, end):
    if start >= end: return 
    A[start], A[end] = A[end], A[start]
    return reverse(A,start+1,end-1)
    
def reveresOneParam(A,i):
    if i >= len(A)//2:
        return 
    A[i], A[len(A)-i-1] = A[len(A)-i-1], A[i]
    return reveresOneParam(A,i+1)
       
def palindrome(s,i):
    if i >= len(s)//2:
        return True
    if s[i] == s[len(s)-i-1]:
        return palindrome(s,i+1)
    return False



if __name__ == '__main__':
    A = [1,2,3,4]
    reverse(A,0,len(A)-1)
    print(A)
    reveresOneParam(A,0)
    print(A)
    print(palindrome("abbba",0))
