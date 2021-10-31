import urllib.request
import string

url = 'https://www.gutenberg.org/files/84/84-0.txt'
response = urllib.request.urlopen(url)
data = response.read()  # a `bytes` object
Frankenstein = data.decode('utf-8')

# print(Frankenstein) # for testing

# print(type(Frankenstein))
# print(Frankenstein.split())

def clean_words(file, skip_header):
    if skip_header:
        skip_gutenberg_header(file)
    for word in file:
        if word.startswith("*** END OF THE PROJECT"):
            break
    lst = []
    for word in file.split():
        w = word.strip(string.whitespace + string.punctuation)
        w = w.lower()
        lst.append(w)   
    return lst

def skip_gutenberg_header(file):
    """Reads from file until it finds the line that ends the header.
    file: open file object
    """
    for line in file:
        if line.startswith("*** START OF THE PROJECT"):
            break

def count_words(text):
    wordfreq = {}
    cleaned_words = clean_words(text, skip_header=True)
    for words in cleaned_words:
        if words not in wordfreq:
            wordfreq[words] = 1
        else:
            wordfreq[words] += 1
    return wordfreq

def total_words(text):
    """Returns the total of the frequencies of words in a histogram."""
    return sum(text.values())

def different_words(text):
    """Returns the number of different words in a histogram."""
    return len(text.keys())

def unique_per_word(a,b):
    return a/b

def most_common(text, excluding_stopwords=False):
    lst = []
    for words, frequency in text.items():
        lst.append((frequency, words))
    lst.sort()
    lst.reverse()
    return lst


def main():
    print(clean_words(Frankenstein, skip_header=True))
    hist = count_words(Frankenstein)
    print(hist)
    print('Total number of words:', total_words(hist))
    print('Number of different words:', different_words(hist))
    A = total_words(hist)
    B = different_words(hist)
    print(f"The ratio of unique word and total word for the writer is: {unique_per_word(B,A)}.")
    t = most_common(hist, excluding_stopwords=True)
    print('The most common words in Frankenstein are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)
    pass
if __name__ == "__main__":
    main()
