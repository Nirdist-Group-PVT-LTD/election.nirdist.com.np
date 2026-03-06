import requests
from bs4 import BeautifulSoup
import json
import datetime
import os
def save_data(data):
    # This ensures the file is created in the current directory
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

# Even if scraping fails, create an empty structure
default_data = {"last_updated": "Pending", "results": []}
save_data(default_data)
def scrape_election_data():
    # Example URL (Replace with your actual target source)
    url = "https://example-nepal-news-portal.com/election-live"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Find elements containing party names and vote counts
        # YOU MUST CHANGE THESE SELECTORS BASED ON THE TARGET WEBSITE
        parties = soup.find_all('div', class_='party-name')
        votes = soup.find_all('div', class_='vote-count')
        
        results = []
        for party, vote in zip(parties, votes):
            results.append({
                "party": party.text.strip(),
                "votes": int(vote.text.strip().replace(',', ''))
            })
            
        return {
            "last_updated": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "results": results
        }
        
    except Exception as e:
        print(f"Error scraping data: {e}")
        return None

if __name__ == "__main__":
    data = scrape_election_data()
    if data:
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data successfully updated.")
