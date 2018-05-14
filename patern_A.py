


# 	012345
# 0	 ****
# 1	*	 *
# 2	******
# 3	*	 *
# 4	*	 *
# 5 *    *

# 6x6 matrix

for row in range(7):

	for col in range(6):

		if (row==0 or row==3) and (col>0 and col<4):
			print '*',
		elif (col ==0 or col==4) and row !=0:
			print '*',
		else:
			print ' ',

	print ""		

					



# 	012345
# 0	*****
# 1	*	 *
# 2	*	 *
# 3	*****
# 4	*	 *
# 5	*	 *
# 6 *****

for row in range(7):
	for col in range(6):
		if ((col==0) or(col==4 and(row !=0 and row !=3 and row !=6))):
			print '*',

		elif((row==0 or row==3 or row==6) and (col>0 and col<4)):
			print '*',
		else:
			print ' ',
	print ""			


# 	012345
# 0	*****
# 1	*	 
# 2	*	 
# 3	*
# 4	*	 
# 5	*	 
# 6 *****

for row in range(7):
	for col in range(6):
		if (col==0) or ((row==0 or row==6) and (col>0 and col<5)):
			print '*',
		else:
			print ' ',

	print ''		  	


# 	012345
# 0	*****
# 1	*	 *
# 2	*	 *
# 3	*	 *	
# 4	*	 *
# 5	*	 *
# 6 *****


for row in range(7):
	for col in range(6):
		if (col==0) or ((col==4) and (row !=0 and row !=6)):
			print '*',
		elif (((row==0 or row ==6)) and (col>0 and col<4)):
			print '*',
		else:
			print ' ',

	print ''		

# 	012345
# 0	******
# 1	*	 
# 2	*	 
# 3	****** 	
# 4	*	 
# 5	*	 
# 6 ******


for row in range(7):
	for col in range(6):
		if (col==0):
			print '*',
		elif ((row==0 or row ==6 or row==3)) and (col>0 and col<5):
			print '*',
		else:
			print ' ',

	print ''


# 	012345
# 0	******
# 1	*	 
# 2	*	 
# 3	****** 	
# 4	*	 
# 5	*	 
# 6 *


for row in range(7):
	for col in range(6):
		if (col==0):
			print '*',
		elif ((row==0 or row==3)) and (col>0 and col<5):
			print '*',
		else:
			print ' ',

	print ''

# 	012345
# 0	******
# 1	*	 
# 2	*	 
# 3	*	***	
# 4	*	 *
# 5	*	 *
# 6 ******

for row in range(7):
	for col in range(6):
		if (col==0 or (col==4) and row>2):
			print '*',
		elif (((row==0 or row==6)and (col>0 and col<5)) or ((row==3)and(col==3 or col==5))):
			print '*',
		else:
			print ' ',

	print ''

# 	012345
# 0	*    *
# 1	*	 *
# 2	*	 *
# 3 ******
# 4	*	 *
# 5	*	 *
# 6 *    *

for row in range(7):
	for col in range(6):
		if (col==0 or col==4):
			print '*',
		elif (row==3 and(col>0 and col<4)):
			print '*',
		else:
			print ' ',

	print ''



# for row in range(7):

# 	for col in range(6):

# 		if (row==0 or row==3) and (col>0 and col<4):
# 			print '*',
# 		elif (col ==0 or col==4) and row !=0:
# 			print '*',
# 		else:
# 			print ' ',

# 	for col in range(6):
# 		if (col==1) or(col==4 and(row !=0 and row !=3 and row !=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
# 			print '*',
# 		else:
# 			print ' ',

# 	for col in range(6):
# 		if (col==0) or (row==0 or row==6):
# 			print '*',
# 		else:
# 			print ' ',
	# for col in range(6):
	# 	if (col==0) or ((col==4) and (row !=0 and row !=6)):
	# 		print '*',
	# 	elif ((row==0 or row ==6)) and (col>0 and col<4):
	# 		print '*',
	# 	else:
	# 		print ' ',

		# for col in range(6):
		# if (col==0):
		# 	print '*',
		# elif ((row==0 or row ==6 or row==3)) and (col!=0):
		# 	print '*',
		# else:
		# 	print ' ',
	# for col in range(6):
	# 	if (col==0):
	# 		print '*',
	# 	elif ((row==0 or row==3)) and (col>0 and col<5):
	# 		print '*',
	# 	else:
	# 		print ' ',


	# for col in range(6):
	# 	if (col==0 or (col==4) and row>2):
	# 		print '*',
	# 	elif (((row==0 or row==6)and (col>0 and col<5)) or ((row==3)and(col==3 or col==5))):
	# 		print '*',
	# 	else:
	# 		print ' ',
	# for col in range(6):
	# 	if (col==0 or col==4):
	# 		print '*',
	# 	elif (row==3 and(col>0 and col<4)):
	# 		print '*',
	# 	else:
	# 		print ' ',
	# print ""			



#THis is O

# for row in range(7):
# 	for col in range(6):
# 		if (col==0 or col==4):
# 			print '*',
# 		elif ((row==0 or row==6)) and (col>0 and col<5):
# 			print '*',
# 		else:
# 			print ' ',

# 	print ''
