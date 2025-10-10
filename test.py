def one_two_three(current, target, memo=None):
    if memo is None:
        memo = {}

    # Проверяем, не вычисляли ли мы уже этот случай
    if (current, target) in memo:
        return memo[(current, target)]

    # Базовые случаи
    if current == target:
        return 1
    if current > target:
        return 0
    if current == 33:
        return 0

    # Рекурсивно вычисляем количество путей
    result = (one_two_three(current + 1, target, memo) +
              one_two_three(current * 2, target, memo) +
              one_two_three(current * 3, target, memo))

    # Сохраняем результат в мемо для повторного использования
    memo[(current, target)] = result
    return result
print(one_two_three(2, 50))

