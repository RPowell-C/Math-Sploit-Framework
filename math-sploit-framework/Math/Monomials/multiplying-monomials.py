#this is for multiplying monomials
#author: Reid Powell


firstNum = int(input("what is the first monomial? "))
secondNum = int(input("what is the second monomial? "))
variableQues = input("what is the variable? ")
firstNumsPower = int(input("what is the first monomial's power? "))
secondNumsPower = int(input("what is the second monomial's power? "))

#now add them
sumOfNums = firstNum * secondNum
powerOfNums = firstNumsPower + secondNumsPower

print("the answer is " + str(sumOfNums) + str(variableQues) + "^" + str(powerOfNums))