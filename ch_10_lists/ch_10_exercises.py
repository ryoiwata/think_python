import timeit
import time 

def nested_sum(input_list_of_list):
    #exercise 10-1
    local_list = input_list_of_list
    for index, value in enumerate(local_list):
        local_list[index] = sum(value)
    return sum(local_list)

def cum_sum(input_list):
    #exercise 10-2
    local_list = input_list
    current_sum = 0
    for index, value in enumerate(local_list):
        current_sum += value
        local_list[index] = current_sum
    return local_list

def middle(input_list):
    #exercise 10-3
    if len(input_list) <= 2:
        return input_list
    else:
        return input_list[1:-1]

def chop(input_list):
    #exercise 10-4
    if len(input_list) >= 3:
        del input_list[0]
        del input_list[-1]

def is_sorted(input_list):
    #exercise 10-5
    return input_list == sorted(input_list)

def is_anagram(input_string_1, input_string_2):
    #exercise 10-6
    return sorted(list(input_string_1)) == sorted(list(input_string_2))

def has_duplicates(input_list):
    #exercise 10-7
    return len(input_list) != len(set(input_list))

def birthday(number_of_students, number_of_iterations):
    #exercise 10-8

    import numpy as np
    iteration = 0
    shared_birthday = 0
    while iteration < number_of_iterations:
        iteration += 1
        random_birthdays = np.random.randint(low = 1, high = 366, size=number_of_students)
        if len(random_birthdays) != len(np.unique(random_birthdays)):        
            shared_birthday += 1
        """ #code for if you want to see liklyhood that you have a shared birthday
        my_birthday = random.randint(1,365)
        if my_birthday in random_birthdays:
            shared_birthday += 1"""
    return shared_birthday / number_of_iterations

def file_to_string_list_append(file_name):
    #exercise 10-9
    file_obj = open(file_name, "r")
    file_iteration = file_obj.readlines()
    word_list = []
    counter = 0 
    for line in file_iteration:
        split_line = line.split()
        for word in split_line:
            word_list.append(word)
        if counter >= 10000:
            break
        counter += 1
    file_obj.close()
    return word_list

def file_to_string_list_addition(file_name):
    #exercise 10-9
    file_obj = open(file_name, "r")
    file_iteration = file_obj.readlines()
    word_list = []
    counter = 0 
    for line in file_iteration:
        split_line = line.split()
        for word in split_line:
            word_list += [word]
        if counter >= 10000:
            break
        counter += 1
    file_obj.close()
    return word_list

def in_bisect(input_sorted_list, target_value):
    bisected_list = input_sorted_list
    while len(bisected_list) > 1:
        midway_point = len(bisected_list) // 2
        if target_value > bisected_list[midway_point]: 
            bisected_list = bisected_list[midway_point + 1:]
        elif target_value < bisected_list[midway_point]:
            bisected_list = bisected_list[:midway_point]
        else:
            return input_sorted_list.index(target_value)
    print(bisected_list)
    return None

def reverse_pair(input_word_list):
    for word in input_word_list:
        print(word)


#exercise 10-1
# t = [[1,2], [3], [4,5,6]]
# print(nested_sum(t))

#exercise 10-2
# t = [1,2,3]
# print(cum_sum(t))

#exercise 10-3
# t = [1,2,4,3]
# print(middle(t))

#exercise 10-4
# t = [1,2,4,5,3]
# chop(t)
# print(t)

#exercise 10-5
# print(is_sorted([1,2,2]))
# print(is_sorted(['b','a']))

#exercise 10-6
# print(is_anagram("hello", "ello"))
# print(is_anagram("hello", "elloh"))

#exercise 10-7
# print(has_duplicates([1,1,0]))
# print(has_duplicates([0,1,2]))

#exercise 10-8
# print(birthday(15, 1000))

#exercise 10-9
# start = time.time()
# print(file_to_string_list_append("odyssey.txt"))
# end = time.time()
# print(end - start)
## 0.11170220375061035

# start = time.time()
# print(file_to_string_list_addition("odyssey.txt"))
# end = time.time()
# print(end - start)
## 0.13565564155578613 

#exercise 10-10
# import random
# random_numbers = random.sample(range(1, 1000000000), 1000000)
# random_numbers.sort()

# start = time.time()
# print(in_bisect(random_numbers, 500000000))
# end = time.time()
# print(end - start)
# #this is faster if you get into really big numbers

# start = time.time()
# print(500000000 in random_numbers)
# end = time.time()
# print(end - start)

#exercise 10-11
word_list = ["bat", "cat", "tab"]
print(reverse_pair(word_list))
