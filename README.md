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

The natural language processing classification task presented and analysed in this report is Semantic Role Labelling (SRL). Semantic Role labelling is the process of identifying semantic relations between predicates and their related participants and characteristcs (Carreras, 2005). Semantic argument identification and classification are the two subtasks within SRL. In an argument classification task, each syntactic element in a sentence is classified as a semantic argument or a non-argument using semantic argument identification. While semantic argument classification entails categorizing each semantic argument into one of several semantic roles, such as ARG0, ARG1, and so on. A great number of features that can capture the syntactic environment of the semantic argument will be proposed in the following section. The aim of this report is to present the creation of a machine learning algorithm system that can identify verb arguments in a sentence and classify them with their semantic role. 


### 2.Identification and Extraction 
  ### 2.1 Rule-based Predicates 
  
To identify and extract the predicates a rule-based approached was used. The first step of the procedure was to read and load the given dataset using the external package, pandas. Then the dataset was combined with an external library SpaCy to process the data. After analyzing the columns within the dataset, it was decided that the relevant column for the predicate identification was XPOS. This column contained POS tag abbreviations that preserved the original value of the dataset with manual annotation and corrections. As predicates tend to refer to verbs it was decided that the rule to identify the predicates will be: if the XPOS tag of a token is one of the following: VBP, VBD, VBZ, VBN, and VB then it is a predicate. These labels cover both regular and irregular forms (inflection and derivation) of the verb. Every instance that was detected with the chosen abbreviation was labels as “PRED”. After the identification process was done all predicated were extracted and stored in a new dataset. Finally, the corresponding gold label for each predicate was also extracted for evaluation reasons. 

  ### 2.2 Rule-based Arguments 

In terms of the argument identification and extraction a rule-based approached was also followed. In order to generate and implement rules for the identification the dataset was analysed in order to identify possible patterns. Six syntactic patterns were identified and were used as the rules for the the identification was conducted,(1) if the dependence is a subject or a prepositional object with the preposition “by”, (2) objects in active sentences, (3) subjects in passive sentences, (4) to + prepositional objects, (5) dative verbs, (6) Frequently used adjectives: now, how, already. All instances that followed any of the rules was classified as "ARG" and was stored in a new dataset that would contained all the results from the identification procedure. The same step as the predicate procedure was followed and all gold labels were extracted for evaluation. 

### 4.Features 

The following table gives an overview of all the features selected in order to carry out the classification tasks. The procedure of implementing the features as well as the motivation behind the selection will be described in greater detail in the following sections. 

| Baseline Features       | Dataset Features          | Advanced Features  |
| :-------------: |:-------------:| :-----:|
| Token      | Morphological Features |Head |
| Lemma      | Dependency Relation      | Voice|
| POS | Token     |  Position   |
| N-grams |  Lemma  | Form-POS on leftmost/rightmost dependent |
| | |Form-POS left sibling of the argument |
 

### 4.1 Baseline Features 
The aim of this report is to implement basic features evaluating local information in the context of the term or element under consideration, and report characteristics of a candidate argument's internal structure. Moreover these features should provide characteristics of the target verb predicate's characteristics and of the verb predicate's relations with the component under examination.The features chosen for the baseline system are: token, lemma, POS tags, n-grams and binary representation.

The most common and most simple features are lemma and token. A token is “the word or the punctuation mark as it appears in the sentence” (Abu-Jbara and Radev, 2012, p.331) while a lemma is the root form of a token (ibid); for instance, the word “undivided” within a sentence is a token and “divide” would be the corresponding lemma. They both are beneficial because they divide the text data into pieces and thus make it easier for the classifier to distinguish. Apart from lemmatization and tokenization, Part of Speech (POS), is also a commonly used feature in NLP tasks. POS is used in order to connect a token in text data to its grammatical definition.  To improve the performance of these features, since some predicates  may consist of multiple words, it can be helpful to include additional features that look at the surrounding cues, for instance, previous token, previous lemma, or n-grams (citation). The feature n-gram is used to look at the left and/or right candidate cues (Lapponi et al., 2012) and can be used on a token-, a word-, or a sentence-level.

### 4.2 Features already adapted in the dataset  
A great anumber of features were already implemented in the dataset provided for this specific task. The data contained some morphological features. The morphological structure of a word is a crucial component for high-level semantic analysis tasks. Due to the fact morphology is the study of the structure and derivation of complex signals, it can concentrate on the semantic aspect. For example, the construction of complex concepts and structural (composition of complex names for concepts) aspects, as well as the relationship between them (Levin, 2017). Dependency relation 

### 4.3 Advanced Features 
 In combination with the baseline features an advance selection was additionally made. Based on previous research conducted it can be seen that the most common advanced features used were: voice of verb, child of the token,the start and end of the token constituent as well as the position of the argument with respect to the predicate. Regarding the target verb, the voice feature of the verb is generally used as it is able to identify if the predicate is passive or active. The voice of the verb refers to the relationship of the subject and the action. The direct objects of active verbs frequently correspond in semantic role to subjects of passive verbs, the distinction between active and passive verbs is crucial in the relationship between semantic role and grammatical function (Gildea, 2002). The position of the argument with repsect to the predicate (left / right English)
 Additionally to the dependency relation, the child of the predicate was implemented as an advanced feature. Each sentence consists of multiple tokens, and those tokens are syntactically or grammatically dependent on each other. For example, in the sentence “My dad gave me an apple”,the root “gave” has children which are parents of their own children (fiinl, 2019). 

### 5.Machine learning algorithm

The machine learning algorithm chosen for these calssification tasks was support vector machines (SVM). Support-vector machines are supervised learning models using
learning algorithms that evaluate data for classification and regression analysis in machine learning. Moreover, it can be seeen from previous studies on SRL that the most frequently used classifier was SVM. Among the numerous classification algorithms, SVM most often used. The kernel approach allows SVMs to do non-linear classification efficiently by implicitly mapping their inputs into high-dimensional feature spaces.

### 6.Summary table for all the results generated 
      |         |   |
| :-------------: |:-------------:| :-----:|
|  |  | |
|   |  | |
|  |   |   |
|  |  | |
| | | |
### 7. Conclusion
### References 
