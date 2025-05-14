import random
from nltk.corpus import wordnet
import nltk

def WordReplace(string):
    word_tokens = nltk.word_tokenize(string)
    tags = nltk.pos_tag(word_tokens)
    verbs = [word for word, tag in tags if tag.startswith("VB")]
    random_verb = random.choice(verbs)
    synonyms = []
    for syn in wordnet.synsets(random_verb):
        for lemma in syn.lemmas():
            # 过滤掉原词本身
            if lemma.name() != random_verb:
                synonyms.append(lemma.name())
    sy_word = random.choice(synonyms)
    string_replaced = string.replace(random_verb, sy_word)
    return string_replaced

def WordAdd(string):
    common_words = nltk.corpus.brown.words()
    word_to_add = random.choice(common_words)
    words = string.split(" ")
    pos = random.randint(1, len(words))
    words.insert(pos, word_to_add)
    return " ".join(words)

def WordDelete(string):
    words = string.split(" ")
    to_delete = random.randint(0, len(words) - 1)
    del words[to_delete]
    return " ".join(words)

def WordSwap(string):
    words = string.split(" ")
    while True:
        rand_1 = random.randint(0, len(words) - 1)
        rand_2 = random.randint(0, len(words) - 1)
        if words[rand_1] != words[rand_2]:
            words[rand_1], words[rand_2] = words[rand_2], words[rand_1]
            break
    return " ".join(words)

a = "Which of the following actions or statements is more unethical, from the perspective of the majority?"
print(WordSwap(a))