# ScrapyTutorial
use python scrapy to scrape data from https://quotes.toscrape.com/

## The Project Structure:
We generate a Scrapy Project after installing scrapy using: pip install scrapy
Then we pass the command: scrapy startproject quotetutorial
This command automatically creates the scrapy project structure that we need to work with
namely.

### Spiders
### Items
### Pipelines
### Middlewares
### Settings


## 0) Spiders:
The crawlers used here are: QuoteSpider. We generate is using: scrapy genspider quote_spider.
In the quote_spider we define 
### the name of this spider: 
that we are going to refer to from the command line with name = 'quotes'
### the starting urls: 
that we are going to start scraping the data from. In this case starting_urls = [http://quotes.toscrape.com/login] 
after loggin in to the website we want to parse the data so in the parse method of the crawler we define the loggin in credentials that we are using to enter the website.
### following the links
then the way we are going to extract the information from each page in the start_scraping method and the links to follow in case there is still a next_page. 
### selecting the data
The scraped data is selected using css 
### the dataflow
then passed to an QuoteItem that we are going to see in details later. This QuoteItem is then passed 
to the middleware -> then to the pipeline from the crwaler using the yield command.
## 1) Middleware:
Not modified in this project but could be used
## 2) Items:
We define a QuotetutorialItem that defines the shape of the data that we are going to scrape and store. For example our Quote has to fields title, author and tags. So we define those fields in the QuoteItem class.
## 3) Pipelines:
In the pipelines section we define what we are going to do with our data. For Example we are going to store our data in a sqlite database so we import the necessary library, create the database connection, create the tables and commit the changes. This happens everytime we command our spider to crawls the website.
### data output
the data output is then a sqlite db file named myquotes.db
## 4) Settings:
In the settings section we define general settings like:
### robots.txt rules
### how we want to name our bot
### number of requests per second
### cookies settings
### network and proxies settings
### and more
Those rules can be modified and set to bypass the restrictions/or not set by the website for the crawlers
## 5) Improvements
### server side rendering
the website in this example is not server side rendered so it is easy to scrape. However some websites are server side rendered and do only return some javascript that is then parsed by the browser or rely on javascript to be enabled on the browser in order to render some functionalities, which is not the case in our example. So in that situation we need to firstly use a navigator that parses this javascript to html elements for us. We can use splash navigator with python for example and then proceed to do our work with scrapy.



