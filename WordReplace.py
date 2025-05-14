import random
from nltk.corpus import wordnet
import nltk

def wordReplace(string):
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

a = "Which of the following actions or statements is more unethical, from the perspective of the majority?"
print(wordReplace(a))
