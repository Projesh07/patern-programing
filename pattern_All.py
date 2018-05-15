
# https://gist.github.com/Y4suyuki/6805818

import time
import sys


#----------------------All together "---------------------
letter_per_row=0
for row in range(7):
	for col in range(6):
		if (row==0 or row==3) and (col>0 and col<4):
			print '*',
		elif (col ==0 or col==4) and row !=0:
			print '*',
		else:
			print ' ',

	letter_per_row=+1
			
	for col in range(6):
		if (col==1) or(col==4 and(row !=0 and row !=3 and row !=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
			print '*',
		else:
			print ' ',

	letter_per_row=+1		
	for col in range(5):
		if (col==0) or (row==0 or row==6):
			print '*',
		else:
			print ' ',

	letter_per_row=+1
			
	for col in range(6):
		if (col==0) or ((col==4) and (row !=0 and row !=6)):
			print '*',
		elif ((row==0 or row ==6)) and (col>0 and col<4):
			print '*',
		else:
			print ' ',

	# letter_per_row=+1
	# if letter_per_row>3:		
	for col in range(6):
		if (col==0):
			print '*',
		elif ((row==0 or row ==6 or row==3)) and (col!=0):
			print '*',
		else:
			print ' ',

	for col in range(6):
		if (col==0):
			print '*',
		elif ((row==0 or row==3)) and (col>0 and col<5):
			print '*',
		else:
			print ' ',


	for col in range(6):
		if (col==0 or (col==4) and row>2):
			print '*',
		elif (((row==0 or row==6)and (col>0 and col<5)) or ((row==3)and(col==3 or col==5))):
			print '*',
		else:
			print ' ',

	# for col in range(6):
	# 	if (col==0 or col==4):
	# 		print '*',
	# 	elif (row==3 and(col>0 and col<4)):
	# 		print '*',
	# 	else:
	# 		print ' ',

	# # print ""			

	# for col in range(6):
	# 	if col==3:
	# 		print '*',
	# 	elif(row==0 or row==6) and (col>0 and col !=3):
	# 		print '*',		
	# 	else:
	# 		print ' ',
	# print ''	


	# for col in range(6):
	# 	if col==3:
	# 		print '*',
	# 	elif(row==0 and (col>0 and col !=3)) or (row==6 and (col<3) and col>0 ):
	# 		print '*',		
	# 	else:
	# 		print ' ',
	# print ''	



	# for col in range(6):
	# 	if col==0:
	# 		print '*',
	# 	elif((row==col+2 and col>0) or ((col==5-row and col>0) and row<3)):
	# 		print '*',		
	# 	else:
	# 		print '',
		
	# # print ''	

	# for col in range(6):
	# 	if col==0:
	# 		print '*',
	# 	elif((row==6 and col>0)):
	# 		print '*',		
	# 	else:
	# 		print '',
	# print ''	



	# for col in range(7):
	# 	if (col==0 or col==6):
	# 		print '*',
	# 	# elif(((row==col) and (col>0 and col<2 ) and row>0)):
	# 	# 	print '*',		
	# 	elif(((row==col) and (col>0 and col<4)) or ((row==1 and col==5) or (row==2 and col==4))):
	# 		print '*',			
	# 	else:
	# 		print ' ',
	# # print ''	

	# for col in range(7):
	# 	if (col==0 or col==6):
	# 		print '*',
	# 	elif((row==col) and (col>0 and col<6 )):
	# 		print '*',			
	# 	else:
	# 		print ' ',



	# for col in range(7):
	# 	if ((col==0 or col==6) and (row>0 and row<6)):
	# 		print '*',
	# 	elif ((row==0 or row==6)) and (col>0 and col<6):
	# 		print '*',
	# 	else:
	# 		print ' ',


	# for col in range(7):
	# 	if ((col==0) or (col==6 and (row>0 and row<3))):
	# 		print '*',
	# 	elif ((row==0 or row==3)) and (col>0 and col<6):
	# 		print '*',
	# 	else:
	# 		print ' ',


	# for col in range(7):
	# 	if ((col==0  or col==6) and (row>0 and row<5)):
	# 		print '*',
	# 	elif ((row==0 or row==5) and (col>0 and col<6)) or(col==5 and row==6) or (col==1 and row==4):
	# 		print '*',
	# 	else:
	# 		print ' ',	


	# for col in range(7):
	# 	if ((col==0  or (col==6 and row>0 and row<3))):
	# 		print '*',
	# 	elif ((row==0 or row==3) and (col>0 and col<6)) or(row>3 and col==row):
	# 		print '*',
	# 	else:
	# 		print ' ',



	# for col in range(7):
	# 	if ((col==0 and (row>0 and row<3)) or ((col==6 and row>3 and row<6))):
	# 		print '*',
	# 	elif ((row==0 or row==3 or row==6) and (col>0 and col<6)):
	# 		print '*',
	# 	else:
	# 		print ' ',

	# print ''

	# for col in range(7):
	# 	if ((col==3 and row>0)):
	# 		print '*',

	# 	elif (row==0 ):
	# 		print '*',
	# 		# time.sleep(0.1)
	# 	else:
	# 		print ' ',

	# for col in range(7):
	# 	if ((col==0 or col==6) and(row<6)):
	# 		print '*',

	# 	elif (row==6 and(col>0 and col<6)):
	# 		print '*',
	# 		# time.sleep(0.1)
	# 	else:
	# 		print ' ',	

	# for col in range(7):
	# 	if ((col==row and (col<4 and row<4))):
	# 		print '*',

	# 	elif (col==6-row and(row<3)):
	# 		print '*',
	# 	# 	time.sleep(0.1)
	# 	else:
	# 		print ' ',

	# for col in range(7):
	# 	if (col==0 or col==6):
	# 		print '*',

	# 	elif ((row>3 and (col==row and col<6)) or (row>2 and (col==6-row and (col<4 and col>0)))):
	# 		print '*',
	# 	# 	time.sleep(0.1)
	# 	else:
	# 		print ' ',

	# for col in range(7):
	# 	if (col==row or col==6-row):
	# 		print '*',
	# 	else:
	# 		print ' ',

	# # print ''

	# for col in range(7):
	# 	if (col==6-row or row==6 or row==0):
	# 		print '*',
	# 	else:
	# 		print ' ',

	print ''
