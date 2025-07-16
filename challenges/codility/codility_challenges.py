"""

author: Pedro Paulo Monteiro Muniz Barbosa
e-mail: pedropaulommb@gmail.com

Codility Challenges

"""

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


def binary_gap(N: int) -> int:
    """

    :param N: A positive integer.
    :return: The length of its longest binary gap
    """
    binary = "{0:b}".format(N)
    contador_0 = 0  # A counter of zeros to set the binary gap size.
    maior_gap = 0  # A variable to store the value of the largest binary gap.

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


def solution_flip_coin(A: list) -> int:
    """
    :param A: An array A consisting of N integers representing the coins. Consecutive elements of array A represent
    consecutive coins and contain either a 0 (heads) or a 1 (tails).
    :return: The minimum number of turns for the results to alternate.
    """

    min_flip_0 = 0  # The minimum number of turns starting with 0.
    min_flip_1 = 0  # The minimum number of turns starting with 1.

    for i, v in enumerate(A):
        if i % 2 != v:
            min_flip_0 += 1
        if (i + 1) % 2 != v:
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

    def rotation(A):  # -> This is a function to set the rotation of A by one unit to the right.
        return [A[-1]] + A[:-1]

    for i in range(K):  # -> As long as i is in the K range, the program will continue running.
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

    min_jump = 0  # The minimal number of jumps that the frog must perform to reach its target.
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
    A = set(A)  # To eliminate duplicate values of the array.
    A = list(A)  # To turn a set type on a list type.
    A.sort()  # To sort the list ascending.
    missing_element = 0  # A variable to store the missing element.
    x = len(A) - 1

    for i, v in enumerate(A):
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
    sum_x = sum(X)  # A variable to store the list value coming from the range of X.
    list_sum = list()  # A list to set the indices of array A that represent seconds.
    num_i = 0  # The moment when the frog can jump.
    sum_a = 0  # The sum of the "list_sum".

    for i, v in enumerate(A):
        if sum_x == sum_a:
            break
        list_sum = list(list_sum)
        list_sum.append(A[i])
        list_sum = set(list_sum)
        sum_a = sum(list_sum)
        num_i = i

    return num_i


"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

            Write a function:

                def solution(A)

            that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
"""


def solution_perm_check(A: list) -> int:
    """
    :param A: An array consisting of N integers.
    :return: 1 if the array is a permutation or 0 if it's not.
    """

    A = set(A)  # To set the array A and exclude repeated elements.
    A = list(A)  # To turn the set type on a list type.
    sum_i = 0
    list_sum_i = []

    for i in A:
        sum_i += 1
        list_sum_i.append(sum_i)

    return 1 if sum(list_sum_i) == sum(A) else 0


"""
You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

            Write a function:
            
                def solution(N, A)
            
            that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers 
            representing the values of the counters.
            
            Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
"""


def solution_max_counters(A: list, N: int) -> list:
    """
    :param A: A non-empty array A of M integers. This array represents consecutive operations:
    if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
    if A[K] = N + 1 then operation K is max counter.
    :param N: An integer N that represents N counters.
    :return: A sequence of integers representing the values of the counters.
    """

    list_counter = list(range(N))  # -> A list with N numbers of elements
    for i in list_counter:
        list_counter[i] = 0  # - > To set all the elements to zero

    for i, v in enumerate(A):

        if 1 <= v and v <= N:
            list_counter[v - 1] += 1

        elif v >= N + 1:
            max_value = max(list_counter)
            for j in range(0, len(list_counter)):
                list_counter[j] = max_value

    return list_counter


"""
This is a demo task.

            Write a function:

                def solution(A)

            that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not 
            occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution_missing_integer(A: list) -> int:
    """
    :param A: An array A of N integers.
    :return: The smallest positive integer (greater than 0) that does not occur in A.
    """

    A = set(A)  # -> To set the array A and exclude the repeated elements.
    list_num = list(range(len(A) + 2))  # -> To create a list with all the elements within the range of A.
    list_num.sort()  # -> To sort the list list_num.
    list_num.remove(0)  # -> To remove the 0 from the list so that it starts at 1.
    A = list(A)  # -> To turn the set type on a list type.
    A.sort()  # -> To sort the list A.
    num_a = 0
    num_list = 0
    missing_integer = 0
    print(A)
    print(list_num)

    for i, v in enumerate(A):
        if v > 0:
            num_a += A[i]
            num_list += list_num[i]
            print(num_a)
            print(num_list)
            if num_a != num_list:
                missing_integer = list_num[i]
                break
            else:
                missing_integer = A[i] + 1
        else:
            missing_integer = 1

    return missing_integer


