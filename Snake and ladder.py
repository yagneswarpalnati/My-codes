import random as r
print("snake and ladder")
print("AS YOU CAN'T CHOOSE THE DICE NUMBER\n****YOU CAN CHOOSE THE NUMBER OF SHUFFLES---\nPLEASE GO THROW")


def sandl(n):
    print("DO WANT TO PLACE SNAKE AND LADDER:\nenter YES OR NO")
    sl = input()
    if sl == "YES":
        print("how many snakes and ladders:")
        sn = int(input())
        s = []
        l = []
        for i in range(sn):
            num = int(input("please where to insert snake:"))
            s.append(num)
        for i in range(sn):
            num = int(input("please enter where to insert ladder:"))
            l.append(num)
        findsandl(n, s, l)
    else:
        s = [25, 45, 67, 89, 99]
        l = [35, 89, 69, 15, 70]
        findsandl(n, s, l)
    d = [1, 2, 3, 4, 5, 6]
    y = 0
    c = 0
    while c <= 100 and y <= 100:
        for i in range(10):
            for j in range(10):
                print('|', str(n[i][j]).rjust(3), '|', end='')
            print()
        n1 = int(input("No of times to shuffle the dice:"))
        for i in range(n1):
            r.shuffle(d)
        k = r.choice(d)
        print("you're number is :", k)
        if y+k > 100:
            pass
        elif y+k == 100:
            print("congratulations,you won buddy")
            break
        else:
            y += k
        if y in l:
            print("you have a ladder(+5)")
            y += 5
        elif y in s:
            print("you hitted by a snake(-5)")
            y -= 5
        print("you're current board position:", y)
        k1 = r.choice(d)
        print("computer number is:", k1)
        if c+k1 > 100:
            pass
        elif c+k1 == 100:
            print("computer won !!!,better luck next time!!!")
            break
        else:
            c += k1
        if c in l:
            print("computer has a ladder(+5)")
            c += 5
        elif c in s:
            print("computer was hitted by a snake")
            c -= 5
        print("computer current board position is:", c)


def findsandl(n, s, l):
    for i in range(10):
        for j in range(10):
            for k in range(len(s)):
                if n[i][j] == s[k]:
                    n[i][j] = "$$"
            for k in range(len(l)):
                if n[i][j] == l[k]:
                    n[i][j] = "LL"


n = []
k = 1
for i in range(10):
    m = []
    if i % 2 == 0:
        for j in range(10):
            m.append(k)
            k += 1
        n.append(m)
    else:
        for l in range(10):
            m.append(k)
            k += 1
        m.reverse()
        n.append(m)
n.reverse()
sandl(n)
