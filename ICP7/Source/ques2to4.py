from bs4 import BeautifulSoup
import urllib.request
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk import ne_chunk
from collections import Counter

# Q2 & Q.3 Extract given web URL text using BeautifulSoup and save in file
def webScraping(url):
    f = open("input.txt", 'w+', encoding='utf-8')
    source_code = urllib.request.urlopen(url)
    plain_text = source_code

    soup = BeautifulSoup(plain_text, "html.parser")
    f.write(soup.body.text.encode('utf-8',"rb").decode('utf-8'))


webScraping("https://en.wikipedia.org/wiki/Google")

# Q.4 Applying some functions

lemmatizer = WordNetLemmatizer()
text = open('input.txt', encoding="utf8").read()

# 4.a) Tokenization
w_tokens =word_tokenize(text)
s_tokens = sent_tokenize(text)
print("Word tokens:",w_tokens)
print("\nSentence tokens:",s_tokens)
#
# 4. b) POS
n_pos = nltk.pos_tag(w_tokens)
print("\nParts of Speech :", n_pos)
#
# 4. c) Stemming
ps = PorterStemmer()
ln = LancasterStemmer()
sb = SnowballStemmer("english")
ps_output = ' '.join([ps.stem(w) for w in w_tokens])
ln_output = ' '.join([ln.stem(w) for w in w_tokens])
sb_output = ' '.join([sb.stem(w) for w in w_tokens])
print("\nPorterStemmer Stemming:\n",ps_output)
print("\nLancasterStemmer Stemming:\n",ln_output)
print("\nSnowballStemmer Stemming:\n",sb_output)
#
# 4. d) Lemmatization
lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in w_tokens])
print("\nLemmatization:\n",lemmatized_output)
#
# 4. e) Trigram
trigrams = ngrams(w_tokens,3)
print("\nTrigrams: ",list(trigrams))
#
# 4. f) Named Entity Recognition
noe = ne_chunk(n_pos)
print("\nNamed Entity Recognition :", noe)