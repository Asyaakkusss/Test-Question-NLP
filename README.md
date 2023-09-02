The purpose of this readme is to walk you through the code and demonstrate how it corresponds to the expectations delineated in the test question.

## Step 1
The expectations for the first step were as follows: 

```
1. **Data Cleaning**: Initiate your study by adopting suitable data preprocessing techniques to
ensure the dataset is clean and accurate for further analysis. Please outline the specific
methodologies employed and justify your decisions where necessary.
```

In order to clean the data in preparation for NLP analysis, I employed 6 methods: 

```
1. I put the CSV file contents into a data frame for easier manipulation
2. I removed the authors and title column from the data frame
3. I removed the month and day from the publication date column, leaving only the publication year
4. I lowercased all the text
5. I removed punctuation and non-ASCII characters
6. I removed stop words
7. I tokenized the abstracts into words using nltk word_tokenize method since we are analyzing
for keywords (as opposed to paragraphs or sentences)
8. I used the WordNet Lemmatizer to reduce the tokenized words to their base forms. WordNet Lemmatizer is
one of the go-tos  
```

## Step 2 and Step 3
The expectations for steps 2 and 3 were as follows: 
2. **Natural Language Processing**: Once the data is in a suitable state, employ relevant NLP
methodologies to generate keywords from the abstracts. Discuss the chosen approach and its
effectiveness.
3. **Data Analysis and Clustering**: Subsequently, perform a cluster analysis to group the
papers based on their publication year and the extracted keywords. Document the algorithm
you have selected for clustering and its justifications.