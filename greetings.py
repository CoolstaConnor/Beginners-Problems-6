def timeless():
    if time > 2359:
        print("Please ensure that your time entered is in between 0000 and 2359.")
        quit()
def goodmorningrange(time):
    timeless()
    if 0 <= time // 100 <= 12:
        print(f"Good morning, {name}!")
    else:
        goodafternoonrange(time)
    
def goodafternoonrange(time):
    timeless()
    if 13 <= time // 100 <= 17:
        print(f"Good afternoon, {name}!")
    else:
        goodeveningrange(time)
    
def goodeveningrange(time):
    timeless()
    if 18 <= time // 100 <= 23:
        print(f"Good evening, {name}!")

name = str(input("What's your name?: "))
time = int(input("What time is it for you in 24 hour time?: "))
goodmorningrange(time)