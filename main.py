#!/usr/bin/python3
import math;

x=-10
c=-1.25
while c<1.25:
	while x<=10:
		if(x==0 and c==0):
			print("0",end="");
		elif (x%10==0 or c%10==0):
			print("+",end="");
		elif(x==0):
			print("|",end="");
		elif(c==0):
			print("-",end="");
		elif(((math.sin(0.5*x) + c)/2+(math.sin(2*x) + c)/2)>0):
			print("#",end="");
		#elif((math.sin(2*x) + c)>0):
		#	print("o",end="");
		else:
			print("-",end="");
		#print ("x =", x, "\n\t\t y =", int(f(x)));
		x+=0.125
	c+=0.0625
	x=-10
	print();

quit(0);
