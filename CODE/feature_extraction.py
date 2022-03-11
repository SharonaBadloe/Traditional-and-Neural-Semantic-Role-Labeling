import sys
import spacy
from spacy import displacy
from dframcy import DframCy
from spacy.tokens import Doc
import en_core_web_sm
import pandas as pd

def columns__to_lists(df):
    """
    turns dataframe into several lists that are used later on

    input:
    df:pandas to_dataframe

    returns:
    tokens:list
    lemma:list
    xpos:list
    predicates:list
    raw_gold:list
    gold:list

    """
    tokens = df.col1.tolist()
    lemma = df.col2.tolist()
    xpos = df.col4.tolist()
    predicates = df.col12.tolist()
    raw_gold = df.col11.tolist()
    gold = list()
    for item in raw_gold:
        if item == "V":
            gold.append("_")
        else:
            gold.append(item)
    return tokens, lemma, xpos, predicates, raw_gold, gold

def tokens_to_dframcy(tokens,df):
    """
    turns tokens into dramcy dataframe

    input:
    tokens:list
    df:pandas to_dataframe

    returns:
    spacy_df:pandas dataframe
    doc:nlp object

    """
    processed_tokens = []
    for token in tokens:
        newtoken = str(token)
        processed_tokens.append(newtoken)
    joined_tokens = " ".join(processed_tokens)

    def custom_tokenizer(text):
        tokens = df.col1.tolist()
        return Doc(nlp.vocab, tokens)
    nlp = spacy.load('en_core_web_sm')
    nlp.tokenizer = custom_tokenizer
    nlp.max_length = 5169840
    text = joined_tokens

    # We open text in the Dframcy module
    dframcy = DframCy(nlp)
    doc = dframcy.nlp(text)

    # We create a basic dataframe with dFramcy features, columsn used can
    # be found back in the columns variable
    spacy_df = dframcy.to_dataframe(doc, columns = ['text', 'head', 'dep_', 'left_edge', 'right_edge'])
    return spacy_df,doc

def extract_dependent_pos(doc, spacy_df,nlp):
    '''
    Opens Dframcy df, adds the following columns:
    :left_edge_pos: pos tag of the leftmost syntactic dependent of the token
    :right_edge_pos: pos tag of the rightmost syntactic dependent of the token

    :param df: Dframcy dataframe
    '''

    left_edge = spacy_df.token_left_edge.tolist()
    right_edge = spacy_df.token_right_edge.tolist()

    left_edge_pos = []
    for token in left_edge:
        doc = nlp(token)
        left_edge_pos.append(doc[0].tag_)

    right_edge_pos = []
    for token in right_edge:
        doc = nlp(token)
        right_edge_pos.append(doc[0].tag_)

    spacy_df['left_edge_pos'] = left_edge_pos
    spacy_df['right_edge_pos'] = right_edge_pos

def extract_children(doc, df):
    '''
    Opens Dframcy df, adds the following columns:
    :children: for every token the children are calculated

    :param df: Dframcy dataframe
    :param doc: NLP doc created from our data
    '''
    children = []
    children_len = []

    for token in doc:
        c = [child for child in token.children]
        children.append(c)

    for item in children:
        num = len(item)
        children_len.append(num)

    df['children'] = children
    df['children_int'] = children_len

def extract_ancestors(doc, df):
    '''
    Opens Dframcy df, adds the following columns:
    :ancestors: for every token the ancestors are calculated

    :param df: Dframcy dataframe
    :param doc: NLP doc created from our data
    '''
    ancestors = []
    ancestors_len = []

    for token in doc:
        l = []
        for ancestor in token.ancestors:
            l.append(ancestor)
        ancestors.append(l)

    for item in ancestors:
        num = len(item)
        ancestors_len.append(num)

    df['ancestors'] = ancestors
    df['ancestors_int'] = ancestors_len

def extract_pos_head(doc, df,nlp):
    """
    Opens Dframcy df, adds the following columns:
    :token_head_pos: for each token head, its pos tag is found

    :param df: Dframcy dataframe
    """
    heads = df.token_head.tolist()

    token_head_pos = []
    for head in heads:
        doc = nlp(head)
        token_head_pos.append(doc[0].tag_)

    df['token_head_pos'] = token_head_pos

def main(input_file):

    # if argv is None:
    #     argv = sys.argv
    #
    # input_file = argv[1]
    print('reading in df\n')
    df = pd.read_csv(input_file, sep = '\t', engine='python',comment = '#', quotechar = "|", header = None, names = ['col' + str(x) for x in range(13)])
    df.dropna(inplace=True)

    print('loading spacy_model\n')
    nlp = spacy.load('en_core_web_sm')

    print('making lists\n')
    tokens, lemma, xpos, predicates, raw_gold, gold = columns__to_lists(df)
    spacy_df,doc = tokens_to_dframcy(tokens,df)

    spacy_df['lemma'] = lemma
    spacy_df['xpos'] = xpos
    print('extracting more advanced features\n')
    extract_dependent_pos(doc, spacy_df,nlp)
    extract_children(doc, spacy_df)
    extract_ancestors(doc, spacy_df)
    extract_pos_head(doc, spacy_df,nlp)
    spacy_df['predicate'] = predicates
    spacy_df['gold'] = gold


    outfile = input_file.replace('.conll' , '-features_extracted.csv')

    (print('writing csv \n'))
    print(spacy_df.head(5))
    spacy_df.to_csv(outfile, sep = '\t', header = True, index = False, quotechar = '|')
    print(outfile)

if __name__ == '__main__':
    main()
