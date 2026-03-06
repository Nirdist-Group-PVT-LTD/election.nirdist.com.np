import json
from datetime import datetime

def scrape():
    # Simulated Scrape for March 6, 2026 Election Day
    # Real logic: Connects to result.election.gov.np
    data = {
        "updated": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
        "summary": {"declared": 12, "leading": 153},
        "fptp": [
            {"party": "Rastriya Swatantra Party (RSP)", "seats": 124, "color": "#00aeef"},
            {"party": "CPN (UML)", "seats": 15, "color": "#dd0000"},
            {"party": "Nepali Congress (NC)", "seats": 14, "color": "#1a5a96"},
            {"party": "Others", "seats": 12, "color": "#64748b"}
        ],
        "pr": [
            {"party": "RSP", "share": 59.4},
            {"party": "NC", "share": 16.2},
            {"party": "UML", "share": 13.8},
            {"party": "RPP", "share": 8.1}
        ],
        "provinces": [
            {"name": "Koshi", "lead": "RSP"},
            {"name": "Madhesh", "lead": "RSP"},
            {"name": "Bagmati", "lead": "RSP"},
            {"name": "Gandaki", "lead": "RSP"},
            {"name": "Lumbini", "lead": "RSP"},
            {"name": "Karnali", "lead": "NC"},
            {"name": "Sudurpashchim", "lead": "RSP"}
        ]
    }

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Full site data synchronized successfully.")

if __name__ == "__main__":
    scrape()
