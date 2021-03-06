**Be sure to execute the terminal from the correct folder (CODE). The steps to run to carry out the experiment are just 1, 2, 5 and 6, since 3 and 4 are already comprehended into 5.**

## 1) To execute duplicate_conll.py:
This script takes as input the original conll file and outputs a duplicated version of the conll, in which the sentences are duplicated according to their number of predicates, and each duplication contains the arguments of a different predicate. The file can be run once, and automatically duplicates the test, dev and training files. They are saved to the DATA folder. 

### how to run:
- python duplicate_conll.py 

## 2) To execute rule-based.py:
This script takes as input a duplicated file (we chose to execute it on the testset) and identifies predicates and arguments with a rule-based approach.

### how to run:
- python rule-based.py "../DATA/UP_English-EWT/en_ewt-up-test.duplicated.conll"

## 3) To execute feature_extraction-py:
**DISCLAIMER: THE EXECUTION OF THIS SCRIPT IS ALREADY INCLUDED IN THE main.py SCRIPT.** This script takes as input the duplicated files and outputs new files with the decided features extracted. 

- python feature_extraction.py "../DATA/UP_English-EWT/en_ewt-up-train.duplicated.conll"
- python feature_extraction.py "../DATA/UP_English-EWT/en_ewt-up-dev.duplicated.conll"
- python feature_extraction.py "../DATA/UP_English-EWT/en_ewt-up-test.duplicated.conll"

## 4) To execute SVM_classifier.py:
**DISCLAIMER: THE EXECUTION OF THIS SCRIPT IS ALREADY INCLUDED IN THE main.py SCRIPT.**
This script takes as input the files that result from feature_extraction-py, in order to 1) train a SVM classifier on the new trainingset with the features extracted; 2) test that classifier on the new testset with the features extracted. 

- python SVM_classifier.py "../DATA/OUTPUT/en_ewt-up-train.duplicated-features_extracted.csv"
- python SVM_classifier.py "../DATA/OUTPUT/en_ewt-up-test.duplicated-features_extracted.csv"

## 5) To execute main.py
This main function runs the following steps: feature extraction + training of the classifier + testing of the classifier. To run this file you need a (duplicated) csv file, the script will extract features and train the classifier. It will output the results of the classification report.

Parameters:
- path to trainingfile (trainingfile)
- path to inputfile (testfile)

### how to run:
- python main.py "../DATA/UP_English-EWT/en_ewt-up-train.duplicated.conll" "../DATA/UP_English-EWT/en_ewt-up-test.duplicated.conll"

## 6) To execute conll_to_json.py
To run this file you need a conll file that is structured in the same way that was provided in the srl_assignment_code.
The parameters you should provide are:
- Path to CoNLL file
- Boolean to indicate whether to duplicate or not

### how to run:
- python conll_to_json.py "../data/srl_univprop_en.dev.conll" False
- python conll_to_json.py "../data/srl_univprop_en.train.conll" True 



