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
st.title("\U0001F4C5 Premier League Season Explorer (2020–2025)")

# Display data
st.subheader("Season Data Table")
st.dataframe(df)

# Plot chart
st.subheader("\U0001F4CA Season Lengths (Days)")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df["Season"], df["Days"], color="skyblue")
ax.set_ylabel("Days")
ax.set_xlabel("Season")
ax.set_title("Premier League Season Lengths")
ax.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
st.pyplot(fig)
