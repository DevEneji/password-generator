import random
'''def suggestor():
    source = 'AaUbHcdeBfgVhiNjkTlmOnoSpqJrsItuvKwxCyz!P@#Z$L%^RM&*-D+W01Q23Y4E56G78X9F'
    source.split()
    l1=[]
    end = 1
    while end<=8:
        raw = random.choice(source)
        l1.append(raw)
        end+=1
        output = ''.join(l1)
    print(output)
suggestor()

from functools import reduce

def suggestor():
    source = 'AaUbHcdeBfgVhiNjkTlmOnoSpqJrsItuvKwxCyz!P@#Z$L%^RM&*-D+W01Q23Y4E56G78X9F'
    source.split()
    l1=[]
    end = 1
    while end<=8:
        raw = random.choice(source)
        l1.append(raw)
        end+=1
        output = reduce(lambda x,y:x+y, l1)
    print(output)
suggestor()'''

def complex_suggestor():
    source = 'AaUb~Hc&deBf?gV>hiN<jk/Tl\mO^noSp@qJ$rs%Itu_vKw@xCyz!P#Z$L%^RM&*-D+W01Q%23Y4+E56G~78X9F'
    cap_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    small_letters = 'abcdefghijklmnopqrstuvwxyz'
    nums = '0123456789'
    spec_char = '~@!#$%^&*_-+<>?\/'

    source.split()
    l1=[]
    end = 1
    while end<=8:
        raw = random.choice(source)
        l1.append(raw)
        end+=1
        for elem in l1:
            if cap_letters and small_letters and nums and spec_char in l1:
                continue
            else:
                print('psst')
    output = ''.join(l1)
    print(output)

complex_suggestor()