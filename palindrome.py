def ispalindrome(s):
    
    if s == s[::-1]:
        print(s,"is a palindrome")
    else:
         print(s,"is not a palindrome")


s = (input("Enter the string: "))
ispalindrome(s)
    
    
        
