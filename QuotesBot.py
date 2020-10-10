import requests
import tweepy
from bs4 import BeautifulSoup

auth = tweepy.OAuthHandler("MVAc7n92wgvBksTCXouaKGOWM", "mu3t199AzlRZlc1biirPwk97KUHWVWSzX6E2Fi9iyOEtqUgG4X")
auth.set_access_token("1314924036347092994-exGzT1EWq60xPKALHhfgtGnhrFqBhW", "4yzV0vT7ADh456pBKfqEcF6wTXbLu1muRaBYw2gQ4sB8o")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Auth OK")
except:
    print("Failed to Authentify")

quote_page = requests.get("http://www.quotationspage.com/random.php")
soup = BeautifulSoup(quote_page.content, 'html.parser')

random_quote = soup.find_all(class_="quote")[0].get_text()
random_quote_author = soup.find_all(class_="author")[0].find("b").get_text()

random_quote_final = random_quote + "\n" + random_quote_author

api.update_status(random_quote_final)
