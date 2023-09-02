import pandas as pd 
import re
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import word_tokenize
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud


nltk.download('stopwords')

#we read the data from the csv
data = pd.read_csv('C:\\Users\\asyas\\Downloads\\test_question.csv')

#now, we clean the data 
'''
1. **Data Cleaning**: Initiate your study by adopting suitable data preprocessing techniques to
ensure the dataset is clean and accurate for further analysis. Please outline the specific
methodologies employed and justify your decisions where necessary.
'''

'''
What I have done to clean the data: 
1. Removed the authors column, since it is not very relevant to the task at hand (done)
2. Removed the month and day from the publication date, leaving only the year (done)
3. Lowercased all text (done)
4. Removed punctuation (done)
5. Removed stop words (done)
6. Used stemming to reduce the words to their most basic root forms
'''

array = data[['title', 'abstract', 'date', 'authors']].values

#convert the array into a dataframe 
data_frame = pd.DataFrame(array, columns = ['title', 'abstract', 'date', 'authors'])

#remove the authors column from the data table 
data_frame = data_frame.drop('authors', axis=1)

#remove the month and day from publication date 
data_frame['date'] = pd.to_datetime(data_frame['date'])
data_frame['year'] = data_frame['date'].dt.year
data_frame = data_frame.drop('date', axis=1)

#lowercase all text
data_frame['title'] = data_frame['title'].apply(str.lower)
data_frame['abstract'] = data_frame['abstract'].apply(str.lower)

#remove punctuation and non-ASCII characters
data_frame['title'] = data_frame['title'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', re.sub(r'[.,-:]', '', x)))
data_frame['abstract'] = data_frame['abstract'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', re.sub(r'[.,-:]', '', x)))

#remove stop words 
stop_words = set(stopwords.words('english'))
data_frame['title'] = data_frame['title'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
data_frame['abstract'] = data_frame['abstract'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

#use stemming 
#stemmer = LancasterStemmer()
#data_frame['title'] = data_frame['title'].apply(lambda x: [stemmer.stem(word) for word in x])
#data_frame['abstract'] = data_frame['abstract'].apply(lambda x: [stemmer.stem(word) for word in x])

'''
2. **Natural Language Processing**: Once the data is in a suitable state, employ relevant NLP
methodologies to generate keywords from the abstracts. Discuss the chosen approach and its
effectiveness.

For this section, I used TF-IDF to extract keywords from each abstract after splitting the initial 
data table up into different years. 
'''
grouped = data_frame.groupby('year')

# Create a dictionary of DataFrames, where each key is a unique year
frames_by_year = {year: group for year, group in grouped}

data_frame_2010 = frames_by_year.get(2010) 
data_frame_2011 = frames_by_year.get(2011) 
data_frame_2012 = frames_by_year.get(2012)
data_frame_2013 = frames_by_year.get(2013) 
data_frame_2014 = frames_by_year.get(2014) 
data_frame_2015 = frames_by_year.get(2015) 
data_frame_2016 = frames_by_year.get(2016) 
data_frame_2017 = frames_by_year.get(2017) 
data_frame_2018 = frames_by_year.get(2018) 

# using TF-IDF to extract keywords 
vectorization = TfidfVectorizer()

# for 2010
vectorization.fit(data_frame_2010['abstract'])
tfidf_2010= vectorization.transform(data_frame_2010['abstract'])
tfidf_2010_dataframe = tfidf_df = pd.DataFrame(tfidf_2010.toarray(), columns=vectorization.get_feature_names_out())

# for 2011
vectorization.fit(data_frame_2011['abstract'])
tfidf_2011 = vectorization.transform(data_frame_2011['abstract'])
tfidf_2011_dataframe = tfidf_df = pd.DataFrame(tfidf_2011.toarray(), columns=vectorization.get_feature_names_out())

# for 2012
vectorization.fit(data_frame_2012['abstract'])
tfidf_2012= vectorization.transform(data_frame_2012['abstract'])
tfidf_2012_dataframe = tfidf_df = pd.DataFrame(tfidf_2012.toarray(), columns=vectorization.get_feature_names_out())

# for 2013
vectorization.fit(data_frame_2010['abstract'])
tfidf_2010= vectorization.transform(data_frame_2010['abstract'])
tfidf_2010_dataframe = tfidf_df = pd.DataFrame(tfidf_2010.toarray(), columns=vectorization.get_feature_names_out())

# for 2014

# for 2015

# for 2016

# for 2017

# for 2018 

#create a word cloud 
data_2010 = " ".join(tfidf_2010_dataframe.columns)
wordcloud2010 = WordCloud(width=400, height=400, background_color = "white").generate(data_2010)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud2010, interpolation='bilinear')
plt.axis('off')
plt.show()