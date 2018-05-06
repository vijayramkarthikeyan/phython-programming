vr = int(input())

if vr > 1:
   
   for i in range(2, num):
       if (vr % i) == 0:
           print "no"
           break
   else:
       print "yes"
