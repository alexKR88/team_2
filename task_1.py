while True:
    if True:
        a = int(input("Введите начало диапазона: "))
        b = int(input("Введите конец диапазона: "))

        prime_numbers = []

        for num in range(a, b + 1):
            if num > 1:
                is_prime = True

                for i in range(2, int(
                        num ** 0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_numbers.append(num)

        print("Простые числа в диапазоне:", prime_numbers)
    else:
        print("Некоректные данные!")
