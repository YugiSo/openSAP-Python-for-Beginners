# Week 4 - Bonus Assignment

with open('Week_04/Bonus/player1.txt') as f1:
    p1 = f1.read().split('\n')[:-1]

with open('Week_04/Bonus/player2.txt') as f2:
    p2 = f2.read().split('\n')[:-1]

p1_win, p2_win, draw = 0, 0, 0

for move1, move2 in zip(p1, p2):
    
    if move1 == move2:
        draw = draw + 1

    elif (move1 == 'R' and move2 == 'S') or (move1 == 'P' and move2 == 'R') or (move1 == 'S' and move2 == 'P'):
        p1_win += 1
    
    else:
        p2_win += 1

# print(p1_win, p2_win, draw)

result = f'''Player1 wins: {p1_win}
Player2 wins: {p2_win}
Draws: {draw}'''

with open('Week_04/Bonus/result.txt', 'w') as file:
    file.write(result)