# DESIGN
This project has two main components, which are the Webscraping component, for finding the information necessary to construct the message, and the Email management portion, for sending the email once the data has been found.
## Webscraping
Over development, I went through several webscraping solutions before landing on BeautifulSoup
- The first attempt was with an API called [ParseHub](https://www.parsehub.com/), while it makes it really easy to grab data and would be a great solution for the issue with national statistics grabbing on to news articles, unfortunately it being more of an enterprise or data-science solution, it was very hard to make it viable for deployment in an application like this one.
- The Second attempt came with [Selenium](https://www.selenium.dev/), Selenium posed some challenges as it wasn't meant designed for webscraping as it's primary purpose, problems arose in both by local and cloud IDE in using the chromedriver, after many troubleshooting attempts, this web scraping solution was ultimately scrapped in favor of BeautifulSoup
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) being a purpose built web scraping solution as well as being very friendly to complete web scraping novices like myself made me very confident in choosing this solution for the current design of the webscraping portion.
### National Statistics

- Ideally, the national statistics would have been found from the large table found in [worldometer](https://www.worldometers.info/coronavirus/#countries), as it is held to a high standard, but the lack of any class of distinguishing classes for any sort of categories made it very difficult to implement a webscraping solution for someone at my skill level. As a compromise, what the program does to fetch national statistics is search google, and then find the information found in the google widgets, as this is the only sort of information made easily accessible to the program, upon a google search that would work for most countries. Unfortunately, google does not distinguish between widget types so for some countries the widget can have news items instead of coronavirus statistics, which is a current bug in the program. that I haven't been able to find a meaningful fix for. I've tried many other sites but it seems like there isn't one that can provide a meaningful improvement in reliability in comparison to the current compromise.
### Global Statistics
- While [worldometer](https://www.worldometers.info/coronavirus/)'s table doesn't have any HTML classes, it does seem like they have classes for the main counters found at the top of their website, this makes it quite easy for Beautifulsoup to find these counters and parse them appropriately, which is the current solution in place to extract the Global statistics found in the second paragraph of the email.
## Email Sending

- Initially, python's own smtp and email libraries seemed like the logical choices to go, unfortunately this solution was ridden with tons of errors that couldn't be solved in either the cloud IDE or my localised IDE. This led to me scrapping this idea after 10 hours of troubleshooting.

- The second solution that I tried was the Gmail API, which also had its fair share of problems. It seems like the documentation and samples provided by Google are outdated or very poorly made for beginners, this led to a disappointing failure in trying to implement this email solution.

- The final solution that I ended at is another gmail API called [SendGrid API](https://sendgrid.com/). This API ultimately provided a great solution that also didn't come with the restrictions for a premium account that a solution like ParseHub did for webscraping. This is the final solution employed in my program and has a throwaway account preconfigured for this program, although I plan on implementing a web application in the future for ease of use.

## Country and Username Handling

- To maximise ease of use, There is a separate file which is read upon each call of scraper.py to find both the Country needed and the recipient's email, this makes life a lot easier for the end user.