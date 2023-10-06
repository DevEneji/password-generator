import random
def complex_suggestor():
    #generates a 10 character password containing: upper-case and lower-case 
    # characters, numbers and special characters using the random module
    source = 'AaUb~Hc&deBf?gV>hiN<jk/Tl\mO^noSp@qJ$rs%Itu_vKw@xCyz!P#Z$L%^RM&*-D+W01Q%23Y4+E56G~78X9F'

    source.split()# separates the individual characters that makes up the string 
                    #stored in source and stores them in a list
    l1=[]
    end = 1
    while end<=10:
        raw = random.choice(source)
        l1.append(raw)
        end+=1
    output = ''.join(l1)
    print(output)

def easy_suggestor():
    #generates an easy-to-remember password by taking random values from the variables
    #words and numbs and joins them together
    words = "Field", "build", "fiend", "kind", "purple", "blue", "dream", "fun", "Dizzy", "drizzle", "mark", "love"
    numbs = "010", "194", "748", "697", "100", "911", "369", "112", "018", "530", "274", "945", "658"
    easy_paswd = random.choice(words) + random.choice(numbs)
    print(easy_paswd)

print("Hi there! Welcome to password suggestor")
print("What kind of password would you like? \nEnter 'ETR' for an easy-to-remember password or 'CMP' for a complex one")
entry = input(">> ")

def entry_func(entry):
    #Takes the user's input as argument, checks what type of password the user wants
    #and calls the right function to generate it
    user_entry = entry.upper()
    if user_entry == 'ETR':
        easy_suggestor()
    elif user_entry == 'CMP':
        complex_suggestor()
    elif entry != 'ETR' or 'etr' or 'CMP' or 'cmp':
        print("Sorry, your input wasn't correct")
        entry = input(">> ")
        entry_func(entry)

entry_func(entry)

i = 1
while i<=5:
    retry = input("\nDo you want another password? \nIf yes, enter 'y' else, enter 'q' to quit \n>> ")
    if retry == 'y': # or 'Y'
        entry = input("\nEnter 'ETR' for an easy-to-remember password or 'CMP' for a complex one \n>> ")
        entry_func(entry)
    elif retry == 'q': #or 'Q':
        quit()