# def solution(s):
#
#     words = s.split(" ")
#     result = []
#
#     for word in words:
#         new_word = ''
#
#         for idx, abc in enumerate(word):
#             if idx % 2 == 0:
#                 new_word += abc.upper()
#             else:
#                 new_word += abc.lower()
#
#         result.append(new_word)
#
#     return " ".join(result)



def solution(s):
    idx = 0
    new_str = ''

    for char in s:
        if char == ' ':
            new_str += char
            continue

        elif idx % 2:
            new_str += char.lower()

        elif idx % 2 == 0:
            new_str += char.upper()

        idx += 1

    return(new_str)

print(solution("try hello world")) # "TrY HeLlO WoRlD"