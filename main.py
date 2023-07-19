def palindrome(string,left,right):
    if(left==right):
        return 1
    if (string[left]!=string[right]):
        return 0
    return palindrome(string,left+1,right-1)
string=input()
left=0
right=len(string)-1
print(palindrome(string,left,right))