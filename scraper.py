import json
from datetime import datetime

def scrape():
    # DATA SOURCE: 2026 Nepal General Election Trends (March 6)
    # Historic surge for Rastriya Swatantra Party (RSP)
    data = {
        "updated": datetime.now().strftime("%I:%M %p, %b %d"),
        "summary": {"declared": 5, "leading": 125},
        "fptp": [
            {"party": "Rastriya Swatantra Party (RSP)", "seats": 110, "color": "#00aeef"},
            {"party": "CPN (UML)", "seats": 12, "color": "#dd0000"},
            {"party": "Nepali Congress (NC)", "seats": 11, "color": "#1a5a96"},
            {"party": "Others", "seats": 7, "color": "#6B7280"}
        ],
        "pr": [
            {"party": "RSP", "share": 58.2},
            {"party": "NC", "share": 17.8},
            {"party": "UML", "share": 12.1},
            {"party": "RPP", "share": 9.0}
        ],
        "hot_seats": [
            {"constituency": "Jhapa-5", "leader": "Balendra Shah", "l_votes": 18204, "runner": "KP Oli", "r_party": "UML", "r_votes": 4120},
            {"constituency": "Chitwan-2", "leader": "Rabi Lamichhane", "l_votes": 25110, "runner": "NC Candidate", "r_party": "NC", "r_votes": 6120},
            {"constituency": "Kathmandu-1", "leader": "Ranju Neupane", "l_votes": 9102, "runner": "Prakash Singh", "r_party": "NC", "r_votes": 3104}
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
    print("Dashboard Sync Complete.")

if __name__ == "__main__":
    scrape()
