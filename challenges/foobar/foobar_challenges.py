"""

author: Pedro Paulo Monteiro Muniz Barbosa
e-mail: pedropaulommb@gmail.com

Foobar Challenges

"""

"""
There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been 
lording it over the poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked 
you with reassigning everyone new random IDs based on a Completely Foolproof Scheme. 

Commander Lambda has concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion 
must draw a number from a hat. That number is the starting index in that string of primes, and the minion's new ID 
number will be the next five digits in the string. So if a minion draws "3", their ID number will be "71113". 

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's 
string of all primes, and returns the next five digits in the string. Commander Lambda has a lot of minions, so the 
value of n will always be between 0 and 10000.

Languages
================================================================================

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
================================================================================
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
    Input:
    Solution.solution(0)
    Output:
        23571
    
    Input:
    Solution.solution(3)
    Output:
        71113

-- Python cases --
    Input:
    solution.solution(0)
    Output:
        23571
    
    Input:
    solution.solution(3)
    Output:
        71113
"""


def solution_prime_numbers(n: int):
    """
        A solution to select the ID number starting with a given prime number
    :param n: The number draw
    :return: The ID number
    """
    list_prime_numbers = list()
    for i in range(0, 20500):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                list_prime_numbers.append(str(i))

    list_prime_numbers = ''.join(list_prime_numbers)
    list_prime_numbers = list_prime_numbers[0:10006]

    id_number = list_prime_numbers[n: n + 5]

    return id_number


def solution_lauro(n):
    list_primes = ['2']
    count_len = 0
    number = 3
    while count_len < n + 5:
        num_div = number // 2
        is_prime = True
        if num_div >= 2:
            for i in range(num_div, 1, -1):
                if number % i == 0:
                    is_prime = False
                    break
        if is_prime:
            list_primes.append(str(number))
        number += 2
        count_len = len(list_primes)

    return ''.join(list_primes)[n: n + 5]


def solution(n):
    """
        A solution to select the ID number starting with a given prime number
    :param n: The number draw
    :return: The ID number
    """
    prime_number = "2"
    for num in range(0, 20500):
        if num > 1:
            for j in range(2, num):
                if (num % j) == 0:
                    break
                elif len(prime_number) >= 10006:
                    break
                elif j == num - 1:
                    prime_number += str(num)
                    break
                else:
                    continue

    return prime_number[n:n + 5]


"""
Power Hungry
================================================================================

Commander Lambda's space station is HUGE. And huge space stations take a LOT of power. Huge space stations with 
doomsday devices take even more power. To help meet the station's power needs, Commander Lambda has installed solar 
panels on the station's outer surface. But the station sits in the middle of a quasar quantum flux field, which wreaks 
havoc on the solar panels. You and your team of henchmen have been assigned to repair the solar panels, but you'd 
rather not take down all of the panels at once if you can help it, since they do help power the space station and all!

You need to figure out which sets of panels in any given array you can take offline to repair while still maintaining 
the maximum amount of power output per array, and to do THAT, you'll first need to figure out what the maximum output 
of each array actually is. Write a function solution(xs) that takes a list of integers representing the power output 
levels of each panel in an array, and returns the maximum product of some non-empty subset of those numbers. So for 
example, if an array contained panels with power output levels of [2, -3, 1, 0, -5], then the maximum product would be 
found by taking the subset: xs[0] = 2, xs[1] = -3, xs[4] = -5, giving the product 2*(-3)*(-5) = 30.  
So solution([2,-3,1,0,-5]) will be "30".

Each array of solar panels contains at least 1 and no more than 50 panels, and each panel will have a power output 
level whose absolute value is no greater than 1000 (some panels are malfunctioning so badly that they're draining 
energy, but you know a trick with the panels' wave stabilizer that lets you combine two negative-output panels to 
produce the positive output of the multiple of their power values). The final products may be very large, so give the 
solution as a string representation of the number.

Languages
================================================================================

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
================================================================================
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
    Input:
    solution.solution([2, 0, 2, 2, 0])
    Output:
        8
    
    Input:
    solution.solution([-2, -3, 4, -5])
    Output:
        60

-- Java cases --
    Input:
    Solution.solution({2, 0, 2, 2, 0})
    Output:
        8
    
    Input:
    Solution.solution({-2, -3, 4, -5})
    Output:
        60
"""


def power_hungry_solution(solar_panels: list):
    """
        A function to calculate the maximum product of some non-empty subset of the numbers of a given array.
    :param solar_panels: A list of integers representing the power output levels of each panel
    :return: The maximum product of the numbers of a given array.
    """

    if len(solar_panels) == 1:
        return str(solar_panels[0])

    # Cleaning list of zeros
    count_zero = 0
    for i in solar_panels:
        if i == 0:
            count_zero += 1
    solar_panels = [i for i in solar_panels if i != 0]

    # Cleaning list of numbers with an absolute value bigger than 1000
    solar_panels = [i for i in solar_panels if abs(i) < 1001]

    if len(solar_panels) < 1 and len(solar_panels) > 50:
        return -1

    # Counting negatives and finding the biggest negative value
    count_neg = 0
    max_neg = -9999999999999
    product = 1
    for i in solar_panels:
        if i < 0:
            count_neg += 1
            max_neg = max(max_neg, i)
        product = product * i

    # Checking if there is an odd number of negative values
    product_str = str()
    if count_neg % 2 == 1:
        if count_neg == 1 and count_zero > 0:
            return str(0)
        product = product / max_neg
        if product < 10000:
            product = int(product)
        product_str = "{:.0f}".format(product)
        return product_str

    return str(product)
