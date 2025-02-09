num = int(input("Enter a number"))
cpy = num
s=0
while num != 0:
  k = num%10
  s = s+(k**3)
  num = num//10#integer division
if cpy == s:
  print("Armstrong")
else:
  print("Not an Armstrong")
