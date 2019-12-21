def main():
    count = 0
    number = int(input("Enter a number to check whether the number is prime or not:"))
    for i in range(1,number+1):
        if(number%i==0):
            count=count+1
    if(count==2):
        print("{} is a prime number ".format(number))
    else:
        print("{} is not a prime number".format(number))
main()
