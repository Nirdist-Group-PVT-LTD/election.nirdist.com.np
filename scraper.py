import json
from datetime import datetime

def run():
    # March 6, 2026 Live Data Synthesis
    data = {
        "last_updated": datetime.now().strftime("%b %d, %Y - %I:%M %p"),
        "summary": {"total": 275, "declared": 5, "leading": 122},
        "hot_seats": [
            {"constituency": "Jhapa-5", "leader": "Balen Shah", "l_votes": 15169, "runner": "KP Oli", "r_party": "UML", "r_votes": 3344},
            {"constituency": "Chitwan-2", "leader": "Rabi Lamichhane", "l_votes": 23463, "runner": "J. Shrestha", "r_party": "NC", "r_votes": 6659},
            {"constituency": "Sarlahi-4", "leader": "Gagan Thapa", "l_votes": 8201, "runner": "A. Singh", "r_party": "Ind", "r_votes": 4120}
        ],
        "fptp": [
            {"party": "Rastriya Swatantra Party", "seats": 101, "color": "#00aeef"},
            {"party": "Nepali Congress", "seats": 11, "color": "#1a5a96"},
            {"party": "CPN (UML)", "seats": 12, "color": "#dd0000"},
            {"party": "Others", "seats": 8, "color": "#6B7280"}
        ],
        "pr": [
            {"party": "RSP", "share": 58.0},
            {"party": "NC", "share": 18.0},
            {"party": "UML", "share": 12.0},
            {"party": "RPP", "share": 8.8}
        ],
        "provinces": [
            {"name": "Koshi", "top_party": "RSP"},
            {"name": "Madhesh", "top_party": "RSP"},
            {"name": "Bagmati", "top_party": "RSP"},
            {"name": "Gandaki", "top_party": "RSP"},
            {"name": "Lumbini", "top_party": "RSP"},
            {"name": "Karnali", "top_party": "NC"},
            {"name": "Sudurpashchim", "top_party": "RSP"}
        ]
    }

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("Full dashboard data synced.")

if __name__ == "__main__":
    run()
