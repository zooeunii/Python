number = [1, 5, 4, 9, 3, 2, 6]
number.sort()   #오름차순으로 정리
print(number)
number.sort(reverse=True)   #내림차순으로 정리
print(number)

number2 = sorted(number)
number3 = sorted(number, reverse=True)
print(f"number: {number}")
print(f"number2: {number2}")
print(f"number3: {number3}")