import spacy
import sys
from spacy import displacy
from spacy.tokens import Doc
from spacy.tokens import Doc
import pandas as pd
import en_core_web_sm
from dframcy import DframCy
from sklearn.metrics import classification_report, confusion_matrix

#######################################################################################################################################

def main(argv = None):
    
    if argv is None:
        argv = sys.argv
    
    input_file = argv[1] #this one should be "../DATA/UP_English-EWT/en_ewt-up-train.conllu"
    
    #We open the input file as a pandas dataframe and we remove all the NaNs
    df = pd.read_csv(input_file, sep = '\t', comment = '#', header = None, names = ['col' + str(x) for x in range(13)])
    df.dropna(inplace = True)
    
    #We convert some of the original columns into lists that we are going to use later on
    xpos = df.col4.tolist()
    preds = df.col10.tolist()
    tokens = df.col1.tolist()
    first_args = df.col11.tolist()
    
    #We create a dFramcy dataframe that contains only the tokens, and that will contain the information processed with Spacy
    def custom_tokenizer(text):
        tokens = df.col1.tolist()
        return Doc(nlp.vocab, tokens)
    
    nlp = spacy.load('en_core_web_sm')
    nlp.tokenizer = custom_tokenizer
    nlp.max_length = 1022030
    # open text in Dframcy module 
    dframcy = DframCy(nlp)
    doc = dframcy.nlp(" ")
    spacy_df = dframcy.to_dataframe(doc, columns = ["text"])
    
    print()
    print()
    print()
    
    #We proceed with PREDICATE IDENTIFICATION and EVALUATION
    print("IDENTIFYING THE PREDICATES WITH A RULE-BASED APPROACH...")
    print()
    print()
    print()
    #We add our predicates, found with some rules, to the Spacy dataframe
    predicates = []
    for item in xpos:
        if item in ['VBP', 'VBD', 'VBZ', 'VBN', 'VB']: #RULE: if the xpost tag is in the list, let's consider it a predicate
            predicates.append("PRED")
        else:
            predicates.append("_")
    spacy_df['predicates'] = predicates   
    
    #We add the gold predicates, found in the original inputfile, to the Spacy dataframe
    gold_predicates = []
    for item in preds:
        if item != "_":
            gold_predicates.append("PRED")
        else:
            gold_predicates.append("_")
    spacy_df['gold predicates'] = gold_predicates
    
    print("THE PREDICATES HAVE BEEN IDENTIFIED, NOW CARRYING OUT THE EVALUATION...")
    print()
    print()
    print()
    
    report = classification_report(gold_predicates, predicates)
    print("Classification report:")
    print(report)
    
    print()
    print()
    print()
    
    matrix = confusion_matrix(gold_predicates, predicates)
    print("Confusion matrix:")
    print(matrix)
    
    print()
    print()
    print()
    
    print("EVALUATION DONE. NOW SAVING THE RESULTS IN A CSV FILE...")
    print()
    print()
    print()
    
    output_path = "../DATA/OUTPUT/predicate_identification_frame.csv"
    spacy_df.to_csv(output_path, sep = '\t', header = True, index = False, quotechar = '|')
    
    print("SAVED.")
    print()
    print()
    print()
    
    #We proceed with ARGUMENT IDENTIFICATION and EVALUATION
    print("IDENTIFYING THE ARGUMENTS WITH A RULE-BASED APPROACH..")
    print()
    print()
    print()
    arguments = []
    for token in doc:
        if token.dep_ in ['nsubj'] or (token.dep_ in ["pobj"] and str(token.head) == "by"):
            arguments.append("ARG")
        elif token.dep_ in ['dobj', 'nsubjpass'] and str(token.head.lemma_) not in ["say", "tell"]:
            arguments.append("ARG")
        elif (token.dep_ in ["pobj"] and str(token.head) == "to") or (token.dep_ in ["dobj"] and str(token.head.lemma_) in ["say", "tell"]) or token.dep_ in ["dative"]:
            arguments.append("ARG")
        elif token.pos_ in ["ADV", "SCONJ"] and token.text.lower() == "how":
            arguments.append("ARG")
        elif token.pos_ in ["ADV", "SCONJ"] and token.text.lower() in ["now", "already"]:
            arguments.append("ARG")
        else:
            arguments.append("_")
    spacy_df['arguments'] = arguments
    
    gold_arguments = []
    for item in first_args:
        if item != "_" and item != "V":
            gold_arguments.append("ARG")
        elif item == "V":
            gold_arguments.append("_")
        else:
            gold_arguments.append("_")
    spacy_df['gold arguments'] = gold_arguments
    
    print("THE ARGUMENTS HAVE BEEN IDENTIFIED, NOW CARRYING OUT THE EVALUATION...")
    print()
    print()
    print()
    
    report = classification_report(gold_arguments, arguments)
    print("Classification report:")
    print(report)
    
    matrix = confusion_matrix(gold_arguments, arguments)
    print("Confusion matrix:")
    print(matrix)
    
    print()
    print()
    print()
    
    print("EVALUATION DONE. NOW SAVING THE RESULTS IN A CSV FILE...")
    print()
    print()
    print()
    
    output_path = "../DATA/OUTPUT/argument_identification_frame.csv"
    spacy_df.to_csv(output_path, sep = '\t', header = True, index = False, quotechar = '|')
    
    print("SAVED. FINISHED.")
    
if __name__ == '__main__':
    main()
