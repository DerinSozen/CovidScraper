# Python Coronavirus Notifier

Python Coronavirus Notifier is a python tool that scours the web for coronavirus information and deliers it to your email.

This project utilizes [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for webscraping

This project utilizes the Twilio's [SendGrid API](https://sendgrid.com/) for email handling

## Project status
This project is very work in progress, there are known issues and improvements on the roadmap for better and easier usage

## Setup

1. Download the Github repository
2. Install the necessary libraries (Check below)
3. Populate config.txt

### Installations(Windows)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/).

```bash
pip install beautifulsoup4
```

install [requests](https://pypi.org/project/requests/).

```bash
pip install requests
```

install the [sendgrid python library](https://pypi.org/project/sendgrid/).

```bash
pip install sendgrid
```

### Installations(Macos)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [BeautifulSoup4]
```bash
python -m pip install beautifulsoup4
```
install [requests](https://pypi.org/project/requests/.)

```bash
python -m pip install requests
```

install the [sendgrid python library](https://pypi.org/project/sendgrid/).

```bash
python -m pip install sendgrid
```

### Config.txt

```python
INSERT_COUNTRY_HERE
INSERT_EMAIL_HERE
```

Inside of config.txt, you will find these two items which need to be swapped out. Please make sure that the first row has your country of choice and the second, your email address


## Usage

```bash
python scraper.py
```
although automated usage of script is possible via python this isn't ideal in comparison to first party utilities found in both Macos and Windows, tutorials on how to schedule a python script on both platforms can be found [here](https://martechwithme.com/schedule-python-scripts-windows-mac/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Roadmap

- [ ] Reliability Improvements for national data
- [ ] Web hosting instead of local installation
- [ ] HTML stylized emails

### Known Bug(s)
- This utility sometimes encounters an error when instead of picking up national statistics, it picks up the title for a news article in relation to the country and coronavirus, in a sample of 30, the issue was replicated 7 times, a fix for this issue is in the works

## License
[MIT](https://choosealicense.com/licenses/mit/)