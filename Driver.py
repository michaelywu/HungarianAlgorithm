from HungarianAlg import HungarianAlgorithm

def main():
    n = [] #4x4 test matrix
    n.append([])
    n.append([])
    n.append([])
    n.append([])
    
    n[0].append(90)
    n[0].append(75)
    n[0].append(75)
    n[0].append(80)

    n[1].append(35)
    n[1].append(85)
    n[1].append(55)
    n[1].append(65)

    n[2].append(125)
    n[2].append(95)
    n[2].append(90)
    n[2].append(105)

    n[3].append(45)
    n[3].append(110)
    n[3].append(95)
    n[3].append(115)

    q=[] # 3x3 test matrix
    q.append([])
    q.append([])
    q.append([])

    q[0].append(250)
    q[0].append(400)
    q[0].append(350)

    q[1].append(400)
    q[1].append(600)
    q[1].append(350)

    q[2].append(200)
    q[2].append(400)
    q[2].append(250)

    p = [] #5x5 test matrix
    p.append([])
    p.append([])
    p.append([])
    p.append([])
    p.append([])
    
    p[0].append(20)
    p[0].append(23)
    p[0].append(36)
    p[0].append(80)
    p[0].append(26)
    
    p[1].append(28)
    p[1].append(29)
    p[1].append(25)
    p[1].append(44)
    p[1].append(73)
    
    p[2].append(21)
    p[2].append(34)
    p[2].append(37)
    p[2].append(45)
    p[2].append(38)
    
    p[3].append(33)
    p[3].append(27)
    p[3].append(40)
    p[3].append(56)
    p[3].append(31)

    p[4].append(39)
    p[4].append(35)
    p[4].append(60)
    p[4].append(50)
    p[4].append(48)
    algortihm = HungarianAlgorithm(p)


main() #invoke main function
