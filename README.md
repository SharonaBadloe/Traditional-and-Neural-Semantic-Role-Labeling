# Advanced NLP Assignment 2: Traditional and Neural Semantic Role Labeling

The project was carried out by Giorgio Malinverni, Sharona Badloe, Sybren MOolhuizen and Konstantina Andronikou during the seminar NLP Technology taugh by Antske Fokkens and Pia Sommerauer.

This README contains the infromation to run a classifier that performs Semantic Role Labeling (SRL). This work is divided into two parts:
* `Part 1: Traditional SRL`
* `Part 2: Neural SRL`

### Data
Development Data:
* `en_ewt-up-dev.conllu`

Training Data:
* `en_ewt-up-train.conllu`

Test Data:
* `en_ewt-up-test.conllu`

### Code 
The folder [**code**](https://github.com/gioguitar99/NLP_Assignment_2/tree/main/Code) consists the following script:
* `main.py` This file carries out the entire experiment (feature extraction,
training, testing)

### Results 
The folder [**results**](https://github.com/gioguitar99/NLP_Assignment_2/tree/main/Results) consists of the output files of the following components:
* `Output of identification for predicates and arguments`
* `Feature Extraction`
* `Basic Evaluation`

### Part 1: Traditional SRL

### 1. Introduction 

The natural language processing classification task presented and analysed in this report is Semantic Role Labelling (SRL). Semantic Role labelling is the process of identifying semantic relations between predicates and their related participants and characteristcs (Carreras, 2005). Semantic argument identification and classification are the two subtasks within SRL. In an argument classification task, each syntactic element in a sentence is classified as a semantic argument or a non-argument using semantic argument identification. While semantic argument classification entails categorizing each semantic argument into one of several semantic roles, such as ARG0, ARG1, and so on. The aim of this report is to present the creation of a machine learning algorithm system that can identify verb arguments in a sentence and classify them with their semantic role. 


### 2.Identification and Extraction 
  ### 2.1 Rule-based Predicates 
  
To identify and extract the predicates a rule-based approached was used. The first step of the procedure was to read and load the given dataset using the external package, pandas. Then the dataset was combined with an external library SpaCy to process the data. After analyzing the columns within the dataset, it was decided that the relevant column for the predicate identification was XPOS. This column contained POS tag abbreviations that preserved the original value of the dataset with manual annotation and corrections. As predicates tend to refer to verbs it was decided that the rule to identify the predicates will be: if the XPOS tag of a token is one of the following: VBP, VBD, VBZ, VBN, and VB then it is a predicate. These labels cover both regular and irregular forms (inflection and derivation, such as 3rd person, tense, affixes) of the verb. Every instance that was detected with the chosen abbreviation was labels as “PRED”. After the identification process was done, all predicates were extracted and stored in a new dataset with the corresponding gold label for each predicate. The extracted predicates and the gold labels are then used to evaluate this sub-task. 

  ### 2.2 Rule-based Arguments 

In terms of the argument identification and extraction a rule-based approached was also followed. In order to generate and implement rules for the identification, the dataset was analysed in order to identify possible patterns. Six syntactic patterns were identified and were used as the rules for the identification process: (1) if the dependence is a subject or a prepositional object with the preposition “by”; (2) objects in active sentences; (3) subjects in passive sentences; (4) to + prepositional objects; (5) dative verbs; (6) frequently used adjectives: now, how, already. All instances that followed any of the rules were classified as "ARG" and were stored in a new dataset with the corresponding gold labels. The process was then evaluated.

### 3. Features 

The following table gives an overview of all the features selected to carry out the classification tasks. The procedure of implementing the features as well as the motivation behind the selection will be described in greater detail in the following sections.  

| Baseline Features       | Dataset Features          | Advanced Features  |
| :-------------: |:-------------:| :-----:|
| Token      | Morphological Features |Token head of a target token |
| Lemma      | Dependency Relation      | Pos head of a target token|
| POS | Token   | Voice |
| Bigram (target+next)|  Lemma  | Form-POS on leftmost/rightmost dependent |
| Trigram (target+2 next)| |Form-POS left sibling of the argument |
| Postag bigram| |List of ancestors |
| Postag trigram| |List of children |
| | |Lenght of lists (ancestors and children) |
 

### 3.1 Baseline Features 

The aim of this report is to implement a variety of features that can capture the information requested to correctly carry out the classification process. Before, presenting the features chosen for this research, it is worth mentioning that the dataset provided for this specific task had already some features implemented.The data contained both syntactic and morphological features (token, lemma, dependency relation).

The features chosen for the baseline system are: token, lemma, POS tags, token bigram/trigrams and POS bigram/trigram):
- Token/lemma: Token is "the word or the punction mark as it appears in the sentence" (Abu-Jbara and Radev, 2012, p.331) while lemma is the root of the token. Token and Lemma in terms of a classification task can be beneficial as the text is divided into pieces thus it can make the process of analyzing and training a classifier easier. 
- PoS tag: It is used to connect a token in text data to its grammatical definition. In a semantic role labelling task it can be useful since some arguments are more likley to correspond to a specific PoS category (e.g. the agent, ARG0, is likely to be a noun).
- Token bigram/trigram: Token bigram and trigram are used to look at the surrondings cues of the token (e.g. previous or next token) (Lapponi et al., 2012). This can be helpful in the identification and classification procedure as it can idenfity potential syntactic patterns. 
- PoS tag of the bigram/trigram: As the previous feature can be helpful to identify patterns within the dataset the POS tag of the trigram and bigram will give a better understanding of their grammatical definition. 
 


### 3.2 Advanced Features 

In combination with the baseline features an advance selection was additionally made. This selection was strongly motivated form previous research done on SRL. The following list of features were implemented:

- Token head of target token: The head of the target 
- POS head of the target token:
- Voice: it is able to identify if the predicate is passive or active. The voice of the verb refers to the relationship of the subject and the action (Gildea, 2002). 
- Form/POS of the left most/rightmost dependent: 
- Form/POS of the left sibling of the argument:
-  List of ancestors:
-  List of children:
-  Length of lists:

### 4.Machine learning algorithm

The machine learning algorithm chosen for these calssification tasks was support vector machines (SVM). Support-vector machines are supervised learning models using
learning algorithms that evaluate data for classification and regression analysis in machine learning. Moreover, it can be seeen from previous studies on SRL that the most frequently used classifier was SVM. Among the numerous classification algorithms, SVM most often used. The kernel approach allows SVMs to do non-linear classification efficiently by implicitly mapping their inputs into high-dimensional feature spaces.

### 6.Summary table for all the results generated 

Three evaluations: Predicate and argument identification and argument classification 

### 7. Conclusion
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
