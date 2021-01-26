from nltk import word_tokenize, pos_tag 

def nltk_pos_tag(input_text) :
    tokenized_text = word_tokenize(input_text, language='french')
    return pos_tag(tokenized_text)
