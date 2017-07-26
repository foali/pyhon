from collections import deque

#function to translate a word into piglatin
def translate(word):
    list_voyelle = ["a","e","i","o","u","y"]
    if isinstance(word,str) and word:
        if word[0] in list_voyelle:
            return word + "way"
        else :
            result= deque()
            result.appendleft("ay")
            index_first_vowel = 0
            list_consonant = [] #list of consonant to move before the ay
            for w in word:
                if w not in list_voyelle:
                    list_consonant.append(w)
                    index_first_vowel += 1
                else:
                    break
            result.appendleft(''.join(list_consonant))
            result.appendleft(word[index_first_vowel:])
        return ''.join(d)
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
