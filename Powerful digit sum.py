def digit_sum(number):
    return sum(map(int, str(number)))

def max_digital_sum(n):
    max_sum = 0
    for a in range(1, n):
        for b in range(1, n):
            max_sum = max(max_sum, digit_sum(a**b))
    return max_sum


n = int(input())
print(max_digital_sum(n))
