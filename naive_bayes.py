# naive_bayes.py
# ---------------
# Licensing Information:  You are free to use or extend this projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to the University of Illinois at Urbana-Champaign
#
# Created by Justin Lizama (jlizama2@illinois.edu) on 09/28/2018
# Last Modified 8/23/2023


"""
This is the main code for this MP.
You only need (and should) modify code within this file.
Original staff versions of all other files will be used by the autograder
so be careful to not modify anything else.
"""


import reader
import math
from tqdm import tqdm
from collections import Counter


'''
util for printing values
'''
def print_values(laplace, pos_prior):
    print(f"Unigram Laplace: {laplace}")
    print(f"Positive prior: {pos_prior}")

"""
load_data loads the input data by calling the provided utility.
You can adjust default values for stemming and lowercase, when we haven't passed in specific values,
to potentially improve performance.
"""
def load_data(trainingdir, testdir, stemming=False, lowercase=False, silently=False):
    print(f"Stemming: {stemming}")
    print(f"Lowercase: {lowercase}")
    train_set, train_labels, dev_set, dev_labels = reader.load_dataset(trainingdir,testdir,stemming,lowercase,silently)
    return train_set, train_labels, dev_set, dev_labels


"""
Main function for training and predicting with naive bayes.
    You can modify the default values for the Laplace smoothing parameter and the prior for the positive label.
    Notice that we may pass in specific values for these parameters during our testing.
"""
def naive_bayes(train_set, train_labels, dev_set, laplace=0.1, pos_prior=0.9, silently=False):
    print_values(laplace,pos_prior)

    pos_word_counts = Counter()
    neg_word_counts = Counter()
    pos_total_words = 0
    neg_total_words = 0
    
    for doc, label in zip(train_set, train_labels):
        if label == 1: 
            pos_word_counts.update(doc)
            pos_total_words += len(doc)
        else:  
            neg_word_counts.update(doc)
            neg_total_words += len(doc)
    
    vocabulary = set(pos_word_counts.keys()) | set(neg_word_counts.keys())
    vocab_size = len(vocabulary)
    
    if not silently:
        print(f"Positive documents: {sum(train_labels)}")
        print(f"Negative documents: {len(train_labels) - sum(train_labels)}")
        print(f"Total positive words: {pos_total_words}")
        print(f"Total negative words: {neg_total_words}")
        print(f"Vocabulary size: {vocab_size}")

    pos_word_probs = {}
    neg_word_probs = {}
    
    for word in vocabulary:
        pos_word_probs[word] = (pos_word_counts[word] + laplace) / (pos_total_words + laplace * vocab_size)
        neg_word_probs[word] = (neg_word_counts[word] + laplace) / (neg_total_words + laplace * vocab_size)
    
    pos_prior_prob = pos_prior
    neg_prior_prob = 1 - pos_prior
    
    if not silently:
        print(f"Calculated probabilities for {len(vocabulary)} words")
        print(f"Positive prior: {pos_prior_prob}")
        print(f"Negative prior: {neg_prior_prob}")

    yhats = []
    for doc in tqdm(dev_set, disable=silently):
        log_prob_pos = math.log(pos_prior_prob)
        log_prob_neg = math.log(neg_prior_prob)
        
        for word in doc:
            if word in vocabulary: 
                log_prob_pos += math.log(pos_word_probs[word])
                log_prob_neg += math.log(neg_word_probs[word])
        
        prediction = 1 if log_prob_pos > log_prob_neg else 0
        yhats.append(prediction)

    return yhats
