#coding:utf8
import string
# 接受输入的字符串
# 判断是否是单词
# 是否有辅音
# 组词
def piglatin():
    self_sound = ['a', 'e', 'i', 'o', 'u']
    s =  raw_input('Input something please!\n')
    words =  s.split()
    new_words =  ''
    for word in words:
        tmp_word =  word.lower()
        position = []
        for i in range(len(tmp_word)):
            if tmp_word[i] in self_sound:
                pass
            #elif tmp_word[i].isdigit(): #TODO
            #    break
            else:
                position.append(i)
        
        tmp_word = tmp_word[:position[0]] +\
                    tmp_word[position[0]+1:] +\
                    tmp_word[position[0]]+'ay'
    

        new_words += tmp_word  + ' '
    print new_words
if __name__ == "__main__":
    piglatin()

