#sophisticated search vs russian searh comparisonator
import time
import random
global size, r

def sophisticated(NumbersArray, small, big, SearchingNumber): # a binary search for the SearchingNumber we're looking for 
    if big >= small:
 
        mid = (big + small) // 2
 
        # If element is at the midpoint
        if NumbersArray[mid] == SearchingNumber:
            return mid
 
        # If element is smaller than mid, then we move the endpoint to the mid -1 and re-establish the boundaries and midpoint.
        elif NumbersArray[mid] > SearchingNumber:
            return sophisticated(NumbersArray, small, mid - 1, SearchingNumber) # trial and error until VICTORY
 
        # If the element is larger than mid, then we move the start point to the mid + 1 and re-establish the boundaries and midpoint.
        else:
            return sophisticated(NumbersArray, mid + 1, big, SearchingNumber) # trial and error until VICTORY

    return NumbersArray

def Rasshya(SearchingNumber):
    for x in range(len(NumbersArray)):
        if NumbersArray[x] == SearchingNumber:
            break # the somewhat russian way of doing things: manually checking each and every position until it finds a match, then exists the loop, pausing the timer.

def bubblesort(): # this whole thing is simply to re-organise the times 2d array in order to make the timings in ascending order.
    for a in range(2):
        for y in range(len(times[0])):
            for x in range(len(times[0])-1):
                if times[a][x] > times[a][x + 1]:
                    times[a][x], times[a][x + 1] = times[a][x + 1], times[a][x]

def importdic(Length):# change of mind: instead of adding the whole dictionary to the program, i've decided to substitute them for numbers instead.
    for x in range(Length): NumbersArray.append(x)

def mainprogram(NumbersArray): #where all the magic happens
    #russian method
    SearchingNumber = random.randint(0,len(NumbersArray)) # picks out a random number in the array
    st = time.time() #  starts the timer
    Rasshya(SearchingNumber) # russian searches it (see the function for more information)
    et = time.time() # stops the timer
    lt = et - st # finds out how long it took
    times[0].append(lt) # adds it to the list of times
    #sophisticated method
    st = time.time() # starts timer
    sp = 0
    ep = len(NumbersArray)
    temp = (ep + sp) / 2
    temp = int(temp)
    midpoint = temp
    # everything above was setting the boundaries for the start, end and midpoint.
    result = sophisticated(NumbersArray, 0, ep-1, SearchingNumber) # sophisticated searches it, see the function for more info.
    et = time.time() # stops the timer
    lt = et - st # finds out how long it took
    times[1].append(lt) # adds it to the list of times.


times = [[],[]]
NumbersArray = [] 
importdic(int(input("how many of the terms should we use?\n")))

average = int(input("how many runs should we do? \n"))
for x in range(average): mainprogram(NumbersArray) # repeats the main program average many times, so that we can properly find the average afterwards.
bubblesort()
a1 = 0 # average for the russian sorting method
a2 = 0 # average for the sophisticated sorting method
for x in range(len(times[1])): 
    a1 += times[0][x]
    a2 += times[1][x]
a1 = a1 / len(times[1])
a2 = a2 / len(times[1])
# here is just printing off the statistics
print("the smallest value of russian method was", times[0][0])
print("the largest value of russian method was", times[0][-1])
print("the average value of russian method was", a1)
print("the smallest value of the sophisticated method was", times[1][0])
print("the largest value of the sophisticated method was", times[1][-1])
print("the average value of the sophisticated method was", a2)