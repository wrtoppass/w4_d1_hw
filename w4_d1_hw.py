# 1 Codewars answer 6kyu
def parse(data):
    value = 0               #O(1)
    output = []             #O(1)
    for char in data:       #O(N)
        if char == 'i':     #O(1)
            value += 1      #O(1)
        elif char == 'd':   #O(1)
            value -= 1      #O(1)
        elif char == 's':   #O(1)
            value *= value  #O(1)
        elif char == 'o':   #O(1)
            output.append(value) #O(1)
        else:               #O(1)
            continue        #O(1)
    return output           #O(1)

#O(N) Linear 


# 2 Codewars answer 7kyu
def count_vowels(sentence):
    vowels = "aeiou"             #O(1)
    count = 0                    #O(1)
    for char in sentence:        #O(N)
        if char in vowels:       #O(1)
            count += 1           #O(1)
    return count                 #O(1)

#O(N) Linear



# 3 Codewars answer 5kyu
def dirReduc(arr):
    opposites = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST'
    }                            #O(1)
    stack = []
    for direction in arr:        #O(N)
        if stack and opposites[direction] == stack[-1]:    #O(N)
            stack.pop()
        else:
            stack.append(direction)
    return stack

#O(N^2) Quadratic 