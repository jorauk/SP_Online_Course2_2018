#!/usr/bin/env python

"""
Threaded version of the script to see how much a given word is
mentioned in the news today

Uses data from the NewsAPI:

https://newsapi.org
"""

import threading
import requests

NEWS_API_KEY = "5e3dca56fa674afe9b01464c3bd308e8"

WORD = "war"
base_url = 'https://newsapi.org/v1/'


def get_sources():
    """
    Get all the english language sources of news

    'https://newsapi.org/v1/sources?language=en'
    """
    url = base_url + "sources"
    params = {"language": "en", "apiKey": NEWS_API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    sources = [src['id'].strip() for src in data['sources']]
    print("Got the sources:")
    print(sources)
    return sources


def get_articles(source):
    """
    download the info for all the articles
    """
    url = base_url + "articles"
    params = {"source": source,
              "apiKey": NEWS_API_KEY,
              "sortBy": "top"
              }
    print("requesting:", source)
    response = requests.get(url, params=params)
    if response.status_code != 200:  # requests has "status"
        print(f'something went wrong with: {source}')
        print(response)
        print(response.text)
        return []
    data = response.json()
    # the url to the article itself is in data['articles'][i]['url']
    titles = [str(art['title']) + str(art['description'])
              for art in data['articles']]
    return titles


def count_word(word, titles):
    word = word.lower()
    count = 0
    for title in titles:
        if word in title.lower():
            count += 1
    return count


# create the objects to hold the data
sources = []
titles = []

# get the sources -- this is essentially synchronous
loop.run_until_complete(get_sources(sources))

# run the loop for the articles
jobs = asyncio.gather(*(get_articles(source) for source in sources))
loop.run_until_complete(jobs)
loop.close()

art_count = len(titles)
word_count = count_word(WORD, titles)

print(f'found {WORD}, {word_count} times in {art_count} articles')
print(f'Process took {(time.time() - start):.0f} sec.')