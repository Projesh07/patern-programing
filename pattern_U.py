import time
import sys


# 	0123456

# 0	*      *
# 1	*      *
# 2	*      *
# 3     *      *
# 4	*      *
# 5	*      *
# 6      ***** 


for row in range(7):
	for col in range(7):
		if ((col==0 or col==6) and(row<6)):
			print '*',

		elif (row==6 and(col>0 and col<6)):
			print '*',
			
		else:
			print ' ',

	print ''
	time.sleep(0.1)