"""
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars 
on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is 
traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

                Write a function:

                    def solution(A)

                that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

                The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""


def solution_passing_cars(A: list) -> int:
    """
    :param A: A non-empty array A consisting of N integers. The consecutive elements of array A represent consecutive
    cars on a road. Array A contains only 0s and/or 1s:
                0 represents a car traveling east,
                1 represents a car traveling west.
    :return: The number of pairs of passing cars.
    """

    west_count = 0
    result = 0
    n = len(A)

    while n >= 1:
        if A[n - 1] == 1:
            west_count += 1
        else:
            result += west_count
        n -= 1

    return result if result <= 10e8 else -1


"""
            Write a function:

                def solution(A, B, K)

            that, given three integers A, B and K, returns the number of integers within the range [A..B] that are 
            divisible by K, i.e.:

                { i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 
2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""


def solution_count_div(A: int, B: int, K: int) -> int:
    """
    :param A: An integer within the range i <= A <= i <= B.
    :param B: An integer within the range i <= A <= i <= B.
    :param K: An integer as a divisor.
    :return: The number of integers within the range [A..B] that are divisible by K, i.e.:
                                                                             { i : A ≤ i ≤ B, i mod K = 0 }
    """

    if type(A) != int or type(B) != int or type(K) != int:
        num_div = 0
    elif K < 1:
        num_div = 0
    elif A > B:
        num_div = 0
    else:
        num_div = 0
        num_list = list(range(A, B + 1))
        for i in num_list:
            try:
                if i % K == 0:
                    num_div += 1
            except ZeroDivisionError:
                num_div = 0

    return num_div


"""
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the types of 
successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. Nucleotides of 
types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer several queries of 
the form: What is the minimal impact factor of nucleotides contained in a particular part of the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M queries, 
which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) requires you to 
find the minimal impact factor of nucleotides contained in the DNA sequence between positions P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 3 and 2 
respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A whose impact 
factor is 1, so the answer is 1.

            Write a function:

                def solution(S, P, Q)

            that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting 
            of M integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

            Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P and Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
"""


def solution_genomic_range_query(S: str, P: list, Q: list) -> list:
    """
    :param S: A DNA sequence given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters.
    :param P: A non-empty array consisting of M integers.
    :param Q: A non-empty array consisting of M integers.
    :return: An array consisting of M integers specifying the consecutive answers to all queries
    """

    S = S.upper()
    imp_factor = []

    A = [0] * len(S)
    C = [0] * len(S)
    G = [0] * len(S)
    T = [0] * len(S)

    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0

    for i in range(0, len(S)):
        if S[i] == "A":
            count_a += 1
        elif S[i] == "C":
            count_c += 1
        elif S[i] == "G":
            count_g += 1
        elif S[i] == "T":
            count_t += 1

        A[i] = count_a
        C[i] = count_c
        G[i] = count_g
        T[i] = count_t

    for i in range(0, len(P)):
        if P[i] == Q[i]:
            if S[P[i]] == "A":
                imp_factor.append(1)
            elif S[P[i]] == "C":
                imp_factor.append(2)
            elif S[P[i]] == "G":
                imp_factor.append(3)
            elif S[P[i]] == "T":
                imp_factor.append(4)

        elif A[P[i]] < A[Q[i]] or S[P[i]] == "A":
            imp_factor.append(1)
        elif C[P[i]] < C[Q[i]] or S[P[i]] == "C":
            imp_factor.append(2)
        elif G[P[i]] < G[Q[i]] or S[P[i]] == "G":
            imp_factor.append(3)
        elif T[P[i]] < T[Q[i]] or S[P[i]] == "T":
            imp_factor.append(4)

    return imp_factor


"""
A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a 
slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of 
A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average 
equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

        Write a function:

            def solution(A)

        that, given a non-empty array A consisting of N integers, returns the starting position of the slice with 
        the minimal average. If there is more than one slice with a minimal average, you should return the smallest 
        starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""


def solution_min_avg_two_slice(A: list) -> int:
    """
    :param A: A non-empty array A consisting of N integers.
    :return: The starting position of the slice with the minimal average.
    """

    min_avg = max(A) * 2
    min_position = 0

    for i in range(0, len(A) - 2):
        avg_two = (A[i] + A[i + 1]) / 2
        avg_three = (A[i] + A[i + 1] + A[i + 2]) / 3

        if min(avg_two, avg_three) < min_avg:
            min_avg = min(avg_two, avg_three)
            min_position = i

    if ((A[-1] + A[-2]) / 2) < min_avg:
        min_position = len(A) - 2

    return min_position


"""
            Write a function

                def solution(A)

            that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


def solution_distinct(A: list) -> int:
    """
    :param A: An array A consisting of N integers.
    :return: The number of distinct values in array A.
    """

    values = list(set(A))
    distinct = len(values)

    return distinct


"""
A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) 
equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

For example, array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
contains the following example triplets:

(0, 1, 2), product is −3 * 1 * 2 = −6
(1, 2, 4), product is 1 * 2 * 5 = 10
(2, 4, 5), product is 2 * 5 * 6 = 60
Your goal is to find the maximal product of any triplet.

            Write a function:

                def solution(A)

            that, given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−1,000..1,000].
"""


def solution_max_product_of_three(A: list) -> int:
    """
    :param A: A non-empty array A.
    :return: The value of the maximal product of any triplet.
    """

    A.sort()
    n = len(A)

    product_1 = A[n - 1] * A[0] * A[1]
    product_2 = A[n - 1] * A[n - 2] * A[n - 3]

    max_product = max(product_1, product_2)

    return max_product


"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

            Write a function:

                def solution(A)

            that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this 
            array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""


def solution_triangle(A: list) -> int:
    """
    :param A: An array A consisting of N integers.
    :return: Returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.
    """

    A.sort()
    triangle = 0
    for i in range(0, len(A) - 2):
        if (A[i] + A[i + 1]) > A[i + 2]:
            triangle = 1

        if (A[-3] + A[-2]) > A[-1]:
            triangle = 1

    return triangle
