import millionaire_data

guesses = []
question_number, prize, guarantee = 0, 0, 0

game = True

name = input('Welcome to “Who Wants to Be a Millionaire?”. What is your name? ')
print('Before you is 15 questions, prizes from $100 all way up to $1.000.000.\n'
      'There are four threshold: $100, $1.000, $32.000 and of course $1.000.000.\n'
      f'Good luck {name}!')

def guaranteeprize(guarantee):
    if guarantee == 1:
        print(f'Congratulations! You won guaranteed {millionaire_data.prizes[0]}')
    elif guarantee == 2:
        print(f'Congratulations! You won guaranteed {millionaire_data.prizes[4]}')
    elif guarantee == 3:
        print(f'Congratulations! You won guaranteed {millionaire_data.prizes[9]}')

while game:
    for i in range(15):
        print(f'Question number {i+1} for {millionaire_data.prizes[i]}')
        if i == 0 or i == 4 or i == 9 or i == 14:
            print('This question is a threshold and prize is guaranteed')
        print(millionaire_data.questions[i])
        for j in range(4):
            print(millionaire_data.options[i][j])
        guesses += input('Your answer: ').lower()
        if i == 14:
            print('Congratulations! You won $1.000.000\n'
                  f'{name} you are first to win such a prize!')
            game = False
            break
        if guesses[i] == millionaire_data.correct[i]:
            prize += 1
            if prize == 1 or prize == 5 or prize == 10:
                guarantee += 1
        else:
            print(f'Sorry but this answer is wrong. Correct one is {millionaire_data.correct[i].capitalize()}')
            guaranteeprize(guarantee)
            game = False
            break
