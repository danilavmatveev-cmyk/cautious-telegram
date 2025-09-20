import random

seed = ["камень","ножницы","бумага"]

computer_score = 0
student_score = 0
while computer_score < 7 and student_score < 7:
    random_seed = random.choice(seed)
    student_main = input("Сделайте свой ход (камень\ножницы\бумага): ").lower().strip()

    if student_main not in seed:
        print("Пожалуйста, введите одно из трех: камень, ножницы или бумага")
        continue
    if student_main == random_seed:
        print(f"компьютер - ученик \n{random_seed} - {student_main}  \n{computer_score} - {student_score} (ничья)")
    elif(student_main == "камень" and random_seed == "ножницы") or \
        (student_main == "ножницы" and random_seed == "бумага") or \
        (student_main == "бумага" and random_seed == "камень"):
        student_score += 1
        print(f"компьютер - ученик \n{random_seed} - {student_main}  \n{computer_score} - {student_score}  (выиграл ученик)")
    else:
        computer_score += 1
        print(f"компьютер - ученик \n{random_seed} - {student_main}  \n{computer_score} - {student_score}  (выиграл компьютер)")

if computer_score == 7 or student_score == 7:
    print("Конец игры!")