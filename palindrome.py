num  = int(input("Enter the number: "))
v = num
rev = 0
while(num > 0):
  
  Rem = num %10
  rev = (rev*10) + Rem
  num = num // 10
c = int(rev)
if c == v:
  print "yes"
  
else:
  print "no"
