sum = 0
num = int(input())
if num >=1 and num < 10:
  v = 1
if num >=10 and num <100:
  v = 2
if num >= 100 and num < 1000:
  v = 3
if num >= 1000 and num < 10000:
  v = 4
if num >= 10000 and num < 100000:
  v = 5
if num >= 100000 and num < 1000000:
  v = 6

tem = num
while tem > 0:
   digit = tem % 10
   sum += digit ** v
   tem //= 10

if num == sum:
   print "yes"
else:
   print "No"
