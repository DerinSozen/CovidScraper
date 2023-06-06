# Coronavirus tool that scraper the internet for both national and global coronavirus figures
# These numbers are sent to the email specified in config.txt
# Don't forget to populate the config.txt with both your email and country
# Check the Github on how to automate this daily on both Windows and Mac


# import nescessary libraries
from bs4 import BeautifulSoup
import sys
import time
import requests
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

pause_time = 1


# Here's a function that checks if the code we get from our web requests
def code_check(result):
    # 200 implies that the webpae was successfully accessed
    if (result.status_code == 200):
        print("\ncode 200 recieved, webpage successfully accessed\n")
    # anything other than a code of 200 means the program was unsecsessful, so it spirts out an error
    else:
        print("\ncode 200 not recieved, webpage was not successfuly accessed")
        time.sleep(pause_time)
        print(f"\nupon trying to access the webpage, we recieved code {result.status_code}")
        time.sleep(pause_time)
        print("\nconsult the following Wikipedia page:")
        time.sleep(pause_time)
        sys.exit("\nhttps://en.wikipedia.org/wiki/List_of_HTTP_status_codes")


def main():

    print("\nprogram starting.")

    URL = f'https://www.google.com/search?q={country}+coronavirus+cases'
    # requests the URL of the webpage by searching google
    result = requests.get(URL)
    # runs the resusts of the web requests through the code_check function
    code_check(result)
    # assigns the contents of the web requests only to variable src
    src = result.content
    # use BeautifulSoup to parse our web data into soup
    soup = BeautifulSoup(src, "html.parser")
    # search the soup to find the country information from the google search
    total_confirm = soup.find("div", {'class': 'BNeawe vvjwJb AP7Wnd'})
    # isolate the text of the country stats
    country_stats = total_confirm.text
    # indicate success in
    print("national statistics successfully found")

    # clear variables for use again
    src, soup, result, URL = None, None, None, None

    # get the html content of worldometer
    Worldometer_URL = 'https://www.worldometers.info/coronavirus/'
    result = requests.get(Worldometer_URL)

    # check if the website was successfully accessed
    code_check(result)

    # parse content of worldometer website
    src = result.content
    soup = BeautifulSoup(src, "html.parser")

    # maincounter-number = total cases, total deaths, total recoveries
    # find counters from html content
    counters = soup.find_all("div", {'class': 'maincounter-number'})

    # isolate text content
    global_cases = counters[0].text
    global_deaths = counters[1].text
    global_rec = counters[2].text
    # remove whitespace
    global_cases = global_cases.strip()
    global_deaths = global_deaths.strip()
    global_rec = global_rec.strip()
# compose message for email
    print("Global Statistics Sucessfully found\n")
    message = f"""
Your country's coronavirus statistics for today are:
{country_stats}

Today's global coronavirus statistics are:
{global_cases} total cases,
a total of {global_deaths} lives lost,
and {global_rec} recoveries


information via google and worlometer"""
    return message
# send email via SendGrid API


def send_mail(message_content, email):
    print("Starting to send")
    message = Mail(from_email='pythoncoronavirustracker@gmail.com',
                   to_emails=email,
                   subject='Your Coronavirus Numbers for Today',
                   plain_text_content=message_content)
    try:
        sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        print("sent successfully")
    except Exception as e:
        print(e)


# read for user inputs inside of config.txt file
with open('config.txt', 'r') as f:
    file = f.readlines()
    country = file[0].strip()
    email = file[1].strip()

# check for proper use of the config file
if country == 'INSERT_COUNTRY_HERE' or country == '':
    sys.exit("\nInvalid use, please insert country of choice in the first line of config.txt\n")

if email == 'INSERT_EMAIL_HERE' or email == '':
    sys.exit("\nInvalid use, please insert your email in the second line of config.txt\n")

# execute the functions
message_content = main()

send_mail(message_content, email)
