import streamlit as st
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Spurs-themed CSS styling (adjusted for actual visibility)
st.markdown("""
    <style>
        body, .stApp {
            background-color: #0A1A2F;
            color: white;
        }
        h1, h2, h3, h4 {
            color: #f0f0f0;
        }
        .stDataFrame { background-color: #1c2d5a; }
    </style>
""", unsafe_allow_html=True)

# Static season data
seasons = {
    2020: ("2020-09-12", "2021-05-23"),
    2021: ("2021-08-13", "2022-05-22"),
    2022: ("2022-08-05", "2023-05-28"),
    2023: ("2023-08-11", "2024-05-19"),
    2024: ("2024-08-09", "2025-05-25"),
    2025: ("2025-08-08", "2026-05-24"),
}

# Spurs match data
spurs_matches = {
    "2021-2022": [
        {"Opponent": "Arsenal", "Date": "2022-05-12", "Venue": "Tottenham Hotspur Stadium", "Badge": "https://upload.wikimedia.org/wikipedia/en/5/53/Arsenal_FC.svg"},
        {"Opponent": "Leicester", "Date": "2022-05-01", "Venue": "Tottenham Hotspur Stadium", "Badge": "https://upload.wikimedia.org/wikipedia/en/6/63/Leicester02.png"},
    ],
    "2022-2023": [
        {"Opponent": "Chelsea", "Date": "2023-02-26", "Venue": "Tottenham Hotspur Stadium", "Badge": "https://upload.wikimedia.org/wikipedia/en/c/cc/Chelsea_FC.svg"},
        {"Opponent": "Manchester City", "Date": "2023-02-05", "Venue": "Tottenham Hotspur Stadium", "Badge": "https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg"},
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

# Fetch weather from Visual Crossing
def fetch_weather(date, location="London"):
    try:
        api_key = "JJB8ZDJF6765HV63WZXRAZQH5"
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{date}?key={api_key}&unitGroup=metric"
        response = requests.get(url)
        data = response.json()
        st.write(data)  # Debug print
        return f"{data['days'][0]['temp']}°C, {data['days'][0]['conditions']}"
    except Exception as e:
        st.error(f"Weather fetch failed: {e}")
        return "Weather data unavailable"

# Create season data table
df = pd.DataFrame([{
    "Season": f"{year}-{year+1}",
    "Start Date": datetime.strptime(start, "%Y-%m-%d"),
    "End Date": datetime.strptime(end, "%Y-%m-%d"),
    "Days": (datetime.strptime(end, "%Y-%m-%d") - datetime.strptime(start, "%Y-%m-%d")).days
} for year, (start, end) in seasons.items()])

# Streamlit UI
st.set_page_config(page_title="Premier League Explorer", layout="centered")
st.title("🏆 The Mighty Spurs")
st.subheader("A dedicated resource to show CJ and Janis that Will Anderson is now a technical wizard")

st.subheader("Season Data Table")
st.dataframe(df)

st.subheader("📊 Season Lengths (Days)")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df["Season"], df["Days"], color="#132257")
ax.set_ylabel("Days")
ax.set_xlabel("Season")
ax.set_title("Premier League Season Lengths")
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
st.pyplot(fig)

# Spurs breakdown
st.subheader("🏟️ Tottenham Hotspur Season Breakdown")
selected_season = st.selectbox("Select a Season to View Tottenham's Stats", list(tottenham_stats.keys()))
st.markdown(f"### Tottenham {selected_season} Season Stats")
st.table(pd.DataFrame(tottenham_stats[selected_season].items(), columns=["Metric", "Value"]))

# Match info
if selected_season in spurs_matches:
    st.markdown("### Selected Matchday Data")
    for match in spurs_matches[selected_season]:
        col1, col2 = st.columns([1, 5])
        with col1:
            st.image(match["Badge"], width=50)
        with col2:
            weather = fetch_weather(match["Date"])
            st.markdown(f"**{match['Date']} vs {match['Opponent']}**")
            st.markdown(f"Venue: {match['Venue']}")
            st.markdown(f"Weather: {weather}")
            st.markdown("---")

# Video highlights
highlight_links = {
    "2021-2022": "https://www.youtube.com/watch?v=0f_1fVg2eLw",
    "2022-2023": "https://www.youtube.com/watch?v=IvlU8kJ0X6g"
}
if selected_season in highlight_links:
    st.markdown(f"**Highlight Video:** [Watch here]({highlight_links[selected_season]})")
