import treetaggerwrapper as ttpw
tagger = ttpw.TreeTagger(TAGLANG='fr', TAGDIR="./TreeTagger")

def ttpw_pos_tag(input_text) :
    output = tagger.tag_text(input_text)
    result=[]
    for word in output :
        result.append([word.split('\t')[0],word.split('\t')[1] ])
    return result
