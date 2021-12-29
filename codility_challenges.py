"""

author: Pedro Paulo Monteiro Muniz Barbosa
e-mail: pedropaulommb@gmail.com

Codility Challenges
"""
from typing import List, Any

"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at 
both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary 
representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary 
representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no 
binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

    Write a function:

        def solution(N)

    that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N 
    doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its 
longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation 
'100000' and thus no binary gaps.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""

def binary_gap(N : int) -> int:
    """

    :param N: A positive integer.
    :return: The length of its longest binary gap
    """
    binary = "{0:b}".format(N)
    contador_0 = 0 # A counter of zeros to set the binary gap size.
    maior_gap = 0 # A variable to store the value of the largest binary gap.

    for i in binary:

        if i == '1':
            if (contador_0 > maior_gap):
                maior_gap = contador_0
            contador_0 = 0
        if i == "0":
            contador_0 += 1

    return maior_gap


""" 

There are N coins, each showing either heads or tails. We would like all the coins to form a sequence of
    alternating heads and tails. What is the minimum number of coins that must be reversed to achieve this?

    Write a function:
    def solution (A)

    that, given an array A consisting of N integers representing the coins, returns the minimum number of coins that
    must be reversed. Consecutive elements of array A represent consecutive coins and contain either a 0 (heads) or a
    1 (tails).

    Examples:
    1. Given array A = [1, 0, 1, 0, 1, 1], the function should return 1. After reversing the sixth coin, we achieve an
    alternating sequence of coins [1, 0, 1, 0, 1, 0].
    2. Given array A = [1, 1, 0, 1, 1], the function should return 2. After reversing the first and fifth coins, we
    achieve an alternating sequence [0, 1, 0, 1, 0].
    3. Given array A = [0, 1, 0], the function should return O. The sequence of coins is already alternating.
    4. Given array A = [0, 1, 1, 0], the function should return 2. We can reverse the first and second coins to get the
    sequence: [1, 0, 1, 0].

    Assume that:
        • N is an integer within the range [1..100];
        • each element of array A is an integer that can have one of the following values: 0, 1.

"""

def solution(A : list) -> int:
    """
    :param A: An array A consisting of N integers representing the coins, returns the minimum number of coins that must
    be reversed. Consecutive elements of array A represent consecutive coins and contain either a
    0 (heads) or a 1 (tails).
    :return: The minimum number of turns for the results to alternate.
    """
    min_flip_0 = 0 # The minimum number of turns starting with 0.
    min_flip_1 = 0 # The minimum number of turns starting with 1.

    for i,v in enumerate(A):
        if i%2 != v:
            min_flip_0 += 1
        if (i + 1)%2 != v:
            min_flip_1 += 1

    return min(min_flip_0, min_flip_1)

"""
An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one 
index, and the last element of the array is moved to the first place. For example, the rotation of array 
A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

        Write a function:

            def solution(A, K)

        that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]

Assume that:

N and K are integers within the range [0..100];
each element of array A is an integer within the range [−1,000..1,000].
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""


def rotation_solution(A, K):
    """
    :param A: A list of integers.
    :param K: A number of times that the list will be shifted to the right.
    :return: A list that was shifted a K number of times.
    """

    def rotation(A):        # -> This is a function to set the rotation of A by one unit to the right.
        return [A[-1]] + A[:-1]

    for i in range(K):      # -> As long as i is in the K range, the program will continue running.
        A = rotation(A)
    return A

"""
A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element 
of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.

    Write a function:

        def solution(A)

    that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired 
    element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times.
"""


def solution_odd_occurrency(A):
    """
    :param A: A list of integers.
    :return: The value of the unpaired element.
    """

    unpaired = set()
    for i in A:
        if i in unpaired:
            unpaired.remove(i)

        else:
            unpaired.add(i)

    result = unpaired.pop() if len(unpaired) > 0 else 0
    return result


"""
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get 
to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.

Count the minimal number of jumps that the small frog must perform to reach its target.

        Write a function:

            def solution(X, Y, D)

        that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or 
        greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:

X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
"""

def solution_frog_jump(X: int, Y: int, D: int) -> int:
    """
    :param X: The position where the frog is located.
    :param Y: Position where the frog wants to go (X =< Y).
    :param D: Fixed distance that the frog jumps.
    :return: The minimal number of jumps that the frog must perform to reach its target.
    """

    min_jump = 0        # The minimal number of jumps that the frog must perform to reach its target.
    position = X

    while position < Y:
        position = (X + D)
        min_jump += 1
        X = position

    return min_jump

"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], 
which means that exactly one element is missing.

Your goal is to find that missing element.

    Write a function:

        def solution(A)

    that, given an array A, returns the value of the missing element.

For example, given array A such that:
  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""


def solution_missing_element(A: list) -> list:
    """
    :param A: An array consisting of N different integers
    :return: The value of the missing element.
    """
    A = set(A)      # To eliminate duplicate values of the array.
    A = list(A)     # To turn a set type on a list type.
    A.sort()        # To sort the list ascending.
    missing_element = 0     # A variable to store the missing element.
    x = len(A) - 1

    for i,v in enumerate(A):
        if i == x:
            """
            The highest valued element in the array will never be the missing element. That way, we can eliminate it so 
            that an error like "list index out of range" doesn't occur.
            """
            break
        if A[i + 1] != (A[i] + 1):
            missing_element = A[i] + 1



    return missing_element


"""
A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: 
                        A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: 
                       |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

        For example, consider array A such that:
        
              A[0] = 3
              A[1] = 1
              A[2] = 2
              A[3] = 4
              A[4] = 3
        We can split this tape in four places:
        
                P = 1, difference = |3 − 10| = 7
                P = 2, difference = |4 − 9| = 5
                P = 3, difference = |6 − 7| = 1
                P = 4, difference = |10 − 3| = 7

            Write a function:
        
                    def solution(A)
        
            that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""



def solution_tape_equilibrium(A: list) -> int:
    """
    :param A: A non-empty array A of N integers.
    :return: The minimal difference that can be achieved.
    """
    import math

    x = len(A)
    min_value = math.inf


    for i in A:
        if i == x:
            break

        num_list = A[: i]
        num_list_2 = A[i:]
        part_1 = sum(num_list)
        part_2 = sum(num_list_2)
        y = abs(part_1 - part_2)

        if y < min_value:
            min_value = y



    return min_value


"""
A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river 

(position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the 
river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where 
one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only 
when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when 
all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is 
negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that: 

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the 
river.

        Write a function:

            def solution(X, A)

        that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog 
        can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
"""


def solution_frog_river_one(A: list, X: int) -> int:
    """
    :param A: An array consisting of N integers representing the falling leaves
    :param X: The position the frog wants to reach.
    :return: The earliest time when the frog can jump to the other side of the river.
    """

    X += 1
    X = range(X)
    X = list(X)
    sum_x = sum(X)
    list_sum = list()
    num_i = 0
    sum_a = 0

    for i,v in enumerate(A):
        if sum_x == sum_a:
            break
        list_sum = list(list_sum)
        list_sum.append(A[i])
        list_sum = set(list_sum)
        sum_a = sum(list_sum)
        num_i = i


    return num_i

