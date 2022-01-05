import random
ALFABET=('a','ą','b','c','ć','d','e','ę','f','g','h','i','j','k','l','ł','m','n','ń','o','ó','p','r','s','ś','t','u','w','y','z','ź','ż')
wyraz=('kasztanowiec',
        'meteoryt',
        'dinozaur',
        'gitara',
        'gramofon',
        'książka',
        'komputer',
        'klawiatura',
        'głośniki',
        )
w=len(wyraz)
w2=random.randrange(w)
hasło=wyraz[w2]
d=len(hasło)
d2=d-1
A=d2
lista=[]
podłoga='_'
próba=5  
odpowiedź=''
print('wyraz ma',d,'liter')
while d!=0:
    d-=1
    lista+=podłoga
print(lista)
print
litera=str(input("Twoja litera to?:\n"))
litera=litera.lower()



while True:
    if litera == hasło:
        print('\nGratulacje udało Ci się!')
        break
    elif litera in hasło and próba>=0 and len(litera)==1:
        if litera==hasło[d2]:
            lista[d2]=litera
            d2-=1
            if d2<0:
                próba-=1
                print('\nTwoja litera znajduję się w wyrazie')
                print(lista)
                print('\npozostała ilość podpowiedzi:', próba)
                d2=A
                if próba==0:
                    print('\nTwoja ostateczna odpowiedź to?', '\n')
                    odpowiedź=str(input())
                    odpowiedź=odpowiedź.lower()
                    if odpowiedź==hasło:
                        print('\nGratulacje udało Ci się!')
                        break
                    else:
                        print('\nNie tym razem :(')
                        print('\nPoprawda odpowiedź to: ',hasło)
                        break
                litera=str(input("\nTwoja litera to?:\n"))
                litera=litera.lower()
        elif litera!=hasło[d2]:
            d2-=1
    elif litera not in ALFABET: 
        print("To nie jest litera!")
        litera=str(input("Twoja litera to?:\n"))      
    elif litera not in hasło and próba>=0 and len(litera)==1:
        print('\nlitera nie znajduję się w wyrazie')
        print(lista)
        próba-=1
        print('\npozostała ilość podpowiedzi:', próba)
        if próba==0:
            print('\nTwoja ostateczna odpowiedź to?''\n')
            odpowiedź=str(input())
            odpowiedź=odpowiedź.lower()
            if odpowiedź==hasło:
                print('\nGratulacje udało Ci się!')
                break
            else:
                 print('\nNie tym razem :(')
                 print('\nPoprawda odpowiedź to: ',hasło)
                 break
        litera=str(input("\nTwoja litera to?:\n"))
        litera=litera.lower()
    elif len(litera)!=0 and próba>=0:
        print('\nPodałeś więcej niż jedną literę!')
        litera=str(input("\nTwoja litera to?:\n"))
        litera=litera.lower()
input('\n\nNaciśnij enter aby zakończyć program')

