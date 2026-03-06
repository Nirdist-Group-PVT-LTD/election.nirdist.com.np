import json
import requests
import time
from datetime import datetime

# Real-world IDs for 2026 districts
DISTRICTS = [
    {"id": 1, "name": "Taplejung"}, {"id": 12, "name": "Jhapa"}, 
    {"id": 27, "name": "Kathmandu"}, {"id": 35, "name": "Chitwan"},
    # Add all 77 IDs here for a full crawl
]

def scrape_election_data():
    master_data = {
        "metadata": {"last_update": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
        "national": {"fptp_declared": 42, "total_seats": 165},
        "places": {}
    }

    for dist in DISTRICTS:
        print(f"Syncing {dist['name']}...")
        # Simulate API call to the election portal backend
        # In production: requests.get(f"https://api.election2026.com/district/{dist['id']}")
        
        master_data["places"][dist["name"]] = {
            "color": "#00aeef" if dist["name"] == "Kathmandu" else "#dd0000", # Example Logic
            "constituencies": [
                {
                    "name": f"{dist['name']}-1",
                    "leader": "Candidate Name",
                    "party": "RSP",
                    "votes": 12450,
                    "margin": 3200,
                    "status": "Counting"
                }
            ]
        }
        time.sleep(0.5) # Prevent IP blocking

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(master_data, f, indent=4)

if __name__ == "__main__":
    scrape_election_data()
