import pandas as pd
import json
import os
import sys

infile = sys.argv[1]
outfile = infile.replace('conll','.duplicated.conll')

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

def sentences_to_string(duplicated_sents):
    """
    Turns the duplicated sentences into a string containing in csv format

    Parameters: duplicated_sents:list
    Returns: joined_text:string
    """
    joined_sents = []
    for sent in duplicated_sents:
        for line in sent:
            joined_line = '\t'.join(line)
            joined_sents.append(joined_line)
    joined_text = '\n'.join(joined_sents)
    return joined_text

def main():
    split_newline = read_and_split_newline(infile)
    clean_split_newline = remove_hashtag(split_newline)
    tab_split = split_on_tab(clean_split_newline)
    duplicated_tab_split = duplicate(tab_split)
    csv_string = sentences_to_string(duplicated_tab_split)

    with open(outfile, 'a') as outputfile:
        outputfile.write(csv_string)

if __name__ == "__main__":
    main()
