import time
import sys



	# 	0123456
	# 0	******** 
	# 1	   *	  
	# 2	   *     
	# 3   	   *
	# 4	   *  
	# 5	   *  
	# 6        *    


for row in range(7):
	for col in range(7):
		if ((col==3 and row>0)):
			print '*',

		elif (row==0 ):
			print '*',
		
		else:
			print ' ',

	print ''
	time.sleep(0.1)
