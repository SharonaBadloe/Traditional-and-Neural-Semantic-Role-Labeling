from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
import pandas as pd
import numpy as np
import sys
import csv

def extract_features_and_labels(trainingfile, feature_list):
    '''
    This function opens the trainingfile and extracts the features and gold labels.
    
    :param trainingfile: file with annotated training data
    :type trainingfile: .conll file
    
    :returns: data - a list of features, and targets - a list of gold labels
    '''
    
    # read in trainingfile
    conllinput = open(trainingfile, 'r', encoding='utf-8')
    conll_train = csv.DictReader(conllinput, delimiter='\t', quotechar='|')
    
    # create empty containers to store training features and targets
    data = []
    targets = []

    # extract training features and targets
    for row in conll_train:
        if len(row) > 0:
            feature_dict = {}
            targets.append(row['gold'])
            for feature in feature_list:
                feature_dict[feature] = row[feature]
            data.append(feature_dict)

    return data, targets
    
def extract_features(inputfile, feature_list):
    '''
    This function extracts features (tokens) from the inputfile
    
    :param inputfile: test data to predict
    :type inputfile: .conll file
    
    :returns: data - list of all features in the inputfile
    '''  
    
    # read in inputfile
    conllinput = open(inputfile, 'r', encoding='utf-8')
    conll_reader = csv.DictReader(conllinput, delimiter='\t', quotechar='|')
    
    # create empty container for features
    data = []

    # extract inputdata features
    for row in conll_reader:
        if len(row) > 0:
            feature_dict = {}
            for feature in feature_list:
                feature_dict[feature] = row[feature]
            data.append(feature_dict)
            
    return data

def create_classifier(train_features, train_targets):
    '''
    This function vectorizes the training data and trains an SVM model
    
    :param train_features: the training features
    :param train_targets: the gold labels
    :type train_features: list of tokens
    :type train_targets: list of labels
    
    :returns: vectorizer and trained SVM model
    '''
    # define model
    model = LinearSVC(max_iter=2000)

    # vectorize training features and train model
    vec = DictVectorizer()
    features_vectorized = vec.fit_transform(train_features)
    model.fit(features_vectorized, train_targets)
    
    return model, vec

def classify_data(model, vec, inputdata, outputfile, feature_list):
    '''
    This function classifies the test data, and writes predictions to a new outputfile for evaluating.
    
    :param model: SVM model trained on gold data
    :param vec: Dict Vectorizer
    :param inputdata: test data file
    :param outpufile: name of file to write output to 
    :type inputdata: .conll file 
    :type outputfile: .conll file
    '''  
    # extract and vectorize inputfile features
    features = extract_features(inputdata, feature_list)
    features = vec.transform(features)
    
    # predict
    predictions = model.predict(features)  
    
    # save predictions to file for evaluating
    input_df = pd.read_csv(inputdata, sep='\t', header=0, quotechar='|')
    input_df['pred'] = predictions

    input_df.to_csv(outputfile, sep='\t', header=True, index=False, quotechar='|')
    
def evaluate(outputfile):
    ''' 
    This function evaluates the classifier.
    
    :param outputfile: path to file that contains the predictions
    '''    
    
    # get evaluation columns from file in dataframe
    eval_df = pd.read_csv(outputfile, sep='\t', header=0, quotechar='|')
    
    # get gold labels and predictions from dataframe to list
    gold = eval_df.gold.tolist()
    predictions = eval_df.pred.tolist()
    
    # print report
    report = classification_report(gold, predictions,digits = 7, zero_division=0)
    print(report)
    
def main(argv=None):
    ''' 
    This function puts all above functions together.
    
    :param trainingfile: path to trainingfile
    :param inputfile: path to inputfile
    '''    
    
    # define features to use
    feature_list = ['token_text',
     'token_head',
     'token_dep_',
     'token_left_edge',
     'token_right_edge',
     'lemma',
     'xpos',
     'left_edge_pos',
     'right_edge_pos',
     'children',
     'children_int',
     'ancestors',
     'ancestors_int',
     'token_head_pos',
     'predicate']
    
    if argv is None:
        argv = sys.argv
    
    # define args
    trainingfile = argv[1]
    inputfile = argv[2]
    
    # define outputfile
    outputfile = inputfile.replace('.csv','.' + 'SVM' + '.csv')

    # function calls
    training_features, gold_labels = extract_features_and_labels(trainingfile, feature_list)
    ml_model, vec = create_classifier(training_features, gold_labels)
    classify_data(ml_model, vec, inputfile, outputfile, feature_list)
    evaluate(outputfile)
    
if __name__ == "__main__":
    main()