#Input data is a text containing three sorts of braces “()”, “{}”, “[]”. Write a program that will
#determine if braces in text are balanced.



def checkBracesBalance(text):
    dict = {'[': ']', '(': ')', '{': '}'}
    bracketList = []
    for character in text:

        if (character == '(' or character == '[' or character == '{') :
            bracketList.append(dict[character])

        elif ( len(bracketList) and character == bracketList[-1]):
            bracketList.pop()


        elif (character == ")" or character == "]" or character == "}" ):
            #ako je character == zagrada za zatvaranje a nije bilo one za otvaranje prethodno
            print ("Braces are NOT balanced. ")
            return

    print("Braces are balanced. ")




with open("./input3.txt", 'r') as myfile:
    data=myfile.read().replace('\n', '')
checkBracesBalance(data)