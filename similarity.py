
# -------------------------------------------------------------------------
# AUTHOR: Md Abrar Fahim - ID: 015665234
# FILENAME: similarity.py
# SPECIFICATION: Printing the highest cosine similarity
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: 4 days (did not calculated like exactly, just guessing)
# -----------------------------------------------------------*/
# Importing some Python libraries
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
# Defining the documents
doc1 = "soccer is my favorite sport"
doc2 = "I like sports and my favorite one is soccer"
doc3 = "support soccer at the olympic games"
doc4 = "I do like soccer, my favorite sport in the olympic games"
# Use the following words as terms to create your document-term matrix
# [soccer, favorite, sport, like, one, support, olympic, games]
# --> Add your Python code here
words = ["soccer", "favorite", "sport", "like", "one", "support", "olympic", "games"]

def document_term_matrix(*docs):
    matrix = np.zeros((len(docs), len(words)))
    for i, doc in enumerate(docs):
        for j, term in enumerate(words):
            matrix[i, j] = doc.split().count(term)
            
    return matrix


# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
only
# Use cosine_similarity([X, Y, Z]) to calculate the pairwise similarities between
multiple vectors
# --> Add your Python code here
def highest_cosine_similarity(matrix):
    similarities = cosine_similarity(matrix)
    
    np.fill_diagonal(similarities, -1) 
    max_similarity = np.max(similarities)
    idx_max = np.argmax(similarities)
    row, col = np.unravel_index(idx_max, similarities.shape)
    
    return row, col, max_similarity

matrix = document_term_matrix(doc1, doc2, doc3, doc4)

row, col, max_similarity = highest_cosine_similarity(matrix)

# Print the highest cosine similarity following the information below
# The most similar documents are: doc1 and doc2 with cosine similarity = x
# --> Add your Python code here
print(f"The most similar documents are: doc{row+1} and doc{col+1} with cosine similarity = {max_similarity:.4f}")
