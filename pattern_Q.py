import time
import sys



# 	0123456
# 0	 ***** 
# 1	*	  *
# 2	*     *
# 3 *     *
# 4	**	  *
# 5	 *****
# 6      *

for row in range(7):
	for col in range(7):
		if ((col==0  or col==6) and (row>0 and row<5)):
			print '*',
		elif ((row==0 or row==5) and (col>0 and col<6)) or(col==5 and row==6) or (col==1 and row==4):
			print '*',
		else:
			print ' ',

	print ''
	time.sleep(0.1)