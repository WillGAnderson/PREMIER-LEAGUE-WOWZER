import streamlit as st
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Static season data (manually defined)
seasons = {
    2020: ("2020-09-12", "2021-05-23"),
    2021: ("2021-08-13", "2022-05-22"),
    2022: ("2022-08-05", "2023-05-28"),
    2023: ("2023-08-11", "2024-05-19"),
    2024: ("2024-08-09", "2025-05-25"),
    2025: ("2025-08-08", "2026-05-24"),  # estimated
}

# Tottenham-specific stats per season
tottenham_stats = {
    "2020-2021": {"Position": 7, "Points": 62, "Top Scorer": "Harry Kane", "Manager": "José Mourinho / Ryan Mason"},
    "2021-2022": {"Position": 4, "Points": 71, "Top Scorer": "Son Heung-min", "Manager": "Antonio Conte"},
    "2022-2023": {"Position": 8, "Points": 60, "Top Scorer": "Harry Kane", "Manager": "Antonio Conte / Stellini / Mason"},
    "2023-2024": {"Position": 5, "Points": 66, "Top Scorer": "Son Heung-min", "Manager": "Ange Postecoglou"},
    "2024-2025": {"Position": "TBD", "Points": "TBD", "Top Scorer": "TBD", "Manager": "Ange Postecoglou"},
    "2025-2026": {"Position": "TBD", "Points": "TBD", "Top Scorer": "TBD", "Manager": "TBD"},
}

# Process season data
seasons_data = []
for year, (start_str, end_str) in seasons.items():
    start_date = datetime.strptime(start_str, "%Y-%m-%d")
    end_date = datetime.strptime(end_str, "%Y-%m-%d")
    duration = (end_date - start_date).days
    seasons_data.append({
        "Season": f"{year}-{year+1}",
        "Start Date": start_date,
        "End Date": end_date,
        "Days": duration
    })

# Convert to DataFrame
df = pd.DataFrame(seasons_data)

# Streamlit UI
st.set_page_config(page_title="Premier League Explorer", layout="centered")
st.title("\U0001F3C6 The Mighty Spurs")
st.subheader("A dedicated resource to show CJ and Janis that Will Anderson is now a technical wizard")

# Display season data
df_display = df.copy()
st.subheader("Season Data Table")
st.dataframe(df_display)

# Plot chart
st.subheader("\U0001F4CA Season Lengths (Days)")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df_display["Season"], df_display["Days"], color="skyblue")
ax.set_ylabel("Days")
ax.set_xlabel("Season")
ax.set_title("Premier League Season Lengths")
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
st.pyplot(fig)

# Tottenham Interactive Section
st.subheader("\U0001F3C0 Tottenham Hotspur Season Breakdown")
season_options = list(tottenham_stats.keys())
selected_season = st.selectbox("Select a Season to View Tottenham's Stats", season_options)

stats = tottenham_stats[selected_season]
st.markdown(f"### Tottenham {selected_season} Season Stats")
st.table(pd.DataFrame(stats.items(), columns=["Metric", "Value"]))

# Optional: Embed a video or link (example only)
if selected_season == "2021-2022":
    st.markdown("**Highlight:** [Watch Tottenham 3-0 Arsenal (May 2022)](https://www.youtube.com/watch?v=0f_1fVg2eLw)")
elif selected_season == "2022-2023":
    st.markdown("**Highlight:** [Watch Harry Kane's Final Season Goals](https://www.youtube.com/watch?v=IvlU8kJ0X6g)")
