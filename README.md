#   Text Preprocessing using NLP
This project performs basic text preprocessing on raw ext data. This includes converting text to lowercase, removing punctuation, tokenizing the text into words, removing stopwords to retain only meaningful information.

## Approach
1. The program first asks the user whether they want to input their own text or use a predefined sample text.
2. Based on user input:
   1. If "yes", the user enters custom text
   2. If "no" or invalid input, a sample paragraph is used
3. The text is converted to lowercase to maintain uniformity
4. Punctuation is removed using Python's string module along wih sr.maketrans() and translate() functions
5. The cleaned text is tokenized into individual words using NLTK's word_tokenize() function
6. Stopwords are removed using the predefined list of stopwords provided by NLTK.
7. Finally, both cleaned text and tokenized output are displayed.

## Difficulties Faced
1. NLTK functions initially gave errors due to missing datasets like punkt and stopwords.
2. There was confusion between cleaned text and tokenized output.
3. Understanding how str.maketrans() and translate() work together required additional effort.
4. Handling user input conditions (yes/no) properly.

## Resolution
1. Installed required datasets using: nltk.download('punkt') & nltk.download('stopwords')
2. Clearly separated cleaned text and tokenized output in the program.
3. Learned how translation tables work for punctuation removal.
4. Added proper conditional checks for user input.

## Results
Sample Input:
Natural Language Processing (NLP) is a fascinating field of Artificial Intelligence that focuses on the interaction between computers and humans through language. In recent years, NLP has gained significant attention due to the rapid growth of digital data. However, raw text data is often unstructured, noisy, and difficult to analyze. Therefore, text preprocessing becomes an essential step in any NLP pipeline. Overall, preprocessing helps improve the performance of machine learning models by reducing complexity and focusing only on meaningful information. Without proper preprocessing, even the most advanced NLP models may produce inaccurate or inefficient results.

Cleaned Text:
natural language processing nlp is a fascinating field of artificial intelligence that focuses on the interaction between computers and humans through language in recent years nlp has gained significant attention due to the rapid growth of digital data however raw text data is often unstructured noisy and difficult to analyze therefore text preprocessing becomes an essential step in any nlp pipeline overall preprocessing helps improve the performance of machine learning models by reducing complexity and focusing only on meaningful information without proper preprocessing even the most advanced nlp models may produce inaccurate or inefficient results

Tokenized Output:
['natural', 'language', 'processing', 'nlp', 'fascinating', 'field', 'artificial', 'intelligence', 'focuses', 'interaction', 'computers', 'humans', 'language', 'recent', 'years', 'nlp', 'gained', 'significant', 'attention', 'due', 'rapid', 'growth', 'digital', 'data', 'however', 'raw', 'text', 'data', 'often', 'unstructured', 'noisy', 'difficult', 'analyze', 'therefore', 'text', 'preprocessing', 'becomes', 'essential', 'step', 'nlp', 'pipeline', 'overall', 'preprocessing', 'helps', 'improve', 'performance', 'machine', 'learning', 'models', 'reducing', 'complexity', 'focusing', 'meaningful', 'information', 'without', 'proper', 'preprocessing', 'even', 'advanced', 'nlp', 'models', 'may', 'produce', 'inaccurate', 'inefficient', 'results']

## Learnings
1. Learned how to clean and preprocess raw text data.
2. Understood the importance of normalization in NLP.
3. Gained hands-on experience with the NLTK library.
4. Learned the difference between raw text, cleaned text, and tokenized output.
5. Understood the use of maketrans() and translate() in Python

## How to set up and run
1. Install dependencies:
   pip install nltk
2. Download required datasets:
   1. import nltk
   2. nltk.download('punkt')
   3. nltk.download('stopwords')
3. Run the script:
   python "text preprocessing.py"
4. Enter 'yes' to input your own text
   OR
   Enter 'no' to use sample text
