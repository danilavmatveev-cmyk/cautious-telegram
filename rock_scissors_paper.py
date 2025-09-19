import random
seed =['камень','ножницы',"бумага"]
random_seed = random.choice(seed)
student_main  = input("Сделайте свой ход (камень\ножницы\бумага): ")
i = 0
j = 0
while i <= 7 or j <= 7:
    if student_main == random_seed:
        i = i+0
        j = j+0
        print(f"компьютер - ученик \n{random_seed} - {student_main}  \n{i} - {j}, (ничья)")
    else:
        for random_seed in seed[0]:
            if student_main == "ножницы":
                i = i+1
                j = j+0
                print(f"компьютер - ученик \n{random_seed} - {student_main}  \n{i} - {j},  (выиграл компьютер)")
            elif student_main == "бумага":
                i = i+0
                j = j+1
                print(f"компьютер - ученик \n{random_seed} - {student_main}  \n{i} - {j},  (выиграл ученик)")
            else:
                print("Введите правильное слово!")

        for random_seed in seed[1]:
            if student_main == "бумага":
                i = i+1
                j = j+0
                print(f"компьютер - ученик \n{random_seed} - {student_main}  \n{i} - {j},  (выиграл компьютер)")
            elif student_main == "камень":
                i = i+0
                j = j+1
                print(f"компьютер - ученик \n{random_seed} - {student_main}  \n{i} - {j},  (выиграл ученик)")
            else:
                print("Введите правильное слово!")

        for random_seed in seed[2]:
            if student_main == "камень":
                i = i + 1
                j = j + 0
                print(f"компьютер - ученик \n{random_seed} - {student_main}  \n{i} - {j},  (выиграл компьютер)")
            elif student_main == "ножницы":
                i = i + 0
                j = j + 1
                print(f"компьютер - ученик \n{random_seed} - {student_main}  \n{i} - {j},  (выиграл ученик)")
            else:
                print("Введите правильное слово!")


