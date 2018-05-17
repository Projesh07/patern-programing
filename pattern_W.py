import time
import sys


	# 	0123456

	# 0	*          *
	# 1	*          *
	# 2	*          *
	# 3     *          *
	# 4	*     *    *  
	# 5	*   *   *
	# 6     *          *

for row in range(7):
	for col in range(7):
		if (col==0 or col==6):
			print '*',

		elif ((row>3 and (col==row and col<6)) or (row>2 and (col==6-row and (col<4 and col>0)))):
			print '*',
		# 	time.sleep(0.1)
		else:
			print ' ',

	print ''
	time.sleep(0.1)
