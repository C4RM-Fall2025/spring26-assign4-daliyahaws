def FizzBuzz(start, finish):
    outlist = []
    
    for i in range(start, finish + 1):
        if i % 3 == 0 and i % 5 == 0:
            outlist.append("FizzBuzz")
        elif i % 3 == 0:
            outlist.append("Fizz")
        elif i % 5 == 0:
            outlist.append("Buzz")
        else:
            outlist.append(i)
    
    return outlist


print(FizzBuzz(1, 15))
