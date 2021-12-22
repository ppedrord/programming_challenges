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

def binary_gap(N : int) -> int:
    """

    :param N: A positive integer.
    :return: The length of its longest binary gap
    """
    binary = "{0:b}".format(N)
    print(binary)
    contador_0 = 0 # A counter of zeros to set the binary gap size.
    maior_gap = 0 # A variable to store the value of the largest binary gap.

    for i in binary:

        if i == '1':
            if (contador_0 > maior_gap):
                maior_gap = contador_0
            contador_0 = 0
        if i == "0":
            contador_0 += 1

    print(maior_gap)
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