def find_max(numbers):
    max_val = numbers[0]
    for i in range(len(numbers)):
        if numbers[i] > max_val:
            max_val = numbers[i]
    return max_val
print(find_max([3, 7, 2, 9, 5]))
