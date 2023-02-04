import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

while True:
    find = int(input("type number: "))
    if find < 5:
        print(f"{find}voice name is:",voices[find].name)
    else:
        print('none')


#Honestly its use is not that important, but if you want to see which voices your windows has, instead of going to regedit it's ok