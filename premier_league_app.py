import streamlit as st
st.set_page_config(page_title="Premier League Explorer", layout="centered")

from datetime import datetime
import pandas as pd
import requests

# Spurs-themed CSS styling
st.markdown("""
    <style>
        body, .stApp {
            background-color: #0A1A2F;
            color: white;
        }
        h1, h2, h3, h4 {
            color: #f0f0f0;
        }
    </style>
""", unsafe_allow_html=True)

# Spurs match data with trivia
spurs_matches = {
    "2021-2022": [
        {"Opponent": "Arsenal", "Date": "2022-05-12", "Venue": "Tottenham Hotspur Stadium", "Badge": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg", "Score": "3-0", "Chart": "Harry Styles - As It Was", "Trivia": {"question": "Which Spurs player scored a brace in this match?", "answer": "Harry Kane"}},
        {"Opponent": "Leicester", "Date": "2022-05-01", "Venue": "Tottenham Hotspur Stadium", "Badge": "https://upload.wikimedia.org/wikipedia/en/6/63/Leicester02.png", "Score": "3-1", "Chart": "Dave - Starlight", "Trivia": {"question": "Who assisted Son Heung-min's second goal?", "answer": "Lucas Moura"}},
    ],
    "2022-2023": [
        {"Opponent": "Chelsea", "Date": "2023-02-26", "Venue": "Tottenham Hotspur Stadium", "Badge": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg", "Score": "2-0", "Chart": "Miley Cyrus - Flowers", "Trivia": {"question": "Which defender scored the second goal?", "answer": "Eric Dier"}},
        {"Opponent": "Manchester City", "Date": "2023-02-05", "Venue": "Tottenham Hotspur Stadium", "Badge": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg", "Score": "1-0", "Chart": "Miley Cyrus - Flowers", "Trivia": {"question": "Who scored the winning goal?", "answer": "Harry Kane"}},
    ]
}

# Tottenham summary stats
tottenham_stats = {
    "2020-2021": {"Position": 7, "Points": 62, "Top Scorer": "Harry Kane", "Manager": "José Mourinho / Ryan Mason"},
    "2021-2022": {"Position": 4, "Points": 71, "Top Scorer": "Son Heung-min", "Manager": "Antonio Conte"},
    "2022-2023": {"Position": 8, "Points": 60, "Top Scorer": "Harry Kane", "Manager": "Antonio Conte / Stellini / Mason"},
    "2023-2024": {"Position": 5, "Points": 66, "Top Scorer": "Son Heung-min", "Manager": "Ange Postecoglou"},
    "2024-2025": {"Position": "TBD", "Points": "TBD", "Top Scorer": "TBD", "Manager": "Ange Postecoglou"},
    "2025-2026": {"Position": "TBD", "Points": "TBD", "Top Scorer": "TBD", "Manager": "TBD"},
}

# Function to fetch weather from Visual Crossing
def fetch_weather(date, location="London"):
    try:
        api_key = "JJB8ZDJF6765HV63WZXRAZQH5"
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date}?key={api_key}&unitGroup=metric"
        response = requests.get(url)
        data = response.json()
        return f"{data['days'][0]['temp']}°C, {data['days'][0]['conditions']}"
    except:
        return "Weather data unavailable"

# Music video links
chart_links = {
    "Harry Styles - As It Was": "https://www.youtube.com/watch?v=H5v3kku4y6Q",
    "Dave - Starlight": "https://www.youtube.com/watch?v=2xW2bFqSXts",
    "Miley Cyrus - Flowers": "https://www.youtube.com/watch?v=G7KNmW9a75Y"
}

# UI content
st.title("🏆 The Mighty Spurs")
st.subheader("A dedicated resource to show CJ, Janis and Jake that Will Anderson is now a technical wizard")

# Spurs breakdown
st.subheader("🏀 Tottenham Hotspur Season Breakdown")
selected_season = st.selectbox("Select a Season to View Tottenham's Stats", list(tottenham_stats.keys()))
st.markdown(f"### Tottenham {selected_season} Season Stats")
st.table(pd.DataFrame(tottenham_stats[selected_season].items(), columns=["Metric", "Value"]))

# Match info with weather, score, badge, music chart and trivia
if selected_season in spurs_matches:
    st.markdown("### Selected Matchday Data")
    for i, match in enumerate(spurs_matches[selected_season]):
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image(match["Badge"], width=50)
        with col2:
            weather = fetch_weather(match["Date"])
            st.markdown(f"**{match['Date']} vs {match['Opponent']}**  ")
            st.markdown(f"Venue: {match['Venue']}  ")
            st.markdown(f"Final Score: {match['Score']}")
            st.markdown(f"Weather: {weather}")
            link = chart_links.get(match['Chart'], "")
            if link:
                st.markdown(f"UK #1 Single: *{match['Chart']}* [▶️ Watch]({link})")
            else:
                st.markdown(f"UK #1 Single: *{match['Chart']}*")

            # Trivia section
            st.markdown(f"**Trivia:** {match['Trivia']['question']}")
            user_answer = st.text_input(f"Your answer for {match['Date']} ({i})", key=f"trivia_{i}")
            if user_answer:
                if user_answer.strip().lower() == match['Trivia']['answer'].lower():
                    st.success("Correct! 🎉")
                else:
                    st.error("Try again!")
            st.markdown("---")

# Video highlights
highlight_links = {
    "2021-2022": "https://www.youtube.com/watch?v=0f_1fVg2eLw",
    "2022-2023": "https://www.youtube.com/watch?v=IvlU8kJ0X6g"
}
if selected_season in highlight_links:
    st.markdown(f"**Highlight Video:** [Watch here]({highlight_links[selected_season]})")
