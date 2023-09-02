import pandas as pd 
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud


nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

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
'''

array = data[['title', 'abstract', 'date', 'authors']].values

#convert the array into a dataframe 
data_frame = pd.DataFrame(array, columns = ['title', 'abstract', 'date', 'authors'])

#remove the authors and title column from the data table 
data_frame = data_frame.drop('authors', axis=1)
data_frame = data_frame.drop('title', axis=1)

#remove the month and day from publication date 
data_frame['date'] = pd.to_datetime(data_frame['date'])
data_frame['year'] = data_frame['date'].dt.year
data_frame = data_frame.drop('date', axis=1)

#lowercase all text
data_frame['abstract'] = data_frame['abstract'].apply(str.lower)

#remove punctuation and non-ASCII characters
data_frame['abstract'] = data_frame['abstract'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', re.sub(r'[.,-:]', '', x)))

#remove stop words 
stop_words = set(stopwords.words('english'))
data_frame['abstract'] = data_frame['abstract'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

#tokenize 
data_frame['abstract'] = data_frame['abstract'].apply(lambda x: ' '.join(word_tokenize(x)))

#stem
stemmer = WordNetLemmatizer()
data_frame['abstract'] = data_frame['abstract'].apply(lambda x: ' '.join([stemmer.lemmatize(word) for word in x.split()]))

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
tfidf_2010_dataframe = pd.DataFrame(tfidf_2010.toarray(), columns=vectorization.get_feature_names_out())

# for 2011
vectorization.fit(data_frame_2011['abstract'])
tfidf_2011 = vectorization.transform(data_frame_2011['abstract'])
tfidf_2011_dataframe = pd.DataFrame(tfidf_2011.toarray(), columns=vectorization.get_feature_names_out())

# for 2012
vectorization.fit(data_frame_2012['abstract'])
tfidf_2012= vectorization.transform(data_frame_2012['abstract'])
tfidf_2012_dataframe = pd.DataFrame(tfidf_2012.toarray(), columns=vectorization.get_feature_names_out())

# for 2013
vectorization.fit(data_frame_2010['abstract'])
tfidf_2013= vectorization.transform(data_frame_2013['abstract'])
tfidf_2013_dataframe = pd.DataFrame(tfidf_2013.toarray(), columns=vectorization.get_feature_names_out())

# for 2014
vectorization.fit(data_frame_2014['abstract'])
tfidf_2014= vectorization.transform(data_frame_2014['abstract'])
tfidf_2014_dataframe = pd.DataFrame(tfidf_2014.toarray(), columns=vectorization.get_feature_names_out())

# for 2015
vectorization.fit(data_frame_2015['abstract'])
tfidf_2015= vectorization.transform(data_frame_2015['abstract'])
tfidf_2015_dataframe = pd.DataFrame(tfidf_2015.toarray(), columns=vectorization.get_feature_names_out())

# for 2016
vectorization.fit(data_frame_2016['abstract'])
tfidf_2016= vectorization.transform(data_frame_2016['abstract'])
tfidf_2016_dataframe = pd.DataFrame(tfidf_2016.toarray(), columns=vectorization.get_feature_names_out())

# for 2017
vectorization.fit(data_frame_2017['abstract'])
tfidf_2017= vectorization.transform(data_frame_2017['abstract'])
tfidf_2017_dataframe = pd.DataFrame(tfidf_2017.toarray(), columns=vectorization.get_feature_names_out())

# for 2018 
vectorization.fit(data_frame_2018['abstract'])
tfidf_2018= vectorization.transform(data_frame_2018['abstract'])
tfidf_2018_dataframe = tfidf_df = pd.DataFrame(tfidf_2018.toarray(), columns=vectorization.get_feature_names_out())

#create a word cloud 
fig, axes = plt.subplots(3, 3, figsize=(12, 12))
axes = axes.ravel()

data_2010 = " ".join(tfidf_2010_dataframe.columns)
data_2011 = " ".join(tfidf_2011_dataframe.columns)
data_2012 = " ".join(tfidf_2012_dataframe.columns)
data_2013 = " ".join(tfidf_2013_dataframe.columns)
data_2014 = " ".join(tfidf_2014_dataframe.columns)
data_2015 = " ".join(tfidf_2015_dataframe.columns)
data_2016 = " ".join(tfidf_2016_dataframe.columns)
data_2017 = " ".join(tfidf_2017_dataframe.columns)
data_2018 = " ".join(tfidf_2018_dataframe.columns)

wordcloud2010 = WordCloud(width=400, height=400, background_color = "white").generate(data_2010)
wordcloud2011 = WordCloud(width=400, height=400, background_color = "white").generate(data_2011)
wordcloud2012 = WordCloud(width=400, height=400, background_color = "white").generate(data_2012)
wordcloud2013 = WordCloud(width=400, height=400, background_color = "white").generate(data_2013)
wordcloud2014 = WordCloud(width=400, height=400, background_color = "white").generate(data_2014)
wordcloud2015 = WordCloud(width=400, height=400, background_color = "white").generate(data_2015)
wordcloud2016 = WordCloud(width=400, height=400, background_color = "white").generate(data_2016)
wordcloud2017 = WordCloud(width=400, height=400, background_color = "white").generate(data_2017)
wordcloud2018 = WordCloud(width=400, height=400, background_color = "white").generate(data_2018)

axes[1].imshow(wordcloud2011, interpolation='bilinear')
axes[1].set_title("2011")
axes[1].axis('off')

axes[2].imshow(wordcloud2012, interpolation='bilinear')
axes[2].set_title("2012")
axes[2].axis('off')

axes[3].imshow(wordcloud2013, interpolation='bilinear')
axes[3].set_title("2013")
axes[3].axis('off')

axes[4].imshow(wordcloud2014, interpolation='bilinear')
axes[4].set_title("2014")
axes[4].axis('off')

axes[5].imshow(wordcloud2015, interpolation='bilinear')
axes[5].set_title("2015")
axes[5].axis('off')

axes[6].imshow(wordcloud2016, interpolation='bilinear')
axes[6].set_title("2016")
axes[6].axis('off')

axes[7].imshow(wordcloud2017, interpolation='bilinear')
axes[7].set_title("2017")
axes[7].axis('off')

axes[8].imshow(wordcloud2018, interpolation='bilinear')
axes[8].set_title("2018")
axes[8].axis('off')

axes[0].imshow(wordcloud2010, interpolation='bilinear')
axes[0].set_title("2010")
axes[0].axis('off')
plt.tight_layout()
plt.show()