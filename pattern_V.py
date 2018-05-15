import time
import sys

# 	0123456

# 0	*      *
# 1	 * 	  *
# 2	  *  *
# 3    *   
# 4	     
# 5	    
# 6     



for row in range(7):
	for col in range(7):
		if ((col==row and (col<4 and row<4))):
			print '*',

		elif (col==6-row and(row<3)):
			print '*',
		# 	time.sleep(0.1)
		else:
			print ' ',

	print ''
	time.sleep(0.1)