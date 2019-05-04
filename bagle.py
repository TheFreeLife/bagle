from random import shuffle

CM = 3 # 1 이상으로 할 것
AGAIN = 10

def RandomNum(CM): 
    wor = []
    a = list(range(10))
    shuffle(a)
    for i in range(CM):
        wor.append(str(a[i]))
    return wor

def MakeAnotherNumList(guess, i):
    IsCtrlv = []
    if len(guess) == 1:
        IsCtrlv = []
    elif guess[i] == 0:
        IsCtrlv = guess[i+1:]
    elif guess[i] == CM-1:
        IsCtrlv = guess[:i]
    else:
        IsCtrlv = guess[:i] + guess[i+1:]
    return IsCtrlv


def plays(CM, guess):
    a = 0
    g = list(guess)
    for i in range(len(guess)):
        if g[i] in '1 2 3 4 5 6 7 8 9 0':
            a += 1
    if a == len(guess):
        return True
    else:
        return False

def Checking(guess, word1, i, CM):
    finish = True
    for j in range(i+1, CM):
        if guess[j] == word1[j]:
            finish = False
            break
        else:
            finish = True
    if guess[i] in guess[:i]:
        anotherfinish = False
    else:
        anotherfinish = True
    return finish, anotherfinish
    
def Judge(guess,word1,CM): #입력된 숫자를 다음과 같은 식으로 판단한다.
    a = []
    p = 0
    UsedWord = []
    CheckNum = True
    if guess == word1:
        print('당신이 이겼네요!')
        return False

    for i in range(CM): 
        CheckNum, AnotherCheck = Checking(guess, word1, i, CM)
        Ctrlv = MakeAnotherNumList(guess, i)
        if guess[i] == word1[i]:
            a.append('안타')
        elif guess[i] in word1 and CheckNum and AnotherCheck:
            a.append('파울')
        elif guess[i] not in word1 or guess[i] in Ctrlv:
            a.append('스트라이크')
                 
    a.sort()
    return a

print ('개발 버전입니다.')
print ('베이글 세계에 오신것을 환영합니다.')
print ('저는 숫자 {0}자리를 생각합니다.'.format(CM))
print ('그러면 당신은 그 숫자를 맞히시면 됩니다. (기회는 10번)')
print ('포함되어 있다:파울,완벽히 틀렸다:스트라이크, 자리까지 맞다:안타')


if CM > 0:
    while True:
        a = 1
        heart = AGAIN
        word1 = RandomNum(CM)
        print(word1)
        y = 0
        while a == 1 and heart > y:
            guess = ''
            while len(guess) != CM or not plays(CM,guess):
                guess = input('입력하세요')            
            guess = list(guess)
            got = Judge(guess, word1, CM)
            if got == False:
                break
            print (got)
            y += 1

        print("정답은" + str(word1)+ "이였습니다.")
        gu = input('다시 하겟습니까?').lower().startswith('y')
        if not gu:
            break
else:
    print('이 게임의 랜덤 숫자 길이는 적어도 1 이상이어야 합니다.')
        
