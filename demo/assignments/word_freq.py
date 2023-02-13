st = "how do you do today and how did you do yesterday"

words = st.split(' ')
for w in sorted(set(words)):
    print(w, words.count(w))

