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

### 1.Introduction

Semantic role labeling (SRL) has gotten a lot of attention in recent years and has become a crucial component in all kinds of natural language applications. In NLP, semantic role labeling is the process of to identifying and describing the semantic relationships that exist between a predicate and its related participants and characteristics drawn from a pre-specified list of possible semantic roles for that predicate (agent, patient, etc) (Carreras, 2005). 

The main aim of this report is to present the creation of a machine learning system that could recognize verb arguments in a sentence and label them with their semantic role.The following sections will describe in greater detail the steps needed to create the machine learning system as well as the evaluation process.

### 2.Predicate Extraction 
The first step for the extraction was to analyse the given dataset and investigate which elements could potentially be useful for the conducted task. The dataset contained multiple columns, after discussion it was decided that the relevant column for the predicate extraction is XPOS. This column contained POS tag abbreviations that preserved the original value of the dataset with manual annotation and corrections. As a first step of the extraction all tags that started with a “V” were generated from the column and checked to see if they were predicates. From the extraction it was evident that the only abbreviation label that was always marked as a predicate was “VBP”. The researchers decided to extract all predicates under that label and create a sample data with 700 predicates for the following steps.

### 3.Description of classification task for argument classification 

Semantic role labeling can be divided into two subtasks: semantic argument identification and semantic argument classification. In a argument classififcation task each syntactic element in a sentence is classified as a semantic argument or a non-argument using semantic argument identification. In this case a syntactic element might be a single word in a sentence, or a group of words. Semantic argument classification entails categorizing each semantic argument into one of several semantic roles, such as ARG0, ARG1, and so on. A great amount of features that are able to capture the syntactic enviroment of the semantic argument will be proposed in the following section. 


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
