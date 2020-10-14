#getting user input

num = int(input("Enter the number:"))

#checking whether the num is prime or not

if num > 1 :
     for i in range(2,num):
          if(num % i) == 0:
                print("{0} is not a prime number".format(num))
                break
          else:
                print("{0} is a prime number".format(num))
                break
else:
     print("{0} is not a prime number".format(num))


