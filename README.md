# Advanced NLP Assignment 2: Traditional and Neural Semantic Role Labeling

The project was carried out by Giorgio Malinverni, Sharona Badloe, Sybren Moolhuizen and Konstantina Andronikou during the "NLP Technology" course taught by Antske Fokkens and Pia Sommerauer.

This README contains the infromation to run a classifier that performs Semantic Role Labeling (SRL). This work is divided into two parts:
* `Part 1: Traditional SRL`
* `Part 2: Neural SRL`

### Provided Data
Development Data:
* `en_ewt-up-dev.conllu`

Training Data:
* `en_ewt-up-train.conllu`

Test Data:
* `en_ewt-up-test.conllu`

This data was preprocessed and duplicated before being used as an input for Part 1 (see Section 2).

### Code 
The folder [**CODE**](https://github.com/gioguitar99/NLP_Assignment_2/tree/main/CODE) consists of the following script:
* `main.py` This file carries out the entire experiment (feature extraction,
training, testing)
* `readme_for_execution.md` This readme includes the information to run the main functions in the terminal 

### Results
The folder [**OUTPUT**](https://github.com/gioguitar99/NLP_Assignment_2/tree/main/DATA/OUTPUT) consists of the output files of the following components:
* `Output of identification for predicates and arguments`
* `Output of the Feature Extraction process`
* `Output of the predictions`
* `Basic Evaluation (scores and matrices)`

### Part 1: Traditional SRL

### 1. Introduction 

The NLP classification task presented and analyzed in this report is Semantic Role Labelling (SRL). Semantic Role labelling is the process of identifying semantic relations between predicates and their related participants and characteristcs (Carreras, 2005). Semantic argument identification and classification are the two subtasks within SRL. In an argument classification task, each syntactic element in a sentence is classified as a semantic argument or a non-argument using semantic argument identification. While semantic argument classification entails categorizing each semantic argument into one of several semantic roles, such as ARG0, ARG1, and so on. The aim of this report is to present the creation of a machine learning algorithm system that can identify verb arguments in a sentence and classify them with their semantic role. 


### 2. Predicate and Argument Identification (and Evaluation) 

In order to carry out the SRL task, the sentences that had multiple predicates were duplicated as many times as the amount of predicates they included. In each duplication, the specific arguments depending on that corresponding predicate were added. During the whole SRL experiment, the duplications were used as input (both for the rule-based identification and the machine learning classification). 

  ### 2.1 Rule-based Predicates 
  
To identify and extract the predicates a rule-based approached was used. The first step of the procedure was to read and load the given dataset using the external package pandas. Then the dataset was combined with the external library SpaCy to process the data. After analyzing the columns of the dataset, it was decided that the relevant column for the predicate identification was "XPOS". This column contained PoS tag abbreviations that preserved the original value of the dataset with manual annotation and corrections. As predicates tend to refer to verbs, it was decided that the rule to identify the predicates would have been the following: if the XPOS tag of a token corresponds to VBP, VBD, VBZ, VBN, or VB, then the token is a predicate. These labels cover both regular and irregular forms both in terms of inflection and derivation (such as 3rd person, tense, affixes etc.). Every detected instance was labeled as “PRED”. After the identification process, all predicates were stored in a new dataset, with the corresponding gold label to each predicate. The extracted predicates and the gold labels are then used to evaluate this sub-task.

  ### 2.2 Rule-based Arguments 

In terms of argument identification, a rule-based approach was also followed. In order to generate and implement rules for the identification, the dataset was carefully analyzed to identify relevant patterns. Six syntactic patterns were identified and used as rules for the identification process: (1) if the dependency is a subject or a prepositional object with the preposition “by”; (2) objects in active sentences; (3) subjects in passive sentences; (4) "to" + prepositional objects; (5) datives depending from certain verbs (e.g. "me" in "give me"); (6) frequent adjectives: "now", "how", "already". All instances that followed any of the rules were classified as "ARG" and were stored in a new dataset with the corresponding gold labels. The process was then evaluated.


### 3. Features 

The following table provides an overview of all the features selected to carry out the classification task. The procedure of implementing the features, as well as the motivation behind the selection, will be described in greater detail in the following sections.

| Baseline Features         | Provided Features       | Advanced Features                        |
| :-----------:             | :-------------:         | :-----:                                  |
| Token                     | Dependency Relation     | Token head of a target token             |
| Lemma                     |                         | Pos head of a target token               |
| PoS tag                   |                         | Corresponding predicate of an argument   |
| Bigram (target + next)    |                         | PoS of left/rightmost dependent          |
| Trigram (target + 2 next) |                         | Lenght of lists (ancestors and children  |
| Postag bigram             |                         |                                          |
| Postag trigram            |                         |                                          |


### 3.1 Baseline Features 

The aim of this report is to implement a variety of features that can capture the information requested to correctly carry out the classification process.

The features chosen for the baseline system are: token, lemma, POS tags, token bigram/trigrams and POS bigram/trigram):
- **Token/lemma:** Token is "the word or the punction mark as it appears in the sentence" (Abu-Jbara and Radev, 2012, p.331) while lemma is the root of the token. Token and Lemma in terms of a classification task can be beneficial as the text is divided into pieces thus it can make the process of analyzing and training a classifier easier. 
- **PoS tag:** It is used to connect a token in text data to its grammatical definition. In a semantic role labelling task it can be useful since some arguments are more likley to correspond to a specific PoS category (e.g. the agent, ARG0, is likely to be a noun).
- **Token bigram/trigram:** Token bigram and trigram are used to look at the surrondings cues of the token (e.g. previous or next token) (Lapponi et al., 2012). This can be helpful in the identification and classification procedure as it can idenfity potential syntactic patterns. 
- **PoS tag of the bigram/trigram:** As the previous feature can be helpful to identify patterns within the dataset the POS tag of the trigram and bigram will give a better understanding of their grammatical definition. 
 
 
### 3.2 Provided Features
It is worth mentioning that the dataset provided for this specific task had already some features implemented. The data contained both syntactic and morphological features (token, lemma, dependency relation). Hence, we did not extracted those features by ourselves. The features we re-used were:
- **Dependency relation:** This feature gets the dependency relation between a target token and its head. It is useful for argument classification since some relations (such as "nsubj") are likely to correspond to a certain argument (such as "ARG0"). 


### 3.3 Advanced Features 

In combination with the baseline features an advance selection was additionally made. This selection was strongly motivated form previous research done on SRL. The following list of features were implemented:

- **Token head of target token:** arguments tend to rely on the syntactic structure, therefore the head of the target token can possibly target a specific argument. 
- **PoS head of the target token:** the corresponding PoS tag is useful when it correlates with the head due to the additional grammatical information that is likely to provide a argument pattern. 
- **PoS of the leftmost/rightmost dependent:** The grammatical information of the PoS tag can provide additional information for the surronding cues. For the identification procedure of the argument, this feature is able to analyze and generate possible grammatical patterns. For example in "Sybren likes tea", "likes" has two nouns as the left/right most dependent and they correspond to ARG0 and ARG1. It is expected that this relation would be a frequent instance in the data. Another pattern identification example is "Sybren works at the bar", in this case "works" has a noun and a preposition as the rightmost/leftmost dependent. Within the sentence a new argument identification label pattern is generated ARG0 and ARGM-LOC.
-  **Length of list of ancestors and children:** This feature measures how much a token is embedded within the dependency structure, by finding the list of ancestors and children of a target token and by measuring its length. It is expected the argument labels can correlate with this measure and certain argument labels are more likely to have a great length. 
-  **Corresponding predicate of an argument:** Since each argument depends on its predicate, and each predicate does not takes the same types of arguments, it was decided to use it as a feature. This way, it is expected that the classifier would make more accurate predictions.


### 4. Machine Learning Algorithm

The machine learning algorithm chosen for these classification tasks was Support Vector Machines (SVM). SVMs are supervised learning models using learning algorithms that evaluate data for classification and regression analysis in machine learning. Moreover, it can be seen from previous studies on SRL that this one was the most frequently used classifier. The kernel approach allows SVMs to do non-linear classification efficiently by implicitly mapping their inputs into high-dimensional feature spaces.

For the machine learning classification, the features were extracted in a new file with the corresponding gold labels from the duplicated file. It was decided to use all the gold labels and not only the ones corresponding to the arguments and predicates thet were found in the identification procedure. The motivation behind this decision was as it was aimed to train a more general classifier that ideally would be able to capture a larger number of arguments, instead of just relying on the rule-based approached. 

### 5. Summary Table for all the Results Generated 

*Three evaluations: Predicate and argument identification and argument classification*

### 6. Conclusion
### References 

Amjad Abu-Jbara and Dragomir Radev. 2012. Umichigan: A conditional random field model for resolving the
scope of negation. In * SEM 2012: The First Joint Conference on Lexical and Computational Semantics–
Volume 1: Proceedings of the main conference and the shared task, and Volume 2: Proceedings of the Sixth
International Workshop on Semantic Evaluation (SemEval 2012), pages 328–334.

Emanuele Lapponi, Erik Velldal, Lilja Øvrelid, and Jonathon Read. 2012. Uio 2: sequence-labeling negation using
dependency features. In * SEM 2012: The First Joint Conference on Lexical and Computational Semantics–
Volume 1: Proceedings of the main conference and the shared task, and Volume 2: Proceedings of the Sixth
International Workshop on Semantic Evaluation (SemEval 2012), pages 319–327.

Daniel Gildea, Daniel Jurafsky. 2002. Automatic Labeling of Semantic Roles.

Xavier Carreras and Llu´ıs Marquez. 2005. Introduction to the CoNLL-2005 Shared Task: Semantic Role Labeling. Proceedings of the 9th Conference on Computational Natural Language Learning (CoNLL), pages 152–164
