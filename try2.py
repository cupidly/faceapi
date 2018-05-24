count = 0
fizzlist = ["fizz", "fizz", "dog", "fizz", "fizz", "cast"]

def fizzcount(x):
    count = 0
    for item in fizzlist:
        if item == "fizz":
            count = count + 1
            print(count)
    return count



finalcount = fizzcount(fizzlist)


## then do print(finalcount) to get the final count
