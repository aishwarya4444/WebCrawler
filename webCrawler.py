#!/usr/bin/python3

# python --version 3.4.2

import argparse
import random
import urllib.request
import urllib.parse
import bs4

def breadthFirstSearch(url, numUrls):
    if numUrls < 0:
        print('Number of URLs should be positive.')
        exit(2)
    # repository of URL
    urls = []
    urls.append(url)
    while numUrls and len(urls):
        # choose a URL randomly from repository
        randomIndex = random.randint(0, len(urls)-1)
        # remove the randomly chosen URL from repository
        url = urls.pop(randomIndex)
        try:
            # get the web page for the URL chosen
            html_page = urllib.request.urlopen(url).read()
            # parse the web page
            soup = bs4.BeautifulSoup(html_page,'html.parser')
            # loop over all the anchor tags in the web page
            for link in soup.find_all('a'):
                # chop the URL
                _link = link.get('href')
                # if the URL is relative, prefix it with it's parent URL
                _url = urllib.parse.urljoin(url, _link)
                # add the URL to the repository
                urls.append(_url)
            print(url)
        except:
            # an error occured while fetching the URL
            print("Cannot access ",url)
        numUrls = numUrls - 1
    # empty the url repository
    urls.clear()

def main():
    # get the arguments
    parser = argparse.ArgumentParser(description="Web Crawler")
    parser.add_argument('url', help='URL to be crawled.')
    parser.add_argument('numUrls', help='Number of URLs that have to be crawled.', type=int)
    args = parser.parse_args()
    # start with BFS of input URL
    breadthFirstSearch(args.url, args.numUrls)

if __name__ == "__main__":
    main()
