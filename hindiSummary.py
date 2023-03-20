import string
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import networkx as nx
import numpy as np
import nltk
import re


### Hindi Summarization:
def remove_redundant_sentences(sentences):
    cleaned=[]
    for s in sentences:
        if s in cleaned or s.strip()=='':
            continue
        else:
            cleaned.append(s)
    return cleaned

def clean_corpus(corpus):
    corpus=corpus.replace('।','.')
    corpus=corpus.replace('\xa0','')
    corpus=corpus.replace('\n','')
    corpus=corpus.replace('\r','')
    return corpus

def get_clean_sentences(doc):
    cleaned_doc=clean_corpus(doc)
    sentences=cleaned_doc.split('.')
    sentences=remove_redundant_sentences(sentences)
    return sentences


def preprocess_textrank(text):
    formatted_text = re.sub(r'\s+', ' ', text)
    formatted_text = formatted_text.lower()
    tokens = []
    for token in nltk.word_tokenize(formatted_text):
        tokens.append(token)
    tokens = [word for word in tokens if word not in stopwords and word not in string.punctuation]
    formatted_text = ' '.join(element for element in tokens)

    return formatted_text

def calculate_sentence_similarity(sentence1, sentence2):
    words1 = [word for word in nltk.word_tokenize(sentence1)]
    words2 = [word for word in nltk.word_tokenize(sentence2)]
    all_words = list(set(words1 + words2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for word in words1:
        vector1[all_words.index(word)] += 1
    for word in words2:
        vector2[all_words.index(word)] += 1
    return 1 - cosine_distance(vector1, vector2)


def calculate_similarity_matrix(sentences):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    #print(similarity_matrix)
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i == j:
                continue
            similarity_matrix[i][j] = calculate_sentence_similarity(sentences[i], sentences[j])
    return similarity_matrix


def summarize(clean_sentences, percentage = 0):
  #original_sentences=sentence_tokenize.sentence_split(original_text, lang='hi')
  #formatted_sentences = [preprocess(original_sentence) for original_sentence in original_sentences]
    similarity_matrix = calculate_similarity_matrix(clean_sentences)

    similarity_graph = nx.from_numpy_array(similarity_matrix)

    scores = nx.pagerank(similarity_graph)
    ordered_scores = sorted(((scores[i], score) for i, score in enumerate(clean_sentences)), reverse=True)
    number_of_sentences=int(len(clean_sentences))
    if percentage > 0:
        number_of_sentences = int(len(clean_sentences) * percentage)

    best_sentences = []
    for sentence in range(number_of_sentences):
        best_sentences.append(ordered_scores[sentence][1])

    return best_sentences, ordered_scores


def generate_summary_textrank(clean_sentences,best_sentences):
    sent_dict={}
    ordered_list_of_sentences=[]
    for sent in clean_sentences:
        if sent[:15] in sent_dict:
            pass
        else:
            sent_dict[sent[:15]]=sent
            ordered_list_of_sentences.append(sent)
    summary_text=""
    for sent in ordered_list_of_sentences:
        if sent in best_sentences:
            summary_text+=sent+". "
    return summary_text

##### End of Hindi Summarization #####









# Hindi Summary

# def preprocess_tokenize(text):
#     text = str(text)
#     text = re.sub(r'(\d+)', r'', text)
#
#     text = text.replace('\n', '')
#     text = text.replace('\r', '')
#     text = text.replace('\t', '')
#     text = text.replace('\u200d', '')
#     text = re.sub("(__+)", ' ', str(text)).lower()
#     text = re.sub("(--+)", ' ', str(text)).lower()
#     text = re.sub("(~~+)", ' ', str(text)).lower()
#     text = re.sub("(\+\++)", ' ', str(text)).lower()
#     text = re.sub("(\.\.+)", ' ', str(text)).lower()
#
#     text = re.sub(r"[<>()|&©@#ø\[\]\'\",;:?.~*!]", ' ', str(text)).lower()  # remove <>()|&©ø"',;?~*!
#     text = re.sub("([a-zA-Z])", ' ', str(text)).lower()
#     text = re.sub("(\s+)", ' ', str(text)).lower()
#
#     return text