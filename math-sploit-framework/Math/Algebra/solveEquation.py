#this program solves algebra equations for you
#author: Reid Powell
equation = input("Enter the equation: ")
print(equation)
#create a list of known variables
knownVariables = ["a", "b", "c", "x", "y", "z"]
#split the equation so that it is easier to deal with
body, answer = equation.split("=")
answerStringed = int(''.join(x for x in answer if x.isdigit()))
print("the body of the equation is: " + body)
print("the answer in this equation is " + answer)
#sorts through all of the chars in the equation until it finds a char that is in knownVariables
for char in equation:
    for char in knownVariables:
        noncharVersion = equation.split(char)
        for i in range(1, len(equation)):
            if equation[i] in knownVariables:
                pos = i + 1
#now it cycles through the chars in equation to count each one
newEquation = equation.replace(" ", "")
counter = 0
for char in newEquation:
    counter += 1
print(newEquation)
numberToGuessBy = equation[pos - 2]
numberToGuessByStringged = int(''.join(x for x in numberToGuessBy if x.isdigit()))
#find the middle part
starter = "+"
ender = "="
middle = newEquation[newEquation.find(starter)+1: newEquation.find(ender)]
middleStringged = int(''.join(x for x in middle if x.isdigit()))
print(middle)
#create a dummy num so that it can count
dummy = 0
#start a loop so that it try every possible iteration
while True:
    if middleStringged + (numberToGuessByStringged * dummy) != answerStringed:
        dummy += 1
    if middleStringged + (numberToGuessByStringged * dummy) == answerStringed:
        print("answer found")
        answerToEquation = dummy
        break

print("the answer is " + str(answerToEquation))