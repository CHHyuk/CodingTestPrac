# 모스 부호(1)
morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'
}
def solution(letter):
    list1 = letter.split()
    list2 = []
    for i in range(len(list1)):
        list2.append(morse[list1[i]])
    result = ''.join(list2)
    return result



solution(".... . .-.. .-.. ---")