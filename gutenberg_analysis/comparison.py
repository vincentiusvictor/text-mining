from Frankenstein_analysis import Frankenstein, clean_words
from Prideandprejudice_analysis import PAP, clean_words

### Grab and clean the book
F_cleaned_lst = clean_words(Frankenstein, skip_header=True)
PAP_cleaned_lst = clean_words(PAP, skip_header=True)
F_cleaned = ' '.join(F_cleaned_lst)
PAP_cleaned = ' '.join(PAP_cleaned_lst)

### Find common word
def create_simplified_trie(words):
    trie = {}
    for word in words:
        curr = trie
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['#'] = True  
    return trie

def smaller_length_list(A,B):
    if len(A) > len(B):
        A, B = B, A

def common_word(A,B):
    lst = []
    for word in B:
        curr = A
        found_prefix = True
        for c in word:
            if c not in curr:
                found_prefix = False
                break
            curr = curr[c]
        if found_prefix and '#' in curr:
            lst.append(word)
    return lst

def count_common_word(common_word_lst):
    wordfreq = {}
    for words in common_word_lst:
        if words not in wordfreq:
            wordfreq[words] = 1
        else:
            wordfreq[words] += 1
    return wordfreq
    

def most_common(text, excluding_stopwords=False):
    lst = []
    for words, frequency in text.items():
        lst.append((frequency, words))
    lst.sort()
    lst.reverse()
    return lst


### Find uncommon word
def uncommonwords(text1, text2):
    count = {}
    for words in text1.split():
        count[words] = count.get(words, 0) + 1
    for words in text2.split():
        count[words] = count.get(words, 0) + 1
    return [word for word in count if count[word] == 1]
   
def uncommon_in_each_text(list_of_uncommon, text_split):
    lst = []
    for words in list_of_uncommon :
        if words in text_split:
            lst.append(words)
    return lst
    


def main():    
    text1 = F_cleaned_lst
    text2 = PAP_cleaned_lst

    # #Finding Common words between 2 texts
    text1_trie = create_simplified_trie(text1)
    smaller_length_list(text1_trie,text2)
    lst_common_words = common_word(text1_trie,text2)
    print(lst_common_words)

    counted_common = count_common_word(lst_common_words)
    print(counted_common)

    t = most_common(counted_common, excluding_stopwords=True)
    print('The most common words in the 2 books are:')
    for freq, word in t[0:20]:
        print(word, '\t', freq)

   
    # Finding uncommon words between 2 texts
    F_PAP_diff = uncommonwords(F_cleaned,PAP_cleaned)
    print(f'The vocabluary {F_PAP_diff} differentiate the two writers ')

    # Finding words each writer lacking from others
    A = uncommon_in_each_text(F_PAP_diff, F_cleaned_lst)
    print(f' The writer of Frankenstein uses {A} vocabluary, while the write of Pride and Prejudice does not') 
    B = uncommon_in_each_text(F_PAP_diff, PAP_cleaned_lst)
    print(f' The writer of Frankenstein uses {B} vocabluary, while the write of Pride and Prejudice does not') 

if __name__ == "__main__":
    main()
