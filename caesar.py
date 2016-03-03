def rotate_word(text,number):
    if isinstance(number,int) and isinstance(text,str) :
        number =number%26
        listext =  list(text)
        for i in range(len(text)):
            value = ord(text[i])
            if value in list(range(65,91)): #Upper Case
                if(value + number >90) :
                    value = value +number - 26
                else: value = value + number
                listext[i] = chr(value)
            elif value in list(range(97,123)): #Lower case
                if(value + number > 122) :
                    value = value +number - 26
                else: value = value + number
                listext[i] = chr(value)
        return "".join(listext)

def decript_word(text,number):
     if isinstance(number,int) and isinstance(text,str) :
        number =number%26
        listext =  list(text)
        for i in range(len(text)):
            value = ord(text[i])
            if value in list(range(65,91)): #Upper Case
                if(value - number <65) :
                    value = value - number + 26
                else: value = value - number
                listext[i] = chr(value)
            elif value in list(range(97,123)): #Lower case
                if(value - number < 97) :
                    value = value - number + 26
                else: value = value - number
                listext[i] = chr(value)
        return "".join(listext)
    
if __name__ == '__main__':
    with open('caesar.txt','r') as f:
        with open('resultc.txt','r+') as g:
            for line in f:
                text = line.rstrip('\n')
                rtext = rotate_word(text,7)
                g.write(rtext)
                g.write('\n')
            g.close()
        f.close()
        
    
