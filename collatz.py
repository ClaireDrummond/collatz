
# The number we will perform the collatz on
n = 20

# Keep looping until we reach 1
while n != 1:
    #Print the current value of n
    print(n)
    # Check if n is even
    if n % 2 == 0:
    # if n is even divide it by 2
        n = n / 2
    else:
        #if n is odd, multiply by 3 and add 1
        n = (3 * n) + 1

print (n)
