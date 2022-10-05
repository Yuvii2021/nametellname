# function to double the number
def num (n) :
	return n * 2
		
lst = [2, 44, 5.5, 6, -7]

# suppose we want to call function
# 'num' for each element of lst,
# we use map

# creates a map object
x = map(num, lst)
print(x)

# returns list
print(list(x))
