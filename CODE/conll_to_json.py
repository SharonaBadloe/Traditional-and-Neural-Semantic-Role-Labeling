import pandas as pd
import json
import os
import sys

infile = sys.argv[1]
duplicate = sys.argv[2]
outfile = infile.replace('conll','jsonl')

def read_and_split_newline(infile):
    """
    Takes the path to the conll file and returns a list split on newline

    Parameters: infile:string
    Returns: split_on_newline:list
    """
    with open(infile, "r") as f:
        sentences = f.read().split('\n\n')

    # splits on newline and appends to new list
    split_on_newline = []
    for sentence in sentences:
        split_on_newline.append(sentence.split('\n'))
    return split_on_newline

def remove_hashtag(newline_split):
    """
    Takes the infile split on newlines and removes all files that start with a
    hashtag

    Parameters: newline_split:list
    Returns: non_hashtag:list
    """
    # loops over the list of splits and removes all lines that start with #
    non_hashtag = []
    for sentence in newline_split:
        sentence_level = []
        for line in sentence:
            # if it starts with a hashtag, do not append it to the list
            if not line.startswith('#'):
                line = line.rstrip("\t''")
                sentence_level.append(line)
        non_hashtag.append(sentence_level)
    return non_hashtag

def split_on_tab(clean_list):
    """
    Takes the clean list and splits it on tab, then append it to a new list

    Parameters: clean_list:list
    Returns: final:list
    """
    final = []
    for i in clean_list:
        lijstje = []
        for j in i:
            j = j.split('\t')
            lijstje.append(j)
        final.append(lijstje)
    return final

def duplicate(list_of_list_of_lists):
    """
    takes List of list of lists extracted from the conll file
    (containig the sentences) and duplicates the sentences that contain more
    than one predicate

    Parameters: list_of_list_of_lists:list
    Returns: duplicated_sents:list
    """
    # duplicate sentences acording to number of predicates
    # e.g. when sentence has 2 predicates, it will be duplicated twice
    duplicated_sents = []
    for sent in list_of_list_of_lists:
        predicate_nr = len(sent[0]) - 11
        if predicate_nr < 1:
            duplicated_sents.append(sent)
        else:
            try:
                # loop over the amount of arguments and add every argument arguments
                # added to the the final list
                for i in range(predicate_nr):
                    new_sent = []
                    for row in sent:
                        arguments = row[11:]
                        basic = row[:11]
                        basic.append(arguments[i])
                        new_sent.append(basic)
                    duplicated_sents.append(new_sent)
            except:
                pass
    return duplicated_sents

# loop over
def make_json(duplicated_sents):
    """
    Turns the duplicated sentences into a string containing the json format

    Parameters: duplicated_sents:list
    Returns: x:string
    """
    x=' '
    # checks whether user provided True or False
    # False = no duplications, True = duplication
    if duplicate:
        sents = duplicated_sents
    else:
        sents = final

    for i in sents:
        try:
            tokens = []
            bio =[]
            # loop over sentences and add tokens to a list inside of a dict per sentence
            for j in i:
                sentence_dict = {}
                tokens.append(j[1])
                # if element at index 11 is a dash, append an O, otherwise
                # append the element with B- in front of it.
                if j[11] == "_":
                    bio.append("O")
                else:
                    bio.append("B-"+j[11])
            # add everything to the dict per sentence
            sentence_dict['seq_words'] = tokens
            sentence_dict['BIO'] = bio
            # "update" the string with the new sentence dict and add new line
            x += json.dumps(sentence_dict) + '\n'

            # import jsonlines
            # with jsonlines.open('output.jsonl', 'w') as writer:
            #     writer.write_all(sentence_dict)
        except:
            pass
    return x
# write the "json string" to the output file

def main():
    split_newline = read_and_split_newline(infile)
    clean_split_newline = remove_hashtag(split_newline)
    tab_split = split_on_tab(clean_split_newline)
    duplicated_tab_split = duplicate(tab_split)
    json_string = make_json(duplicated_tab_split)

    with open(outfile, 'a') as outputfile:
        outputfile.write(json_string)

if __name__ == "__main__":
    main()
