import random
def choose():
    words=['orange','kiwi','peach', 'banana', 'figure', 'nectarine', 'grape', 'plastic', 'apple', 'apricot', 'mango', 'datesheet', 'cherry', 'guava', 'papaya']
    pick = random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,'your score is:',p1)
    print(p2n,'your score is:',p2)
    print('Thank you for playing,bye')


def play():
    p1name=input('Player 1, name:')
    p2name=input('Player 2, name:')
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if turn%2==0:
            print(p1name,'your turn')
            ans=input('what do you think?:')
            if ans==picked_word:
                pp1=pp1+1
                print('correct')
                print('point is',pp1)
            else:
                print('incorrect,word is:',picked_word)
                print('point is',pp1)
                c= input('Press 1 to continue, 0 to stop:')
                if c==0:
                    thank(p1name,p2name,pp1,pp2)
                    break
        else:
            print(p2name,'your turn')
            ans=input('what do you think?:')
            if ans==picked_word:
                pp2=pp2+1
                print('correct')
                print('point is',pp2)
            else:
                print('incorrect,word is:',picked_word)
                print('point is',pp2)
                
        c = input('Press 1 to continue, 0 to stop: ')
        if c == '0':
            thank(p1name, p2name, pp1, pp2)
            break
            turn+=1
play()
            
    