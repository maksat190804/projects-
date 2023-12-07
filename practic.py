# a = ['hola', 'lola', 'lara']
# a.remove(str('lola'))
# print(a)

# a = 40 
# b = 50 
# if a <= b:
#     print('error')
# elif a == b:
#     print('б больше а')
# else:
#     print("оба равны ")



# def is_isogram(string):
#     strong = string.lower()
#     for letter in string:
#         if string.count(letter) > 1:
#             return False
#         return True
    
def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True

    # char_dict = {}
    # string = string.lower()

    # for char in string:
    #     if char in char_dict:
    #         char_dict[char] = char_dict[char] + 1 
    #     else:
    #         char_dict[char] = 1 

    # for key in char_dict:
    #     if char_dict[key] > 1:
    #      return False 
    # return True 
    
