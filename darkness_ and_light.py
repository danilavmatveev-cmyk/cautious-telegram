letter = ["С","Т"]
seq = []
import random
for i in range(5):
    random_letter = random.choice(letter)
    seq.append(random_letter)
    result_seq = "".join(seq)
def check(seq: str) -> str:
    while True:
        student = input("Введите энергию (Свет/Тьма): ").lower().strip()
        if student == "свет" or student == "тьма":
            res = seq.count("С")
            if (res >= 3 and student == "свет") or (res < 3 and student == "тьма"):
                print(f'Последовательность из 5 кристаллов: {result_seq}\nПадаван достоин звания "Рыцаря-джедая"!')
            else:
                print(f"Последовательность из 5 кристаллов: {result_seq}\nПадаван остаётся на дополнительное обучение...")
            break
        else:
            print("Ошибка! Введите либо свет, либо тьма!")
            

check(result_seq)




