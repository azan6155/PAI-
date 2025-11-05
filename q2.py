PUNCTUATION = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
STOPWORDS = {'i','me','my','a','an','the','is','am','was','and','but','if','or','to','of','at','by','for','with','this','that'}
POSITIVE = {'love','amazing','great','helpful','resolved'}
NEGATIVE = {'disaster','broken','worst','avoid','bad'}

posts = [
    {'id': 1, 'text': 'I LOVE the new #GuIPhone! Battery life is amazing.'},
    {'id': 2, 'text': 'My #GuIPhone is a total disaster. The screen is already broken!'},
    {'id': 3, 'text': 'Worst customer service ever from @GuIPhoneSupport. Avoid this.'},
    {'id': 4, 'text': 'The @GuIPhoneSupport team was helpful and resolved my issue. Great service!'}
]

def clean_text(text, punctuation, stopwords):
    text = text.lower()
    for c in punctuation:
        text = text.replace(c, '')
    words = text.split()
    return [w for w in words if w not in stopwords]

def evaluate_posts(data, punctuation, stopwords, pos_words, neg_words):
    def calc_score(tokens):
        s = 0
        for t in tokens:
            if t in pos_words:
                s += 1
            elif t in neg_words:
                s -= 1
        return s
    result = []
    for post in data:
        words = clean_text(post['text'], punctuation, stopwords)
        result.append({
            'id': post['id'],
            'text': post['text'],
            'tokens': words,
            'score': calc_score(words)
        })
    return result

def filter_negative(posts):
    return [p for p in posts if p['score'] < 0]

def extract_topics(posts):
    tags, mentions = {}, {}
    for p in posts:
        for w in p['text'].split():
            if w.startswith('#'):
                tags[w] = tags.get(w, 0) + 1
            elif w.startswith('@'):
                mentions[w] = mentions.get(w, 0) + 1
    return {'hashtags': tags, 'mentions': mentions}

results = evaluate_posts(posts, PUNCTUATION, STOPWORDS, POSITIVE, NEGATIVE)
negatives = filter_negative(results)
topics = extract_topics(negatives)

print("Analyzed Posts:")
for r in results:
    print(r)

print("\nNegative Posts:")
for n in negatives:
    print(n)

print("\nTrending Negative Topics:")
print(topics)
