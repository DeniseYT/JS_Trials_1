"""Python functions for JavaScript Trials 1."""

# // Print each item in the given array.
# //
# // Ex.:
# //   > output_all_items([1, 'hello', True]);
# //   1
# //   hello
# //   True
def output_all_items(items):
    for item in items:
        print(item)

def get_all_evens(nums):
    a_list =[]

    for num in nums:
        if num % 2 == 0:
            a_list.append(num)
    
    return a_list

print(get_all_evens([7, 8, 10, 1, 2, 2]))


def get_odd_indices(items):
    results = []
    for i in range(1,len(items),2):
        results.append(items[i])
    return results


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f"{i}, {item}")
        i += 1
    


def get_range(start, stop):
    result = []
    for i in range(start, stop):
        result.append(i)
    return result


def censor_vowels(word):
    chars = []
    for letter in word:
        if letter in "aeiou":
            chars.append("*")
        else:
            chars.append(letter)
    
    return "".join(chars)
        


def snake_to_camel(string):
    camel_case = []

    for word in string.split('_'):
        camel_case.append(word[0].upper()+word[1:])
    
    return ''.join(camel_case)


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)
    
    return longest


def truncate(string):
    result = []

    for char in string:
        if len(result) == 0 or result[-1] != char:
            result.append(char)
    
    return "".join(result)


def has_balanced_parens(string):
    front_parens = 0
    back_parens = 0

    for char in string:
        if char == '(':
            front_parens += 1
        elif char == ')':
            back_parens += 1
        
    if front_parens == back_parens:
        return True
    else:
        return False
        




# def compress(string):
#     result = []

#     current_char = string[0]
#     count = 0

#     for char in string:
#         if char != current_char:            
            
#             current_char = char
#             count += 1
            
        
#         else:
#             count += 1












