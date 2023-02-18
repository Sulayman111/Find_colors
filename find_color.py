from random import choice

def select_colors():
    colors = ['r', 'b', 'o', 'y', 'p', 'g', 'w']
    color_1 = choice(colors)
    color_2 = choice(colors)
    color_3 = choice(colors)
    color_4 = choice(colors)
    print(f'{color_1}, {color_2}, {color_3}, {color_4}')
    data = (color_1, color_2, color_3, color_4)
    return data
def TryIt(color_1, color_2, color_3, color_4):
    print(f'colors: (r)ed, (b)lue, (o)range, (y)ellow, (p)ink, (g)reen, (w)hite')
    tryAgain = True
    while tryAgain:
        q1 = input('Guess the place (1): ').lower()
        if q1 != 'r' and q1 != 'b' and q1 != 'o' and q1 != 'y' and q1 != 'p' and q1 != 'g' and q1 != 'w':
            print('You did not guess')
        else:
            tryAgain = False

    tryAgain = True
    while tryAgain:
        q2 = input('Guess the place (2): ').lower()
        if q2 != 'r' and q2 != 'b' and q2 != 'o' and q2 != 'y' and q2 != 'p' and q2 != 'g' and q2 != 'w':
            print('You did not guess')
        else:
            tryAgain = False
    
    tryAgain = True
    while tryAgain:
        q3 = input('Guess the place (3): ').lower()
        if q3 != 'r' and q3 != 'b' and q3 != 'o' and q3 != 'y' and q3 != 'p' and q3 != 'g' and q3 != 'w':
            print('You did not guess')
        else:
            tryAgain = False

    tryAgain = True
    while tryAgain:
        q4 = input('Guess the place (4): ').lower()
        if q4 != 'r' and q4 != 'b' and q4 != 'o' and q4 != 'y' and q4 != 'p' and q4 != 'g' and q4 != 'w':
            print('You did not guess')
        else:
            tryAgain = False
    
    correct = 0
    incorrect = 0
    if color_1 == q1:
        correct += 1
    elif color_1 == q2 or color_1 == q3 or color_1 == q4:
        incorrect += 1
    
    if color_2 == q2:
        correct += 1
    elif color_2 == q1 or color_2 == q3 or color_2 == q4:
        incorrect += 1
    
    if color_3 == q3:
        correct += 1
    elif color_3 == q1 or color_3 == q2 or color_3 == q4:
        incorrect += 1
    
    if color_4 == q4:
        correct += 1
    elif color_4 == q1 or color_4 == q2 or color_4 == q3:
        incorrect += 1

    print(f'The right colors are in the right place {correct}')
    print(f'the right colors are not in the right place {incorrect}')
    print()
    data2 = [correct, incorrect]
    return data2
def main():
    (color_1, color_2, color_3, color_4) = select_colors()
    score = 0
    isPlay = True
    while isPlay:
        (correct, incorrect) = TryIt(color_1, color_2, color_3, color_4)
        score += 1
        if correct == 4:
            isPlay = False
        print('You win!')
        print(f'You have earned {score} score.')

if __name__ == '__main__':
    main()
