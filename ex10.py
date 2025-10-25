# python quiz game

questions = ('元素周期表里有多少种元素？：',
             '那种生物产的蛋最大？：',
             '地球上最丰富的气体是哪一种？：',
             '人体有多少块骨头？：',
             '太阳系里那颗星球最热？：')

options = (('A. 116', 'B. 117', 'C. 118', 'D. 119'),
           ('A. 企鹅', 'B. 鳄鱼', 'C. 鸡', 'D. 鸵鸟'),
           ('A. 氮气', 'B. 氧气', 'C. 氩气', 'D. 二氧化碳'),
           ('A. 206', 'B. 205', 'C. 207', 'D. 208'),
           ('A. 水星', 'B. 金星', 'C. 火星', 'D. 木星'))

answers = ('C', 'D', 'A', 'A', 'B')
guesses = []
score = 0
question_num = 0

for question in questions:
    print('---------------------------')
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input('Enter (A, B, C, D):').upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print('正确！')
    else:
        print('错误！')
        print(f'{answers[question_num]} is the right answer.')
    question_num += 1

print('----------------')
print('    RESULTS     ')
print('----------------')

print('answers: ', end=' ')
for answer in answers:
    print(answer, end=' ')
print()
print('guesses: ', end=' ')
for guess in guesses:
    print(guess, end=' ')
print()


score = int(score / len(questions) * 100)
print(f'Your score is: {score} %.')
