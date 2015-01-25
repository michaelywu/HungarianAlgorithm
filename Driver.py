from HungarianAlg import HungarianAlgorithm

def main():
    n = []
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
    algortihm = HungarianAlgorithm(n)
        #algorithm.Execute()

main() #invoke main function
