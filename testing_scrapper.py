import re
import requests
from bs4 import BeautifulSoup


def scrape_emails(url):
    response = requests.get(url)
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    urls = set()
    emails = []

    if response.ok:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find and extract emails from the current page
        emails += re.findall(email_regex, response.text)

        # Find all URLs on the current page
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('http'):  # Filter out non-http links
                urls.add(href)

    # Scrape emails from each URL found on the current page
    for url in urls:
        response = requests.get(url)
        if response.ok:
            emails += re.findall(email_regex, response.text)

    return emails


# Main function
if __name__ == "__main__":
    target_url = 'https://www.buzzinteractive.co/'  # Replace with the actual URL of the webpage
    scraped_emails = scrape_emails(target_url)

    # Print the scraped email addresses
    print(scraped_emails)
