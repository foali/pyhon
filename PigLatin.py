# Pig Latin challenge for /r/Renegade_Pythons
def translate(word):
    if isinstance(word,str):
        if   len(word) > 0:
            words =  word.split()
            l = len(words)
            final =""
            for i in range(l):
                w =  words[i]
                if w[0] in ["a","e","i","o","u","y"]:
                    new = w + "way"
                else :
                    listtext = list(w)
                    listopt = []
                    while listtext[0] not in ["a","e","i","o","u","y"]:
                        listopt.append(listtext[0])
                        del listtext[0]
                    listtext.extend(listopt)
                    listtext.extend(["a","y"])
                    new = "".join(listtext)
                if i == 0:
                    final = new
                else:
                    final += " " + new 
            return final
    return ''


if __name__ == '__main__':
    # Test cases for the challenge.
    print('starting tests.\n')

    assert type(translate('house')) == str
    assert translate(1.25) == ''
    assert translate('') == ''
    assert translate("california") == "aliforniacay"
    assert translate("paragraphs") == "aragraphspay"
    assert translate("glove") == "oveglay"
    assert translate("algorithm") == "algorithmway"
    assert translate("eight") == "eightway"
    print('finished tests.\nYou passed all tests!')
