def init()->str:
    while True:
        s=input()
        if s.count(')')==s.count('('):
            return s
        print('Данные введены не коректно')
def decoder(s:str)->None:
    while True:
        for e, x in enumerate(s):
            if x==')':
                for y in range(e-1,-1,-1):
                    if s[y]=='(':
                        b=y
                        break
                temp=s[b:e+1].replace('(','')
                temp=temp.replace(')','')
                if s[b+1].isdigit():
                    temp=temp[1:]*int(temp[0])
                if s[b-1].isdigit():
                    b=b-1
                    temp=temp*int(temp[b])
                s=s[:b]+temp+s[e+1:]
                break
        if s.count(')')==0:
            break
    print(s)
if __name__=='__main__':
    s=init()
    decoder(s)