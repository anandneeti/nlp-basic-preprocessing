import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Sample text
sample_text='''Natural Language Processing (NLP) is a fascinating field of Artificial Intelligence that focuses on the interaction between computers and humans through language. In recent years, NLP has gained significant attention due to the rapid growth of digital data. However, raw text data is often unstructured, noisy, and difficult to analyze. Therefore, text preprocessing becomes an essential step in any NLP pipeline. Overall, preprocessing helps improve the performance of machine learning models by reducing complexity and focusing only on meaningful information. Without proper preprocessing, even the most advanced NLP models may produce inaccurate or inefficient results.'''
ans=input("Do you want to enter your text or use sample text? (Enter 'yes' to input your own text, or 'no' to use sample text): ")
if ans.lower() == 'yes':
    text=input("Enter text:")
elif ans.lower()=='no':
    text=sample_text
    print("Using sample text:\n")
    print(text+"\n\n")
else:
    print("Invalid input.\nUsing sample text:\n")
    text=sample_text
    print(text+"\n\n")

# converting text to lowercase
text=text.lower()

# removing punctuation
trans_text=str.maketrans('','',string.punctuation)
cleaned_text=text.translate(trans_text)

# tokenizing text into words
tokens=word_tokenize(cleaned_text)

# removing stopwords
stop_words=set(stopwords.words('english'))
filtered_tokens=[word for word in tokens if word not in stop_words]

# output:
print("Cleaned Text:")
print(cleaned_text)

print("\n\nTokenized Output:")
print(filtered_tokens)
