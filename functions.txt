def printHidden(word, correctguesses): #defining a function
    for letter in word:
        if letter in correctguesses:
            print(letter, end=" ") 
        else:
            print("_", end=" ") # print _ if not guessed
    print() #to print "make a guess" after the underscores

def notguessed(word, correctguesses):
    for letter in word:
        if letter not in correctguesses:
            return True
    
    return False


    
f5 = '''
 |---
 |  |
 |
 |
 |
 |
'''

f4 = '''
 |---
 |  |
 |  O
 |
 |
 |
''' 

f3 = '''
 |---
 |  |
 |  O
 | /|
 |
 |
'''

f2 = '''
 |---
 |  |
 |  O 
 | /|\\
 |
 |
'''

f1 = '''
 |---
 |  |
 |  O 
 | /|\\
 | / 
 |
'''

f0 = '''
 |---
 |  |
 |  O 
 | /|\\
 | / \\
 |
'''

def printfigures(lives):
    if lives == 5:
        print(f5)
    
    elif lives == 4:
        print(f4)
    
    elif lives == 3:
        print(f3)
    
    elif lives == 2:
        print(f2)
        
    elif lives == 1:
        print(f1)
    
    elif lives == 0:
        print(f0)

