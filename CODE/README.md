DISCLAIMER: Be sure to execute the terminal from the correct folder (CODE) ! The steps to run to carry out the experiment are 1, 2, 5 and 6.

## 1) To execute duplicate_conll.py:
This script takes as input the original conll file and outputs a duplicated version of the conll, in which the sentences are duplicated according to their number of predicates, and each duplication contains the arguments of a different predicate.

- python duplicate_conll.py "../DATA/UP_English-EWT/en_ewt-up-train.conllu"
- python duplicate_conll.py "../DATA/UP_English-EWT/en_ewt-up-dev.conllu"
- python duplicate_conll.py "../DATA/UP_English-EWT/en_ewt-up-test.conllu"

## 2) To execute rule-based.py:
This script takes as input a duplicated file (we chose to execute it on the testset) and identifies predicates and arguments with a rule-based approach.

- python rule-based.py "../DATA/UP_English-EWT/duplicated_test.conllu"

## 3) To execute feature_extraction-py:
DISCLAIMER: THE EXECUTION OF THIS SCRIPT IS ALREADY INCLUDED IN THE main.py SCRIPT. This script takes as input the duplicated files and outputs new files with the decided features extracted. 

- python feature_extraction.py "../DATA/UP_English-EWT/duplicated_train.csv"
- python feature_extraction.py "../DATA/UP_English-EWT/duplicated_dev.csv"
- python feature_extraction.py "../DATA/UP_English-EWT/duplicated_test.csv"

## 4) To execute SVM_classifier.py:
DISCLAIMER: THE EXECUTION OF THIS SCRIPT IS ALREADY INCLUDED IN THE main.py SCRIPT.
This script takes as input the files that result from feature_extraction-py, in order to 1) train a SVM classifier on the new trainingset with the features extracted; 2) test that classifier on the new testset with the features extracted. 

- python SVM_classifier.py "../DATA/OUTPUT/feature_extraction_frame_train.csv"
- python SVM_classifier.py "../DATA/OUTPUT/feature_extraction_frame_test.csv"

## 5) To execute main.py
This main function runs the following steps: feature extraction + training of the classifier + testing of the classifier. To run this file you need a (duplicated) csv file, the script will extract features and train the classifier. It will output the results of the confusion matrix.

Parameters:
- path to inputfile (trainingfile)
- path to testfile

### example:
- python main.py "../DATA/UP_English-EWT/duplicated_train.csv"
- python main.py "../DATA/UP_English-EWT/duplicated_test.csv"

## 6) To execute conll_to_json.py
To run this file you need a conll file that is structured in the same way that was provided in the srl_assignment_code.
The parameters you should provide are:
- Path to CoNLL file
- Boolean to indicate whether to duplicate or not

### example:
- python conll_to_json.py "../data/srl_univprop_en.dev.conll" False
- python conll_to_json.py "../data/srl_univprop_en.train.conll" True 



