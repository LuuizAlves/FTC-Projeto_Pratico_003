palavra = input()

p = []
for i in range(len(palavra)):
    p.append(palavra[i])
c = 0
p2 = []
p3 = []
p4 = []
p5 = []
res = "REJEITA"
p.append("\0")


def q0():
    global c
    global res

    if p[c] == "1":
        c = c + 1
        p3.append("1")
        p5.append("0")
        q1()
    else:
        if p[c] == "0":
            c = c + 1
            p3.append("0")
            p5.append("0")
            q1()
        else:
            if p[c] == "+":
                c = c + 1
                q2()
            else:
                res = "REJEITA"

def q1():
    global c
    global res

    if p[c] == "1":
        c = c + 1
        p3.append("1")
        p5.append("0")
        q0()
    else:
        if p[c] == "0":
            c = c + 1
            p3.append("0")
            p5.append("0")
            q0()
        else:
            if p[c] == "+":
                c = c + 1
                q2()
            else:
                res = "REJEITA"

def q2():
    global c
    global res

    if p[c] == "1":
        c = c + 1
        p2.append("1")
        p4.append("0")
        q3()
    else:
        if p[c] == "0":
            c = c + 1
            p2.append("0")
            p4.append("0")
            q3()
        else:
            if p[c] == "\0":
                c = c - 1

                tamp4 = len(p4)
                tamp5 = len(p5)

                if tamp4 > tamp5:
                    #p2.insert(0, "\0")
                    q4()
                else:
                    if tamp5 >= tamp4:
                        #p2.insert(0, "\0")
                        q5()
            else:
                res = "REJEITA"


def q3():
    global c
    global res

    if p[c] == "1":
        c = c + 1
        p2.append("1")
        p4.append("0")
        q2()
    else:
        if p[c] == "0":
            c = c + 1
            p2.append("0")
            p4.append("0")
            q2()
        else:
            if p[c] == "\0":
                c = c - 1

                tamp4 = len(p4)
                tamp5 = len(p5)

                if tamp4 > tamp5:
                    #p2.insert(0, "\0")
                    q4()
                else:
                    if tamp5 >= tamp4:
                        #p2.insert(0, "\0")
                        q5()
            else:
                res = "REJEITA"

def q4():
    x = len(p2)
    x = x - 1
    y = len(p3)
    y = y - 1
    z = len(p4)
    z = z - 1

    while x >= 0:
        while y >= 0:
            um = p2[x]
            tres = p4[z]
            dois = p3[y]
            if um == "1" and dois == "1" and tres == "0":  # 110
                p4[z] = "0"
                if z == 0:
                    p4.insert(0, "1")
                elif z != 0:
                    p4[z - 1] = "1"
            else:
                if um == "0" and dois == "0" and tres == "0":  # 000
                    p4[z] = "0"
                else:
                    if um == "1" and dois == "0" and tres == "0":  # 100
                        p4[z] = "1"
                    else:
                        if um == "0" and dois == "1" and tres == "0":  # 010
                            p4[z] = "1"
                        else:
                            if um == "1" and dois == "1" and tres == "1":  # 111
                                p4[z] = "1"
                                if z == 0:
                                    p4.insert(0, "1")
                                elif z != 0:
                                    p4[z - 1] = "1"
                            else:
                                if um == "0" and dois == "0" and tres == "1":  # 001
                                    p4[z] = "1"
                                else:
                                    if um == "1" and dois == "0" and tres == "1":  # 101
                                        p4[z] = "0"
                                        if z == 0:
                                            p4.insert(0, "1")
                                        elif z != 0:
                                            p4[z - 1] = "1"
                                    else:
                                        if um == "0" and dois == "1" and tres == "1":  # 011
                                            p4[z] = "0"
                                            if z == 0:
                                                p4.insert(0, "1")
                                            elif z != 0:
                                                p4[z - 1] = "1"
            y = y - 1
            x = x - 1
            z = z - 1

        um = p2[x]
        tres = p4[z]
        if um == "1" and tres == "0":
            p4[z] = "1"
        else:
            if um == "0" and tres == "0":
                p4[z] = "0"
            else:
                if um == "1" and tres == "1":
                    p4[z] = "0"
                    if z == 0:
                        p4.insert(0, "1")
                    elif z != 0:
                        p4[z - 1] = "1"
                else:
                    if um == "0" and tres == "1":
                        p4[z] = "1"
        x = x - 1
        z = z - 1
    q6()

def q5():
    x = len(p3)
    x = x - 1
    y = len(p2)
    y = y - 1
    z = len(p5)
    z = z - 1

    while x >= 0:
        while y >= 0:
            um = p3[x]
            tres = p5[z]
            dois = p2[y]
            if um == "1" and dois == "1" and tres == "0":  # 110
                p5[z] = "0"
                if z == 0:
                    p5.insert(0, "1")
                elif z != 0:
                    p5[z - 1] = "1"
            else:
                if um == "0" and dois == "0" and tres == "0":  # 000
                    p5[z] = "0"
                else:
                    if um == "1" and dois == "0" and tres == "0":  # 100
                        p5[z] = "1"
                    else:
                        if um == "0" and dois == "1" and tres == "0":  # 010
                            p5[z] = "1"
                        else:
                            if um == "1" and dois == "1" and tres == "1":  # 111
                                p5[z] = "1"
                                if z == 0:
                                    p5.insert(0, "1")
                                elif z != 0:
                                    p5[z - 1] = "1"
                            else:
                                if um == "0" and dois == "0" and tres == "1":  # 001
                                    p5[z] = "1"
                                else:
                                    if um == "1" and dois == "0" and tres == "1":  # 101
                                        p5[z] = "0"
                                        if z == 0:
                                            p5.insert(0, "1")
                                        elif z != 0:
                                            p5[z - 1] = "1"
                                    else:
                                        if um == "0" and dois == "1" and tres == "1":  # 011
                                            p5[z] = "0"
                                            if z == 0:
                                                p5.insert(0, "1")
                                            elif z != 0:
                                                p5[z - 1] = "1"
            y = y - 1
            x = x - 1
            z = z - 1

        um = p3[x]
        tres = p5[z]
        if um == "1" and tres == "0":
            p5[z] = "1"
        else:
            if um == "0" and tres == "0":
                p5[z] = "0"
            else:
                if um == "1" and tres == "1":
                    p5[z] = "0"
                    if z == 0:
                        p5.insert(0, "1")
                    elif z != 0:
                        p5[z - 1] = "1"
                else:
                    if um == "0" and tres == "1":
                        p5[z] = "1"
        x = x - 1
        z = z - 1
    q6()

def q6():
    global res
    res = "ACEITA"

q0()

tp4 = len(p4)
tp5 = len(p5)

if res == "ACEITA":
    if tp4 >= tp5:
        f4 = ''.join(p4)
        print(palavra + "=" + f4, res)
    else:
        if tp5 > tp4:
            f5 = ''.join(p5)
            print(palavra + "=" + f5, res)
else:
    print(palavra, res)