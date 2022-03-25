#The first program a developer writes in a new language is typically a "hello world" program to
#see a first output on the screen. In this task, you will create a more advanced version that can generate
#a more complex greeting.

#Given the two variables `name` and `age`, write a program that will generate a personalized greeting. For example,
#for `"Karl"` and `25`, the program should generate the string `"Hello Karl, you are 25 years old!"`.

#Implement it in a function `generate_greeting` where it should be returned.

#Please make sure that your solution is self-contained within the `generate_greeting` function. 
#In other words, only change the body of the function, not the code outside the function.


name = "Kalr"
age = 25

# generate the greeting sentence
def generate_greeting():
    greeting = "Hello " + name + ", you are " + str(age) + " years old!"
    return greeting
