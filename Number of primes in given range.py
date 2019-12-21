def main():
    count = 0
    k=0
    print("Enter the range to find the primes in between the range:")
    number1 = int(input("Enter number1:"))
    number2 = int(input("Enter number2:"))
    if(number1>number2):
        max = number1
        min = number2
    else:
        max = number2
        min = number1
    for i in range(min,max+1):
        count = 0
        for j in range(1,i+1):
            if(i%j==0):
                count = count + 1
        if(count==2):
            k = k + 1
    print("The number of primes between {} and {} are : {}".format(number1,number2,k))
main()
