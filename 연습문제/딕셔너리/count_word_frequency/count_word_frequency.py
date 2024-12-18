def count_word_frequency(text):
    text = text.replace('.', '')
    text = text.replace(',', '')
    text = text.replace('!', '')
    text = text.replace('?', '')
    text = text.lower()
    array = text.split()
    dic = {}
    for i in array:
        dic[i] = dic.get(i, 0) + 1
    return dic
