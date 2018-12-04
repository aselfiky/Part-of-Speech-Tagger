import nltk
nltk.download('universal_tagset')
from nltk.corpus import brown
from nltk.tokenize import sent_tokenize
import string


def main():
    corp = brown.sents(categories='news')
    print(corp[0])
    print(corp[1])

    brown_news_tagged = brown.tagged_sents(categories='news', tagset='universal')

    print (len(brown_news_tagged))

    for c in brown_news_tagged:
        print(c)


if __name__ == "__main__":
    main()