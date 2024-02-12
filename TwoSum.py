def twoSum(nums, target):
    numbers = [x for x in nums if x < target]
    output = []
    out = False
    sub = numbers[1:]
    for number in numbers:
        for index, rest in enumerate(sub):
            if number + rest == target:
                output.append(numbers.index(number))
                output.append(index)
                out = True
                break
        if len(sub) != 0:
            sub.pop(0)
        if out:
            break
    return output


output1 = twoSum([3,3], 6)
print(output1)
