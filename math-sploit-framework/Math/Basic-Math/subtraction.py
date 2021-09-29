#find their problem
problem = input("your problem here: ")

#de-stringify it
first, second = problem.split("-")
firstInt = int(''.join(x for x in first if x.isdigit()))
secondInt = int(''.join(x for x in second if x.isdigit()))
if firstInt < secondInt:
    print("whoops! looks like you inputed your problem incorrectly\nif this was intended please try to do so under algebra's subtraction")
else:
    print(firstInt - secondInt)