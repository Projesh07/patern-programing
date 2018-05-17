# pattern-programing using 2D Matrix

You can understand different Pattern of 2D Matrix such as different Alphabetical character.

# A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z

To print  patterns of 2D matrix you have to use two for loops. In  this program that prints pattern contains two for loops: the first loop is responsible for rows and the second for loop is responsible for columns.

Here is an Example:


	# 	0 1 2 3 4 5 6
	# 0	  * * * * *  
	# 1	*	     *
	# 2	* * * * * * **
	# 3	*	     *
	# 4	*	     *
	# 5     *            *
	# 6     *            *

	# 7x7 matrix

                        

	for row in range(7):      			      # Looping through Row
		for col in range(7):                          # Looping through Column

			if (row==0 or row==3) and (col>0 and col<4):
				print '*',                                #This print is used to print star in a position where condition matches
			elif (col ==0 or col==4) and row !=0:
				print '*',                                #This print is used to print star in a position where condition matches
			else:
				print ' ',                                # This print is for every space where * is not needed

		print ""                                                  #This print is for every new line after each Row


More are comming soon. when time and things are getting cool.
