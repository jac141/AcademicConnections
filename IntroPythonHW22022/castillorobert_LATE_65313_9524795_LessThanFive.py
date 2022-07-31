def LTF(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) < n:
            word_len.append(x)
    return word_len	

input = input("Sentence? :")
print(LTF(5, input))
