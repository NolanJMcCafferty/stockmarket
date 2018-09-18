import sys
import time

# get the list of stock prices from the input file
data = [int(line.strip()) for line in open(sys.argv[1], 'r')]

# remove the first element which is the length
length = data.pop(0)

# start clock for time testing
start_time = time.time()


# function to compute longest non-decreasing subsequence
def get_longest(a):

	# base-case where each list has one element
    if len(a) < 2:

    	# return the length 1 and start index 1
        return (1,1,a)

    # recursive case 
    else:

    	# index of halfway element
        index = int(len(a)/2)

        # find the longest non-decreasing subsequence for the left half
        left_n, start_left, left = get_longest(a[:index])

        # find the longest non-decreasing subsequence for the right half
        right_n, start_right, right = get_longest(a[index:])   

        # mark the first element in the right half and initialize counter i  
        first_right = right[0]
        i = 1

        # compute the longest non-decreasing subsequence that
        # contains elements in the left array and the first element in the right array
        while  first_right >= left[-i]:

        	# move left
            first_right = left[-i]
            i+=1
            if i > len(left):
                break
            
        # mark the first element in the right array as the end and initialize counter j
        end = right[0]
        j = 1

        # check that the right array has more than one element
        if len(right) > 1:

        	# compute the longest non-decreasing subsequence that
        	# begins with the first element in the right array
            while end <= right[j]:

            	# move right
                end = right[j]
                j+=1
                if j == len(right):
                    break

        # compute the longest non-decreasing subsequence 
        # that contains elements from both arrays
        mid_n = i+j-1

        # find the max of the three longest sequences
        n = max(left_n, mid_n, right_n)

        # check where the longest sequence is located
        if n == left_n:

        	# keep the start index of the left array
            start = start_left
        elif n == right_n:

        	# add the length of the left array to the start index of the right
            start = len(left) + start_right
        else:

        	# get the first element in the left array that is in the longest sequence
            start = len(left) - i + 2
                
        # return the length of the subsequence, the start index, and the whole array
        return (n,start,left+right)

# run the algorithm on the input data
n, start, data = get_longest(data)

# stop the clock for time testing
elapsed_time = time.time() - start_time

# get the longest non-decreasing subsequence using the start index and length
days = data[(start-1):(start+n-1)]

# display output including time data 
print("longest =", n)
print("start = ", start)
print("time = ", elapsed_time)
print("n = ", len(data))


# write the length, start index, and subsequence to the given output file
with open(sys.argv[2], 'w') as outfile:
	outfile.write(str(n)+'\n')
	outfile.write(str(start) + '\n')
	for day in days:
		outfile.write(str(day) + '\n')

