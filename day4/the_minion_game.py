def minion_game(string):
    stuart=0
    kevin=0
    for i in range(len(string)):
        if string[i]=='A' or string[i]=='E' or string[i]=='I' or string[i]=='O' or string[i]=='U':
            kevin+= len(string)-i
        else:
            stuart+= len(string)-i
    if stuart == kevin:
        print("Draw")
    elif kevin>stuart:
        print("Kevin " +str(kevin))
    else:
        print("Stuart " +str(stuart))
             

if __name__ == '__main__':
    s = input()
    minion_game(s)