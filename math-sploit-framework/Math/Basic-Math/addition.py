#find their problem
problem = input("your problem here: ")

#de-stringify it
first, second = problem.split("+")
firstInt = int(''.join(x for x in first if x.isdigit()))
secondInt = int(''.join(x for x in second if x.isdigit()))
print(firstInt + secondInt)