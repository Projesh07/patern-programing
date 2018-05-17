import time
import sys

	# 	012345
	# 0	 *****
	# 1	*	 
	# 2	*	 
	# 3	*
	# 4	*	 
	# 5	*	 
	# 6	 ******

for row in range(7):
	for col in range(7):
		if (col==0) or ((row==0 or row==6) and (col>0 and col<5)):
			print '*',
		else:
			print ' ',

	print ''
	time.sleep(0.1)	
