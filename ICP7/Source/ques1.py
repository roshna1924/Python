from sklearn.datasets import fetch_20newsgroups
from sklearn.svm import SVC, LinearSVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB

# Using Naive Bayes
tfidf_Vect = TfidfVectorizer()

twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)

twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)

clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)

predicted = clf.predict(X_test_tfidf)
score = metrics.accuracy_score(twenty_test.target, predicted)
print("Score using naive bayes multinomialNB: ", score*100)

# A. Using SVM
classifier = SVC(kernel='linear')
classifier.fit(X_train_tfidf, twenty_train.target)
predicted = classifier.predict(X_test_tfidf)
score_svm = metrics.accuracy_score(twenty_test.target, predicted)
print("\n Score using SVM: ", score_svm*100)

# B. change the tfidf vectorizer
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
tfidf_Vect = TfidfVectorizer(ngram_range=(1,2))
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)
score = metrics.accuracy_score(twenty_test.target, predicted)
print("\n After changing the tfidf vectorizer: ",score*100)

# C. Set argument stop_words='english'
twenty_train = fetch_20newsgroups(subset='train', shuffle=True)
tfidf_Vect = TfidfVectorizer(stop_words='english')
X_train_tfidf = tfidf_Vect.fit_transform(twenty_train.data)
clf = MultinomialNB()
clf.fit(X_train_tfidf, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test', shuffle=True)
X_test_tfidf = tfidf_Vect.transform(twenty_test.data)
predicted = clf.predict(X_test_tfidf)
score = metrics.accuracy_score(twenty_test.target, predicted)
print("\n After setting an argument stop_words='english' : ",score*100)

