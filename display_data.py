import math


def checkRawData(lst):
    """
    Verifies that data is well-formed. Well formed means:
        each tuple has 3 elements (number, palindrome, steps)
        the palindrome and steps parameters can be no less than -1
    :param lst: should be a list of 3-tuples with elements 2, 3 no less than -1
    :return: true if the data is well-formed
    """
    return all([len(tup) == 3 and tup[1] >= -1 and tup[2] >= -1 for tup in lst])


def printRawResults(results):
    """
    Show raw data in readable format
    :param results: data from a given program run
    :return: nothing.
    """

    # Verify data
    if not checkRawData(results):
        print("Error: Data must be a series of (number, palindrome, steps) tuples. Try again.")

    print(f"\n{'Results': >25}")
    print("-" * 50)

    for test, pal, stp in results:
        print(f"Number: {test : 7} | steps: {stp : 4} |  palindrome: {pal} ")


def printBySteps(results):
    """
    Show data by a count of how many inputs take x steps to become a palindrome
    :param results: data
    :return: nothing.
    """
    # Verify data
    if not checkRawData(results):
        print("Error: Data must be a series of (number, palindrome, steps) tuples. Try again.")

    steps = [tup[2] for tup in results]

    print(f"\n{'Results': >15}")
    print("-" * 25)
    for stp in range(min(steps), max(steps) + 1):
        print(f"Steps: {stp : 4}  |  Count: {len([tup for tup in results if tup[2] == stp])}")


def printByPalidromeMag(results):
    pass


def printByLogPalindromeMag(results):
    # Verify data
    if not checkRawData(results):
        print("Error: Data must be a series of (number, palindrome, steps) tuples. Try again.")

    palindromes = [tup[1] for tup in results]

    print(f"\n{'Results': >20}")
    print("-" * 35)
    for i in range(int(math.log10(max(palindromes))) + 1):
        print(f"Palindromes over: 10^{i : <4}|"
              f"  Count: {len([tup for tup in results if (10 ** i) < tup[1] < (10 ** (i + 1))])}")


def printDuplicatePalindromes(results):
    pass
