import time
import sys

# 	012345
# 0	 ****
# 1	*	 *
# 2	******
# 3	*	 *
# 4	*	 *
# 5 *    *

# 6x6 matrix

for row in range(7):

	for col in range(7):

		if (row==0 or row==3) and (col>0 and col<4):
			print '*',
		elif (col ==0 or col==4) and row !=0:
			print '*',
		else:
			print ' ',

	print ""
	time.sleep(0.1)	