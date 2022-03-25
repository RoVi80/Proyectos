#In number theory, a friendly number is a natural number that shares a certain characteristic called abundancy with one or more other numbers. 
#Abundancy is the ratio between the sum of divisors of the number and the number itself. Two different numbers with the same abundancy form a friendly pair.

#The abundancy of n is the rational number σ(n) / n, in which σ denotes the sum of divisors function. A number n is a friendly number if there exists m ≠ n where σ(m) / m = σ(n) / n.

#For example 6 is a friendly number because abundancy of 6 and 28 are same : 2. Thus 6 and 28 are friendly pair

#The divisors of 6 are 1, 2, 3, 6. σ(n) is calculated as the sum of divisors.
#So in this case σ(6) = 1+2+3+6 = 12. We found σ(6) = 12. Now we need to calculate the abundancy of 6.
#The abundancy is σ(n) / n . So in this case: σ(6) / 6 = 12 / 6 = 2
#So the abundancy of 6 is 2.
#Now we calculate the abundancy of 28: σ(28) / 28 = (1+2+4+7+14+28) / 28 = 2.
#Since abundancies of 6 and 28 are both 2 we call (6, 28) a friendly pair.
#Your task is to implement an algorithm in the function isFriendlyPair which checks whether two numbers are a friendly pair or not.

num1 = 1
num2 = 28

def isFriendlyPair():

    # The sum of divisors of num1
    teta1 = 0
    # The sum of divisors of num2
    teta2 = 0

    # Division of teta1 by num1 . teta1 / num1
    abundancy1 = 0 

    # Division of teta2 by num2 . teta2 / num2 
    abundancy2 = 0

    # Check if num1 and num2 are natural numbers and they are not the same. 
    # If conditions are not met return Invalid
    if num1 < 1 or num2 < 1 or num1 == num2 or not isinstance(num1, int) or not isinstance(num2, int):
        return "Invalid"
    else :
        # Find divisors of num1, calculate their sum and set it to teta1
        for x in range(1,num1+1):
            if num1%x==0:
                teta1 = teta1 + x
        
        # Calculate abundancy of number 1 by dividing teta1 by number 1
        abundancy1 = teta1 / num1 

        # Find dividers of num2, calculate their sum and set it to teta2
        for x in range(1,num2+1):
            if num2 % x==0:
                teta2 = teta2 + x
       
        # Calculate abundancy of number 2 by dividing teta1 by number 2
        abundancy2 = teta2 / num2

        # If both abundancies are equal num1 and num2 are friendly pairs so return True. 
        # If they are different return False since numbers are not friendly pairs
        if abundancy1 == abundancy2:
            return True 
        else :
            return False
