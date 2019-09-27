import time
import sys
		
	# 	012345
	# 0	*******
	# 1	   *
	# 2	   *
	# 3    	   *
	# 4	   *
	# 5	   *
	# 6     *******

for row in range(7):
	for col in range(6):
		if col==3:
			print '*',
		elif(row==0 or row==6) and (col>0 and col !=3):
			print '*',		
		else:
			print ' ',
	print ''			
	time.sleep(0.1)
	
a=[[1,2,3,4,5],
[1,2,3,4,5],
[1,2,3,4,5],
[1,2,3,4,5],
[1,2,3,4,5]
]

n=int(len(a)/2)


for i in range(len(a)):
    
    for j in range(len(a[0])):

        if (i==0 or i==len(a)-1) and j !=n:
            print("*",end=" ")
        elif(j==n):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")     
