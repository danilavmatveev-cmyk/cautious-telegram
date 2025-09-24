letter = ["С","Т"]
seq = []
import random
for i in range(5):
    random_letter = random.choice(letter)
    seq.append(random_letter)
def check(seq: str) -> str:
    student = input("Введите энергию (Свет/Тьма): ").lower().strip()
    res = seq.count ("С")
    if (res >= 3 and student == "свет") or (res < 3 and student == "тьма"):
        print('Падаван достоин звания "Рыцаря-джедая"!')
    else:
        print("Падаван остаётся на дополнительное обучение...")
check(seq)




