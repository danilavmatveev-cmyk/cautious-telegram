week_days = ["понедельник","вторник","среда","четверг","пятница","суббота","воскресенье"]

mood_list = []
for i in range (len(week_days)):
    mood = int(input())
    star = mood * "*"
    rating = f"({mood})"
    if 1 <= mood <= 10:
        mood_list.append(star + " " + rating)
    else:
        mood_list.append("(0)")

print('\n'.join(mood_list))