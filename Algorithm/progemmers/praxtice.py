# def up_and_low(chars):
#
#     new_text = ''
#     for idx, char in enumerate(chars):
#         if idx % 2:
#             new_text += char.upper()
#
#         else:
#             new_text += char.lower()
#
#
#     return new_text
#
#
#
# print(up_and_low('appleppie')) # aPpLePiE
# print(up_and_low('spaceship')) # sPaCeShIp

def passpass(scores):
    scores = list(scores.items())
    print(scores)

    good_scores = []

    for score in scores:
        if score[1] >= 60:
            good_scores.append(score)

    good_scores.sort(key=lambda elem: elem[1], reverse=True)

    answers = []

    for subj, score in good_scores:
        answers.append(subj)

    print(answers)


print(passpass({'Java': 10, 'Ruby': 80, 'Python': 74, 'C': 88})) #=> ['Ruby', 'Python']