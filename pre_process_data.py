# Imoprting Libraries

import nltk
import re
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
# nltk.download('stopwords')
stop_words = stopwords.words('english')
from bertopic import BERTopic
from sentence_transformers import SentenceTransformer



# Object of lemmetizer
lemmatizer = WordNetLemmatizer()

# Object of sentence transformer
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Loading our trained model
model = BERTopic.load("./static/final_model", embedding_model=embedding_model)



topic_list = ["Debt, Loan & Mortage",
              "Credit Report, Company & Identity Theft",
              "Account & Fraud,Scam",
              "Account Credit Card Transaction"]

# Data Cleaning
def re_clean(data):
    ex = re.sub("[^A-za-z\s]+" ,'',data)
    ex = re.sub("X",'',ex)
    ex = re.sub('\s+',' ',ex)
    ex = re.sub('\n','',ex)
    return ex.strip().lower()



def lemmatize(data):
    return ' '.join([lemmatizer.lemmatize(word) for word in word_tokenize(data) 
                        if word not in stop_words and len(word)> 2])



# Prediction function
def pred(data):
    topic, _ = model.transform(data)
    return topic_list[topic[0]]



def main_fun(data):
    data = re_clean(data)
    data = lemmatize(data)
    return pred(data)










