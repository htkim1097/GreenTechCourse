# 재귀 함수
def factorial(n):
    output = 1
    for i in range(1, n + 1):
        output *= i

    return output

print(f"1!:", factorial(1))
print(f"1!:", factorial(2))
print(f"1!:", factorial(3))
print(f"1!:", factorial(4))

