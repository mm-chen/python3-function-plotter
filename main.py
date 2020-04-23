#!/usr/bin/python3
import math;
import sys;

startX=-11.0
stopX=11.0
interX=0.1
startY=-11.0
stopY=11.0
interY=0.1

marks=1.0

x=startX
y=startY
while y<stopY:
	while x<=stopX:
		if  ((interX/2>x>-interX/2) and (interY/2>y>-interY/2)):
			sys.stdout.write("0");
		elif((interX/2>abs(x)%marks>-interX/2 or interX/2>marks-abs(x)%marks>-interX/2) and (interY/2>abs(y)%marks>-interY/2 or interY/2>marks-abs(y)%marks>-interY/2)):
			sys.stdout.write("+");
		elif(interX/2>abs(x)%marks>-interX/2 or interX/2>marks-abs(x)%marks>-interX/2):
			sys.stdout.write("|");
		elif(interY/2>abs(y)%marks>-interY/2 or interY/2>marks-abs(y)%marks>-interY/2):
			sys.stdout.write("-",);
		elif((math.sqrt(abs(x)) + y)>0):
			sys.stdout.write("\033[31m#\033[0m");
		elif(((x*x) + y)>0):
			sys.stdout.write("\033[32mo\033[0m");
		else:
			sys.stdout.write(" ");
		x+=interX
	y+=interY
	x=startX
	sys.stdout.write("\n");

quit(0);
