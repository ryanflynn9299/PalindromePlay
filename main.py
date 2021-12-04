"""
Ryan Flynn
Palindrome Fun

I saw a Youtube video about this strange phenomenon and had to test it out.
You're welcome to download it and modify it as much as you wish, If you use any
of the original code and publish it, please link my Github repo!!

Here's the trick:
Take a number:              174
Reverse its digits:         471
add:                        645
repeat!
Eventually, you get:        5115, a palindrome!

This code provides a way to test this behavior, and identify which numbers don't work (I won't spoil!).
Complete with unit tests, this code enables you to define a selection of positive integers,
run the analysis, and display the results in several formats. Enjoy!

Requires Python 3.6+
"""


from display_data import *


def isPalindrome(n):
    """
    Check if [n] is a palindrome
    :param n:
    :return:
    """
    return n >= 0 and str(n) == str(n)[::-1]


def getPalindromeAndSteps(n, enforcelimit=True, steplimit=100):
    """
    At each step, check for palindrome, otherwise add reversed digits and repeat
    :param n: number to check
    :param enforcelimit: optional param to disable limit (for discovery operations)
    :param steplimit: optional param to limit steps checked before returning -1, -1
    :return: the palindrome and the number of steps it took, or (-1, -1) on an error condition
    """
    if n < 0:
        return -1, -1

    steps = 0
    while not isPalindrome(n):
        if enforcelimit and steps >= steplimit:
            break

        steps += 1
        n = n + int(str(n)[::-1])
    else:
        # successfully found palindrome
        return n, steps

    # limit hit, loop broken out of
    return -1, -1


def main():
    tstval = 1000

    # Intro quip (optional, comment out in unwanted)
    print(f"\nTesting first {tstval} numbers...")

    # set tests
    # tests = [10, 296, 991, 10567]
    tests = list(range(tstval))

    # gather data
    data = [(tst, *getPalindromeAndSteps(tst)) for tst in tests]

    # print results
    printByLogPalindromeMag(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
