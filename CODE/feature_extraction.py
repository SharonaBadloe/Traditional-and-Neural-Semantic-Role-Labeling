import sys
import spacy
from spacy import displacy
from dframcy import DframCy
from spacy.tokens import Doc
import en_core_web_sm
import pandas as pd

#######################################################################################################################################

def main(argv = None):
    
    if argv is None:
        argv = sys.argv
    
    input_file = argv[1] #this one should be "../DATA/UP_English-EWT/duplicated_train.csv"
    
    print()
    print()
    print()
    print("PREPROCESSING THE DATAFRAME...")
    print()
    print()
    print()
    
    #We open the input file as a pandas dataframe and we remove all the NaNs
    df = pd.read_csv(input_file, sep = '\t', comment = '#', header = None, names = ['col' + str(x) for x in range(13)])
    df = df.dropna()
    
    #We convert some of the original columns into lists that we are going to use later on
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
            
    #We process the text to convert it into a Dframcy format
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
    nlp.max_length = 1022030
    text = joined_tokens
    
    #We open text in the Dframcy module 
    dframcy = DframCy(nlp)
    doc = dframcy.nlp(text)

    #We create a basic dataframe with dFramcy features
    spacy_df = dframcy.to_dataframe(doc, columns = ['text', 'head', 'dep_', 'left_edge', 'right_edge'])
    
    print("PREPROCESSING DONE. NOW EXTRACTING THE FEATURES...")
    print()
    print()
    print()
    
    #We load spacy again but with its own tokenizer, because our custom tokenizer is hardcoded to return the entire tokenlist of the original data
    nlp = spacy.load('en_core_web_sm')
    
    def extract_dependent_pos(df):
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

    def extract_pos_head(df):
        """
        Opens Dframcy df, adds the following columns:
        :token_head_pos: for each token head, its pos tag is found

        :param df: Dframcy dataframe
        """
        heads = spacy_df.token_head.tolist()

        token_head_pos = []
        for head in heads:
            doc = nlp(head)
            token_head_pos.append(doc[0].tag_)

        df['token_head_pos'] = token_head_pos
        
    #We execute all the previous functions
    spacy_df['lemma'] = lemma
    spacy_df['xpos'] = xpos
    extract_dependent_pos(spacy_df)
    extract_children(doc, spacy_df)
    extract_ancestors(doc, spacy_df)
    extract_pos_head(spacy_df)
    spacy_df['predicate'] = predicates
    spacy_df['gold'] = gold
    
    #We save the output in a csv file
    print("THE FEATURES HAVE BEEN EXTRACTED. NOW SAVING THE RESULTS IN A CSV FILE...")
    print()
    print()
    print()
    
    if input_file == "../DATA/UP_English-EWT/duplicated_train.csv":
        output_path =  "../DATA/OUTPUT/feature_extraction_frame_train.csv"
    elif input_file == "../DATA/UP_English-EWT/duplicated_dev.csv":
        output_path = "../DATA/OUTPUT/feature_extraction_frame_dev.csv"
    elif input_file == "../DATA/UP_English-EWT/duplicated_test.csv":
        output_path =  "../DATA/OUTPUT/feature_extraction_frame_test.csv"

    spacy_df.to_csv(output_path, sep = '\t', header = True, index = False, quotechar = '|')
    print("THE RESULTS HAVE BEEN SAVED.")
    
    
if __name__ == '__main__':
    main()