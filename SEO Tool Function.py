import os
import nltk
import syllapy

def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()  
    return set(words)

def read_words_from_folder(folder_path):
    all_words = set()
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        words = read_words_from_file(file_path)
        all_words.update(words)
    return all_words
positive_words = read_words_from_file('positive-words.txt')
negative_words = read_words_from_file('negative-words.txt')

stop_words_folder = r'C:\Users\sahil\Desktop\Project Blackcoffer\StopWords'  
stop_words = read_words_from_folder(stop_words_folder)
def analyze_sentiment(text):
    words = nltk.word_tokenize(text.lower())
    
    words = [word for word in words if word not in stop_words]
    
    positive_score = sum(1 for word in words if word in positive_words)
    negative_score = sum(1 for word in words if word in negative_words)
    
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    
    return polarity_score
def calculate_readability(text):
    sentences = nltk.sent_tokenize(text)
    num_sentences = len(sentences)

    words = nltk.word_tokenize(text)
    num_words = len(words)

    average_sentence_length = num_words / num_sentences

    complex_words = [word for word in words if syllapy.count(word)> 2]
    num_complex_words = len(complex_words)
    percentage_complex_words = (num_complex_words / num_words) * 100

    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)

    return fog_index



def calculate_keyword_density(article, keyword):
      # Split the article into sentences
    sentences = article.lower().split('. ')
    art=article
    # Initialize keyword count
    keyword_count = 0
    
    # Count the occurrences of the keyword in each sentence
    for sentence in sentences:
        keyword_count += sentence.count(keyword.lower())
    # Calculate the total number of sentences
    total_sentences = len(art.split())
    
    # Calculate the keyword density
    keyword_density = (keyword_count / total_sentences) * 100
    
    return keyword_density

# Get user input for the article
article = input("Enter the article text: ")

# Get user input for the keyword
keyword = input("Enter the keyword or long-tail keyword: ")

density = calculate_keyword_density(article, keyword)
print(f"The keyword density for '{keyword}' is {density:.2f}%.")
print(f'The readability score of article is {calculate_readability(article)}')
print(f'The sentimental score of article is {analyze_sentiment(article)}')
print('It is Between -1 to +1 where - stands for negative sentiment + for positive sentiment ')



