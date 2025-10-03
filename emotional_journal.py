week_days = ["понедельник","вторник","среда","четверг","пятница","суббота","воскресенье"]
mood = [1,2,3,4,5,6,7,8,9,10]
mood_list=[]
for i in range (len(week_days)):
    mood = input()
    if mood == mood [0]:
        mood_list = mood_list.append("*(1)")
    elif mood == mood [1]:
        mood_list = mood_list.append("**(2)")
    elif mood == mood [2]:
        mood_list = mood_list.append("***(3)")
    elif mood == mood [3]:
        mood_list = mood_list.append("****(4)")
    elif mood == mood [4]:
        mood_list = mood_list.append("*****(5)")
    elif mood == mood [5]:
        mood_list = mood_list.append("******(6)")
    elif mood == mood [6]:
        mood_list = mood_list.append("*******(7)")
    elif mood == mood [7]:
        mood_list = mood_list.append("********(8)")
    elif mood == mood [8]:
        mood_list = mood_list.append("*********(9)")
    elif mood == mood [9]:
        mood_list = mood_list.append("**********(10)")
    else:
        mood_list = mood_list.append("(0)")

print('\n'.join(mood_list))