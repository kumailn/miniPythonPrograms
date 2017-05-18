import random
import os
board = [["E", "E", "E"],["E", "E", "E"],["E", "E", "E"]]
nb = [["E", "E", "E"],["E", "E", "E"],["E", "E", "E"]]

def main():
    print("Welcome to the tictactoe app: ")
    try:
        x = int(input("Num of players????: "))
    except:
        print("MUST be a valud num")
        x = input("Num of players????: ")
    print("welcome!")
    try:
        n = int(input("new game or continue? 1 or 2"))
    except:
        print("again, this has to be a number!!")
        n = input("new game or continue? 1 or 2")
    if int(n) == 2:
        y = int(input("Enter initial state: "))
        nb = []
        for i in y:
            if (i == "X") or (i == "O"):
                nb.append(i)
            else:
                nb.append("E")
        B = nb[:3]
        C = nb[3:6]
        D = nb[6:9]
        nb2 = []
        nb2.append(B)
        nb2.append(C)
        nb2.append(D)
    else:
        nb2 = board
    print("Starting Board: ")
    printB(nb2)
    if win(nb2) == True:
        print("someone already won")
        return 0
    if int(x) == 0:
        AIsim()
        return 0

   

        
    if int(x) == 1:
        p1 = "X"
        p2 = "O"
        w = False
        while w == False:
            gg = False
            cp = 1
            while gg == False:
                p1x = input("player 1: x coordinate (row): ")
                p1y = input("player 1: y (column): ")
                p1x= int(p1x)
                p1y = int(p1y)
                if (nb2[p1x - 1][p1y - 1] == "E"):
                    nb2[p1x - 1][p1y - 1] = p1
                    gg = True
                else:
                    print("There's already something there! Try again")
            print("Your turn:")
            printB(nb2)
            if report(nb2, cp) == True:
                return  0
            cp = 2
            AI(nb2, p2, 2)
    else:
        
        p1 = input("Player 1 character?: ")
        p2 = input("Player 2 character?: ")
        w = False
        while w == False:
            gg = False
            cp = 1
            while gg == False:
                p1x = input("player 1: x coordinate (row): ")
                p1y = input("player 1: y (column): ")
                p1x= int(p1x)
                p1y = int(p1y)
                if (nb2[p1x - 1][p1y - 1] == "E"):
                    nb2[p1x - 1][p1y - 1] = p1
                    gg = True
                else:
                    print("There's already something there! Try again")
            printB(nb2)
            #report(nb2, cp)
            if report(nb2, cp) == True:
                return  0
                

            cp = 2
            gg = False
            while gg == False:
                p2x = input("player 2: x coordinate (row): ")
                p2y = input("player 2: y (column): ")
                p2x= int(p2x)
                p2y = int(p2y)
                if (nb2[p2x - 1][p2y - 1] == "E"):
                    nb2[p2x - 1][p2y - 1] = p2
                    gg = True
                else:
                    print("There's already something there! Try again")
            printB(nb2)
            #report(nb2, cp)
            if report(nb2, cp) == True:
                return  0

def win(board):
    if (board[0][0] != "E") and (board[0][0] == board[0][1]) and (board[0][1] == board[0][2]):
        return True
    elif (board[1][0] != "E") and (board[1][0] == board[1][1]) and (board[1][1] == board[1][2]):
        return True
    elif (board[2][0] != "E") and (board[2][0] == board[2][1]) and (board[2][1] == board[2][2]):
        return True
    elif (board[0][0] != "E") and (board[0][0] == board[1][0]) and (board[1][0] == board[2][0]):
        return True
    elif (board[0][1] != "E") and (board[0][1] == board[1][1]) and (board[1][1] == board[2][1]):
        return True
    elif (board[0][2] != "E") and (board[0][2] == board[1][2]) and (board[1][2] == board[2][2]):
        return True
    elif (board[0][0] != "E") and (board[0][0] == board[1][1]) and (board[1][1] == board[2][2]):
        return True
    elif (board[2][0] != "E") and (board[2][0] == board[1][1]) and (board[1][1] == board[0][2]):
        return True
    else:
        return False

def draw(board):
    cc = 0
    for i in board:
        for j in i:
            if j != "E":
                cc += 1
    if cc == 9:
        return True
    return False


    
def report(board, player):
    if (player == 1) and win(board) == True:
        print("Player 1 WINS!!")
        return True

    elif (player == 2) and win(board) == True:
        print("Player 2 wins!!!!!")
        return True
    elif draw(board) == True:
        print("Its a draw....")
        return True
    return False
    


def reportBool(board, player):
    if (player == 1) and win(board) == True:
       # print("Player 1 WINS!!")
        return True

    elif (player == 2) and win(board) == True:
        #print("Player 2 wins!!!!!")
        return True
    elif draw(board) == True:
       # print("Its a draw....")
        return True
    return False

def reportBoolWin(board, player):
    if (player == 1) and win(board) == True:
       # print("Player 1 WINS!!")
        return True

    elif (player == 2) and win(board) == True:
        #print("Player 2 wins!!!!!")
        return True

    return False


def printB(board):
    for i in board:
        print(i)
        
def AI(board, char, cp):
    print( char + " AIs TURN:")
    nb2 = board
    h = False
    gg = False
    while gg == False:
        ry = random.randint(1, 3)
        rx = random.randint(1,3)
        p1x = rx
        p1y = ry
        if (nb2[p1x - 1][p1y - 1] == "E"):
            nb2[p1x - 1][p1y - 1] = char
            gg = True
            w = True
        else:
            if report(nb2, cp) == True:
               h = True
               return  0
               exit
            print( char + " AI trying again")
    printB(nb2)

def AIsimMod(board, char, cp):
    #print( char + " AIs TURN:")
    nb2 = board
    h = False
    gg = False
    while gg == False:
        ry = random.randint(1, 3)
        rx = random.randint(1,3)
        p1x = rx
        p1y = ry
        if (nb2[p1x - 1][p1y - 1] == "E"):
            nb2[p1x - 1][p1y - 1] = char
            gg = True
            w = True
        else:
            if reportBool(nb2, cp) == True:
               h = True
               return  0
               exit
            #print( char + " AI trying again")
    #printB(nb2)
    #eport(nb2, cp)
   # if report(nb2, cp) == True:
  #       return  0
 #        exit
    
def AIsim():
    ccc = 0
    xw = 0
    ow = 0
    nb2 = board
    while ccc < 50:
        w = False
        nb2 = [["E", "E", "E"],["E", "E", "E"],["E", "E", "E"]]
        while w == False:
            p1 = "X"
            p2 = "O"
            AIsimMod(nb2, p1, 1)
            w = reportBool(nb2, p1)
            if w == True:
                #report(nb2, p1)
                xw += 1
                break
            AIsimMod(nb2, p2, 2)
            w = reportBool(nb2, p2)
            if w == True:
                #report(nb2, p2)
                ow += 1
                break
            
        
        ccc += 1

    print("O AI won " + str(round(((ow/xw)*100), 3)) + "% of the time")
    return (xw, ow)
main()
        
                
                
"""
        w = False
        while w == False:
            p1 = "X"
            p2 = "O"
            AI(nb2, p1, 1)
            w = reportBool(nb2, p1)
            if w == True:
                report(nb2, p1)
                #os._exit(0)
                #break
                return 0
            AI(nb2, p2, 2)
            w = reportBool(nb2, p2)
            if w == True:
                report(nb2, p2)
                #os._exit(0)
                #break
                return 0
        return 0
"""        
                
                
                
        
