nums = []
evennums = []
oddnums = []
numberslist = []

def getEven(number):
    if number % 2 == 0:
        evennums.append(number)
        numberslist.append(number)
        return(evennums)
    else:
        oddnums.append(number)
        numberslist.append(number)

for i in range(5):
    number = int(input("Enter a number: "))
    nums.append(number)
    getEven(number)
print(f"Here is your list: {numberslist}")
print(f"Here is your list of even numbers: {evennums}")