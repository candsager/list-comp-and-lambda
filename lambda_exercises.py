#SHort term function
#only contains a single expression, but can take several arugments
#creates a function object when assigned to a a variable
#
''' 1)
Write a Python program to filter a list of integers using Lambda. Go to the editor
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]
'''
org_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = list(filter(lambda num: num % 2 ==0,org_int))
print(even_list)

odd_list = list(filter(lambda num: num % 2 !=0, org_int))
print(odd_list)


''' 2)
find which days of the week have exactly 6 characters.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

count_char = list(map(lambda i: len(i) == 6, weekdays))
print(count_char)




''' 3)
remove specific words from a given list 
Original list:
['orange', 'red', 'green', 'blue', 'white', 'black']

Remove words:
['orange', 'black']

After removing the specified words from the said list:
['red', 'green', 'blue', 'white']

'''

org_color = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_words = ['orange', 'black']

new_list = list(filter(lambda x: x not in remove_words, org_color))
print(new_list)



''' 4)
 remove all elements from a given list present in another list
Original lists:
list1: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2: [2, 4, 6, 8]

Remove all elements from 'list1' present in 'list2:
[1, 3, 5, 7, 9, 10]
 '''
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

remove_list = list(filter(lambda x: x not in list2, list1))
print(remove_list)


''' 5)
find the elements of a given list of strings that contain specific substring using lambda
Original list:
['red', 'black', 'white', 'green', 'orange']
Substring to search:
ack
Elements of the said list that contain specific substring:
['black']
Substring to search:
abc
Elements of the said list that contain specific substring:
[]

'''
og_list = ['red', 'black', 'white', 'green', 'orange']
substring1 = 'ack'
substring2 = 'abc'

the_list = list(filter(lambda p: substring1 in p, og_list))
print(the_list)

second_list = list(filter(lambda o: substring2 in o, og_list))
print(second_list)


''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

str1 = "Hello8world" #Should pass
#str1 = "HELLO" #Should fail
#str1= "hello" #Should fail

contains_upper = (lambda s: any(char.isupper() for char in s))
contains_lower = (lambda s: any(char.islower() for char in s))
contains_digit = (lambda s: any(char.isdigit() for char in s))
has_min_length = (lambda s: len(s) >= 8)

password_check = all([contains_upper(str1),contains_lower(str1),contains_digit(str1),has_min_length(str1)])

print(password_check)


''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''

org_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

sorted_scores = sorted(org_scores, key=lambda x: x[1])
print(sorted_scores)