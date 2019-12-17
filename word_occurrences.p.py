string =input("Please enter a string:")
word_dic={}


words=string.split()
for word in words:
    count=word_dic.get(word,0)
    word_dic[word]=count+1

words=list(word_dic.keys())
words.sort()

maxlength=max(len(word)for word in words)
for word in words:
    print("{:{}} : {}".format(word, maxlength, word_dic[word]))