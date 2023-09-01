import pandas as pd 
import re
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import word_tokenize
import nltk

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
data_frame['title'] = data_frame['title'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', re.sub(r'[.,-]', '', x)))
data_frame['abstract'] = data_frame['abstract'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', '', re.sub(r'[.,]', '', x)))

#remove stop words 
stop_words = set(stopwords.words('english'))
data_frame['title'] = data_frame['title'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
data_frame['abstract'] = data_frame['abstract'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))

#use stemming 
#stemmer = LancasterStemmer()
#data_frame['title'] = data_frame['title'].apply(lambda x: [stemmer.stem(word) for word in x])
#data_frame['abstract'] = data_frame['abstract'].apply(lambda x: [stemmer.stem(word) for word in x])

#sort the tables 
data_frame['year'] = data_frame['year'].astype(int)
final_sorted_data = data_frame.sort_values(by='year')
print(final_sorted_data)

'''
2. **Natural Language Processing**: Once the data is in a suitable state, employ relevant NLP
methodologies to generate keywords from the abstracts. Discuss the chosen approach and its
effectiveness.

For this section, I used TF-IDF and 
'''

