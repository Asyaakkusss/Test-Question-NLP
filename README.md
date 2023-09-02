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

```
2. **Natural Language Processing**: Once the data is in a suitable state, employ relevant NLP
methodologies to generate keywords from the abstracts. Discuss the chosen approach and its
effectiveness.
3. **Data Analysis and Clustering**: Subsequently, perform a cluster analysis to group the
papers based on their publication year and the extracted keywords. Document the algorithm
you have selected for clustering and its justifications.
```
I decided to tackle these two steps more simultaneously with the following steps: 

```
1. I grouped the data by year for my clustering analysis. I then divided them up into 9 data frames for every year that was represented on the original data frame (2010 - 2018). I separated them into different data frames so that the TF-IDF scores I would calculate for each keyword would not be influenced by the frequency of that same word occurring in other years. 

2. I decided to go with TF-IDF analysis and created another set of data frames with key words from each abstract and each word's TF-IDF score. TF-IDF analysis is effective because the score determines the relevance of the 
words. The higher the score, the greater the frequency of the word in the abstract. The TF-IDF data can then be fed into visual aids such as charts, graphs, and word clouds. 
```
## Steps 4 and 5

```
4. **Findings and Trend Analysis**: Identify and discuss your findings, with a special emphasis
on the trends in keyword usage over the years. Make sure to substantiate your conclusions
with evidence from the data.
5. **Data Visualization**: To support your findings, create a compelling and appropriate data
visualization, for example, keywords network graph, that clearly illustrates the trends you
have identified.
```
I used a wordcloud to visualize each of the data clusters. In the first four tiles, there seems to be a lot of keywords that indicate investigation/discovery of problems, such as "addressing", "algorithm", "adapting", "amended", etc. In the last 5 tiles, there are more keywords that indicate progress/applicability and development, such as "achievement", "develop", "achieve", "accelerate", and "absorb". There are also more keywords indicating technical terms and processes. This would make sense since over time these methods would be developed and applied with greater frequency. 
