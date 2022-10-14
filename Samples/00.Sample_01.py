import random

random_number = random.randint(1,100)
# print(random_number)

game_number = 1

while True:

    try:

        my_number = int(input('1-100 사이 숫자를 입력하세요.'))

        if my_number > random_number:
            print('Down!!')
        elif my_number < random_number:
            print('Up!!')
        else:
            print(f'Correct!! Congratulation^^ {game_number}번만에 맞추셨습니다~')
            break
    
        game_number = game_number + 1

    except:

        print('숫자를 입력해주세요.')

        

