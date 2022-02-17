

#import keyboard
import random
def bingo():
    gameOver = 0
    L = [[1], [ 2], [ 3], [ 4], [ 5], [ 6], [ 7], [ 8], [ 9], [10], 
         [11], [12], [13], [14], [15], [16], [17], [18], [19], [20], 
         [21], [22], [23], [24], [25], [26], [27], [28], [29], [30], 
         [31], [32], [33], [34], [35], [36], [37], [38], [39], [40], 
         [41], [42], [43], [44], [45], [46], [47], [48], [49], [50], 
         [51], [52], [53], [54], [55], [56], [57], [58], [59], [60], 
         [61], [62], [63], [64], [65], [66], [67], [68], [69], [70], 
         [71], [72], [73], [74], [75],
         [76], [77], [78], [79], [80], 
         [81], [82], [83], [84], [85], [86], [87], [88], [89], [90], 
         [91], [92], [93], [94], [95], [96], [97], [98], [99]]
    NL = []
    act = 0
 
    while gameOver != 1:
        delta = 0
        if act == 1:
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
            print("\n")
   
            
        if len(L) == 0:
            break
        x = random.randint(0,len(L)-1)
        y = L[x]
        print("Current Number " + str(L[x]))
        NL.append(L[x])
        L.remove(L[x])
     
        print("Numbers already called: ")
        print("\n")
      
        count = 0
        for x in range(len(NL)):
            if count == 10:
                print("\n")
                count = 0
            
            print(NL[x], end = '  ')
                #delta = 1
            count = count +1
        act = 1
        count = count + 1
        print("\n")
        print("\n")
        if delta == 1:
            print("")
        if wantsRollAgain() == False:
            break
    print("\n")
    print("\n")
    print("Game Over!!!")
            
        
def wantsRollAgain():
   '''asks a player if they want to roll again, uses wantsContinue().
   For part2, also handles case where player is the AI'''
   response = input('Press [Enter] to reveal another number: ').strip()
   return wantsContinue(response)

def wantsContinue(response):
   '''checks if the response a user gives indicates they want to continue'''
   if response=='n':
       return False
   else:
       return True
    
if __name__ == '__main__':
  bingo()
