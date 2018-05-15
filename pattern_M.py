import time
import sys
		



# 	012345
# 0	*    *
# 1	**	**
# 2	* ** *
# 3 * *  *
# 4	*	 *
# 5	*	 *
# 6 *    *


for row in range(7):
	for col in range(7):
		if (col==0 or col==6):
			print '*',
		# elif(((row==col) and (col>0 and col<2 ) and row>0)):
		# 	print '*',		
		elif(((row==col) and (col>0 and col<4)) or ((row==1 and col==5) or (row==2 and col==4))):
			print '*',			
		else:
			print ' ',
	print ''	
	time.sleep(0.1)