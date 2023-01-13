# BLOG SCRAPER v1

This project is a Python script that uses the requests and BeautifulSoup libraries to scrape the titles and links of recently posted articles from a set of websites (in this case, freeCodeCamp and Hacker News) and saves them to a reading list if they match certain keywords.

## REQUIREMENTS

- Python 3.x

- [requests](https://pypi.org/project/requests/)

- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

## CUSTOMIZATION


### Websites
A dictionary containing the websites you want to scrape and their URLs.

### Keywords
A list of keywords that the script will match against the article titles.

### Scraping Logic
The script uses the requests library to retrieve the HTML of the websites specified in the website list and the BeautifulSoup library to     parse the HTML and extract the titles and links of the articles.

### Matching Logic
The script checks if the titles of the articles match any of the keywords specified in the keyword list and saves the matched articles to a reading list.

## OUTPUT

The script output the matched articles with their title and links in the following format: title, link.
