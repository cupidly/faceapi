finalcount = 0
count = 0


def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
  return count
      
    
     

fizzlist = ["fizz", "fizz", "fizz", "dog"]

fizz_count(fizzlist)

print(count)

print(len(fizzlist))


print(fizzlist.count("fizz"))
