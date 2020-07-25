import random

# allows user to create a set of numbers, at their desiered length
setSize = int(input('How many numbers are we sorting today?'))
# creates a random list of numbers between 0 and 999,999
numbers = random.sample(range(0, 999999), setSize)


def sort (arr, a, b, i, j):
    while j < a:
        while i < a:
            if arr[b] > arr[i]:
                b = i
            i += 1
        arr[j], arr[b] = arr[b], arr[j]
        j += 1
        i = j
        b = i

sort(numbers, setSize, 0, 0, 0)


print('The sorted set is')
for i in range(setSize):
    print(str(numbers[i]))