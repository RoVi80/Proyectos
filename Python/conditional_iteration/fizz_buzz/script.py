#"FizzBuzz": Every time a number is divisible by 3, a person will say "Fizz" instead of the number and every time a number is divisible by 5, they will say "Buzz". 
#If a number is divisible by both 3 and 5, the person should say "FizzBuzz". So for example, the first couple of steps would be:
#1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, FizzBuzz, 31, 32, Fizz, 34, Buzz, Fizz, and so on...
#Your task is to provide implementations for the two additional test cases:
#Your task is to provide implementations for the two additional test cases:

#1. The third test case, `test_five`, should check that for `n = 5`, the function correctly returns "Buzz".
 #2. The fourth test case, `test_fifteen`, should check that for `n = 15`, the function correctly returns "FizzBuzz".

#Please do not rename the four existing tests, but feel free to add more of your own.
#You will notice that once you implement the fourth test case, the test suite will fail, because the function is returning "Fizz" instead of "FizzBuzz". Your final task is:

#3. Fix the bug in the implementation of `fizz_buzz()` so that all tests pass.

#If you want to run the test suite locally on your machine, make sure you are in the top-level directory of the exercise (which contains the public folder and description), and then run `python -m unittest public/tests.py`.
#Alas, we may not yet have discussed imports, classes, "self" and other aspects of the testing code, but you should be able to mentally "pattern-match" the important parts given the existing examples and comments. For future reference, have a look at the [unittest Python module](https://docs.python.org/2/library/unittest.html#unittest.TestCase.debug). In this exercise, we only used `assertEqual`, but there are many more such functions, like `assertTrue`, `assertGreater` or `assertAlmostEqual`, which you may find useful.


n = 0

def fizz_buzz():
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

