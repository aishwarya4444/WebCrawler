PROBLEM STATEMENT
-----------------
<p>Write a web crawler.<\p>
<p>A crawler is a program that starts with a url on the web (ex: http://python.org), fetches the web-page corresponding to that url, and parses all the links on that page into a repository of links. Next, it fetches the contents of any of the url from the repository just created, parses the links from this new content into the repository and continues this process for all links in the repository until stopped or after a given number of links are fetched.</p>

RUNNING THE SCRIPT
------------------
<p>progName URL numberOfUrlsToBeCrawled</p>1111
<p>./webCrawler.py http://python.org/pypi 4</p>

ERRORS
------
<p>Unable to crawl for "http://stackoverflow.com" and "http://python.org"</p>
