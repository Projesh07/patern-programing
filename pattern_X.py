import time
import sys


# 	0123456

# 0	 * 	      *
# 1	  *     *
# 2     * *
# 3	    * *  
# 4	  *     *
# 5 *         *

for row in range(7):
	for col in range(7):
		if (col==row or col==6-row):
			print '*',
		else:
			print ' ',

	print ''
	time.sleep(0.1)