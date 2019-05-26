def decompose(n):
	if n ==1:
		return [1]
	else:
	    goal = 0
	    print ("Adding n, %s, to sequence.\n" % (n))
	    result = [n]
	    while result:
	        current = result.pop()
	        print ("The last number, %s, wasn't helpful. Removing it from sequence and adding it back to `goal`" % (current))
	        print ("Trying lower numbers now.\n" if current - 1 > 0 else "\n")

	        # Goal is the square of n.
	        goal += current ** 2
	        for i in range(current - 1, 0, -1):
	            print ("Trying %s" % (i))
	            if goal - (i ** 2) >= 0:
	            	# Goal are greater than zero we can decrement goal and continue 
	                goal -= i ** 2
	                result.append(i)
	                "This number, %s, might work. Goal is not below zero. Adding it to sequence and subtracting from `goal`." % (i)
	                if goal == 0:
	                	# End.
	                    result.sort()
	                    print ("\nFound result, %s." % (result))
	                    return result
	            else:
	              # It is too big
	              print ("This number, %s, is too big here. Continuing." % (i))
	    return None
		

def test_decomponse_one():
	assert decompose(1) == [1];

def test_decomponse_five():
	assert decompose(5) == [3,4];

def test_decomponse_eigth():
	assert decompose(8) == None;

def test_decomponse_nine():
	assert decompose(9) == [1, 4, 8];


test_decomponse_one();
test_decomponse_five();
test_decomponse_eigth();
test_decomponse_nine();
