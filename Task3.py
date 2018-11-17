#Write a decorator that stores the result of a function call and returns the cached version in
#subsequent calls (with the same parameters) for 5 minutes, or ten times ­­ whichever comes
#first.

from functools import wraps
import time
import datetime

def memoize(function):
    memo = {}

    @wraps(function)
    def wrapper(*args):
        if (args in memo) and (memo['cache'] < 10 and memo['elapsedTime'] < 300) :
            #Taking result from cache:
            memo['cache'] = memo['cache'] + 1
            memo['elapsedTime'] = time.time() - memo['startTime']

            return memo[args]

        else:
            #Clearing cache:
            memo['cache'] = 1
            memo['startTime'] = time.time()
            memo['elapsedTime'] = 0

            #Storing result from function:
            f_result = function(*args)
            memo[args] = f_result
            return f_result
    return wrapper

@memoize
def get_element(e):
    myList = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
    time.sleep(5)
    return (myList[e], datetime.datetime.now())




for i in range (0,200):
    print (get_element(1))
    #time.sleep(3)

