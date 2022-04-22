'''
Sophia DiCuffa
Lab 11
I pledge my honor that I've abided by the stevens honor code
4/14/22
'''


def swap(aList, i, j):
    '''swaps the values of aList[i] and aList[j]'''
    aList[i], aList[j] = aList[j], aList[i]

def isSorted(L):
    '''Whether L is sorted.'''
    for i in range(1,len(L)):
        if L[i-1] > L[i]: return False
    return True

def allLE(L,x):
    '''Whether every element of L is less than or equal to x.'''
    for i in range(len(L)):
        if x < L[i]: return False
    return True

#############################################################
# Step 0: Implement this function (insertion in ordered list).
# Notice that it does not return anything.  It just modifies 
# the contents of a list.
# Some tests are provided.
#############################################################

def insertV1(L, i):
    '''Assume L[0:i] is sorted and 0 < i < len(L).
       Shift elements of the list as needed, and swap L[i] into 
       position so that L[0:i+1] is sorted.'''
    while( i > 0):
        k = i - 1
        if L[i] < L[k]:
            swap(L,i,k)
            if isSorted(L) == True:
                print (L)
        i -= 1
    print (L)

L = [0,2,4,6,3,0,5]
insertV1(L, 4)

def testInsert(ins):
    '''Assume ins is a function.  Test whether it solves the insert problem.
    For example, testInsert(insertV1).'''

    L = [0,2,4,6,3,0,5]
    ins(L, 4) # in middle
    assert L == [0,2,3,4,6,0,5]

    L = [1,2,3,4,1] # near start
    ins(L,4)
    assert L == [1,1,2,3,4]

    L = [1,2,3,0] # at start
    ins(L,3)
    assert L == [0,1,2,3]

    L = [1,3,5,5] # at end
    ins(L,3)
    assert L == [1,3,5,5]

    L = [4,3] # short list
    ins(L,1)
    assert L == [3,4]
testInsert(insertV1)
#############################################################
# Step 1: Implement this function.
# Before coding, make sure you understand the description of
# search(L,i,x) by figuring out how it could be used to solve 
# another problem, namely: whether x is in L.
#############################################################

def search(L, i, x):
    '''Assuming L[0:i] is sorted and 0 <= i <= len(L),
       return j such that 0 <= j <= i and L[0:j] <= x < L[j:i]. '''
    k = 0
    for j in range(i):
        if L[j]<= x:
            k +=1
    print(k)

def testSearch():
    # in middle
    assert search([0,2,4,6,3,0,5], 3, 3) == 2
    # near start
    assert search([1,2,3,4,1], 3, 1) == 1
    # at start 
    assert search([1,2,3,0], 3, 2) == 2
    # at end
    assert search([1,3,5,5], 3, 6) == 3
    # at end, short list 
    assert search([0], 1, 5) == 1
    # at start, short list
    assert search([5], 1, 2) == 0

#############################################################
# Step 2: Implement the following version of insertion.
##############################################################
    
def insertV2(L, i):
    '''Assume L[0:i] is sorted and 0 < i < len(L).
       Shift elements of the list as needed to swap L[i] into 
       position so that L[0:i+1] is sorted.'''
    value = L[i]
    x = search(L,i,value)
    while (i>x):
        swap(L,i-1,i)
        i -= 1
    print (L)
    

    # Do this version as follows: save the value of L[i], use the 
    # search function to find where to insert that value, then 
    # shift to make room, and finally put the value in place.


##################################################
# Step 3: Here are two versions of insertion sort.
# Run the tests to be sure that your insertV1 and
# insertV2 work correctly.
##################################################

def insertSortV1(L):
    '''Sort L in place, using insertV1.'''
    for i in range(1,len(L)):
        assert isSorted(L[0:i])
        insertV1(L,i)
    assert isSorted(L)

def insertSortV2(L):
    '''Same as V1 but using insertV2.'''
    for i in range(1,len(L)):
        assert isSorted(L[0:i])
        insertV2(L,i)
    assert isSorted(L)


import random # for testing

def randList(N):
    '''A list of N randomly chosen numbers in the range 0..50.'''
    L = [0]*N
    for i in range(N):
        L[i] = random.randrange(50)
    return L

def testV1():
    testSort(insertSortV1)

def testV2():
    testSort(insertSortV2)
    
def testSort(sortFun):
    
    def test(L):
        print(L)
        sortFun(L)
        print("sorted?", L)
        assert isSorted(L)

    test([]) # empty
    test([3]) # one element
    test(list(range(7))) # already sorted
    test(randList(5))
    test(randList(5))
    test(randList(10))
    test(randList(20))



#############################################
# Step 4: Implement letterCounts.
# Hints and sample output are given below.
# Two test files, small_file.txt and dict.txt,
# are provided for testing.
#############################################

def letter(s):
    if 'a' <= s <= 'z': return s
    elif 'A' <= s <= 'Z': return s.lower()
    else: return "non-letter"
    
freqs = {"non-letter" : 0}
def letterCounts(fname):
    with open(fname) as f:
        for line in f:
            for char in line:
                if char.isalpha() == True:
                    if letter(char) in freqs:
                        freqs[char] += 1
                    else:
                        freqs[char] = 1
                else:
                    freqs['non-letter'] += 1
        return freqs

print(letterCounts('small_file.txt'))

# HINTS

# Use a dictionary to keep track of the counts, with lower case letters
# as keys.  Also one special key, "non-letter".

# You can use a for-loop to get the letters in a string, like this: 
# for c in "abc":

# Pairs like (7,'a') can be compared using <, which will compare 
# the first element and if they're equal compare the second.  (Try it!)

# You may use the built-in .sort() operation, and also .reverse() 
# But for more fun, use your own insertSortV2. And write your own
# reverse function using a loop.

# For reading a file and processing it line by line, see the function
# read_print_user_prefs in demo_file_io.py

# Here is the complete output of letterCounts("small_file.txt")
# [(3, 'non-letter'), (3, 'l'), (2, 't'), (1, 'x'), (1, 's'),
#   (1, 'm'), (1, 'i'), (1, 'f'), (1, 'e'), (1, 'a')]

# Here is part of the output of letterCounts("dict.py"):
# [(17293, 'non-letter'), (1927, 'e'), (1606, 'a'), (1331, 'o'), (1250, 'r')...

