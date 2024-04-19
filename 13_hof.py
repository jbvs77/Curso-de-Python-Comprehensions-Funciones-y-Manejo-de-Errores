sum = lambda n: n+1
sum2 = lambda n,m: n+m(n)

print(sum2(5,sum))

'''Here is the code demonstrating a higher-order function in Python that takes a function as a parameter and returns a function'''