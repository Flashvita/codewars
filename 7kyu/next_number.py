"""Task by solution factories
Return next number
Example:
    arr = [1, 5] => 15 + 1 = 16
    return [1, 6]
"""


def next_number(arr: list) -> list[int]:
    return [int(i) for i in f"{int(''.join(map(str, arr))) +1}"]

print(next_number([1, 9]))
print(next_number([9, 9, 8, 2]))
print(next_number([3, 9, 2]))
print(next_number([1, 8, 9]))