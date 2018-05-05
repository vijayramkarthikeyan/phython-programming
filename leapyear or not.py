
vr = int(input("Enter the value:"))
if (vr % 4) == 0:
   if (vr % 100) == 0:
       if (vr % 400) == 0:
           print "yes"
       else:
        print "No"
   else:
    print "yes"
else:
  print "No"
