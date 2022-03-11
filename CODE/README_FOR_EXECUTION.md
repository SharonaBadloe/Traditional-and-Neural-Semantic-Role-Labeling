Be sure to execute the terminal from the correct folder (CODE)

## 1) To execute rule-based.py:

python rule-based.py "../DATA/UP_English-EWT/en_ewt-up-train.conllu"

## 2) To execute feature_extraction-py:

python feature_extraction.py "../DATA/UP_English-EWT/duplicated_train.csv
<br /><br />
and also
python feature_extraction.py "../DATA/UP_English-EWT/duplicated_dev.csv"
  <br /><br />and also
python feature_extraction.py "../DATA/UP_English-EWT/duplicated_test.csv"

## 3) To execute conll_to_json.py
To run this file you need a conll file that is structured in the same way that was provided in the srl_assignment_code.
The parameters you should provide are:
- Path to CoNLL file
- Boolean to indicate whether to duplicate or not

### example usage:
- python conll_to_json.py "../data/srl_univprop_en.dev.conll" False
- python conll_to_json.py "../data/srl_univprop_en.train.conll" True 



