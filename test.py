finalcount = 0
count = 0

def fizz_count(x):
  count = 0
  for item in x:
    if item == "fizz":
      count = count + 1
      print(str(count) + "this is in the loop")
      
      
    
     

fizzlist = ["fizz", "fizz", "fizz", "dog"]

fizz_count(fizzlist)

print(str(count) + "this is called outside the loop")

