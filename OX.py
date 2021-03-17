#排出遊戲的九宮格
theBoard={'top_L':' ','top_M':' ','top_R':' ',
	      'mid_L':' ','mid_M':' ','mid_R':' ',
	      'bot_L':' ','bot_M':' ','bot_R':' '}

def printBoard(board):
    print(board['top_L']+'|'+board['top_M']+'|'+board['top_R'])
    print('-+-+-')
    print(f"{board['mid_L']}|{board['mid_M']}|{board['mid_R']}")
    print('-+-+-')
    print("{0}|{1}|{2}".format(board['bot_L'],board['bot_M'],board['bot_R']))

#將九宮格中的數字改為1~9
def ntob(num):
    li=['top_L','top_M','top_R',
        'mid_L','mid_M','mid_R',
        'bot_L','bot_M','bot_R']
    return li[num-1]

#判斷是否為正常輸入
def vinput(input):
    try:
        temp=int(input)
        return True
    except:
        return False

#遊戲過程
turn='X'

for i in range (9):
    printBoard(theBoard)
    print(f'turn for {turn}.Move on which space?')
    move=input()

#是否輸入錯誤
    while True:
        if not vinput(move):
            print(f'錯誤，請再輸入一次')
            move=input()
            continue
        if int(move)>0 and int(move)<10:
            if theBoard[ntob(int(move))]==' ':
                break
            else:
                print(f'錯誤，請再輸入一次')
                move=input()
        else:
            print(f'錯誤，請再輸入一次')        
            move=input()

#轉換回合
    theBoard[ntob(int(move))]=turn
    if turn=='X':
        turn ='O'
    else:
        turn ='X'

printBoard(theBoard)