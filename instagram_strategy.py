

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.templates.default = "plotly_white"

# Load the dataset
instagram_data = pd.read_csv("Instagram-data.csv")

# Engagement metrics to analyze
engagement_metrics = ['Impressions', 'Likes', 'Shares', 'Saves', 'Comments', 'Follows', 'Conversion Rate']

# Calculate average values for each metric
average_metrics = instagram_data[engagement_metrics].mean().reset_index()
average_metrics.columns = ['Metric', 'Average Value']


metric_emojis = {
    'Impressions': '👁️ Impressions',
    'Likes': '❤️ Likes',
    'Shares': '🔁 Shares',
    'Saves': '💾 Saves',
    'Comments': '💬 Comments',
    'Follows': '➕ Follows',
    'Conversion Rate': '📈 Conversion Rate'
}


# Plot
fig = px.bar(
    average_metrics,
    x='Metric',
    y='Average Value',
    text='Average Value',
    title='📊 Average Instagram Engagement Metrics',
    color='Metric',
    color_discrete_sequence=px.colors.qualitative.Set2,  # Soft aesthetic colors
    height=500,
    width=900
)

# Update text appearance
fig.update_traces(textposition='outside', textfont_size=12)

# Update layout aesthetics
fig.update_layout(
    title_font_size=22,
    font=dict(family="Arial", size=14),
    plot_bgcolor='#f9f9f9',
    paper_bgcolor='#f9f9f9',
    xaxis_title='',
    yaxis_title='Average Value',
    yaxis=dict(showgrid=True, gridcolor='lightgrey', zeroline=False),
    margin=dict(l=40, r=40, t=80, b=40)
)

fig.show()

import pandas as pd
import plotly.express as px
import plotly.io as pio

# Set Plotly theme
pio.templates.default = "plotly_white"

# ✅ STEP 1: Load the CSV (REPLACE filename with your real one)
df = pd.read_csv("Instagram-data.csv")  # Use exact file name

# ✅ STEP 2: Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# ✅ STEP 3: Create 'Day' and 'Hour' columns
df['Day'] = df['Date'].dt.day_name()
df['Hour'] = df['Date'].dt.hour

# ✅ STEP 4: Reorder days
df['Day'] = pd.Categorical(df['Day'], categories=[
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
], ordered=True)

# ✅ STEP 5: Bar Chart – Avg Impressions per Day
day_avg = df.groupby('Day')['Impressions'].mean().reset_index()

fig_day = px.bar(
    day_avg,
    x='Day',
    y='Impressions',
    color='Impressions',
    color_continuous_scale='turbo',  # More vibrant shades
    title='📅 Average Impressions by Day',
    labels={'Impressions': 'Avg Impressions'},
)

fig_day.update_layout(
    font=dict(family="Arial", size=16),
    title_font=dict(size=22),
    plot_bgcolor='#E7C7C7',
    paper_bgcolor="#E7C7C7",
)

# ✅ STEP 6: Scatter Plot – Impressions vs Hour
fig_hour = px.scatter(
    df,
    x='Hour',
    y='Impressions',
    color='Impressions',
    size='Impressions',
    color_continuous_scale='viridis',
    title='🕒 Impressions by Hour of the Day',
    labels={'Impressions': 'Impressions'},
    opacity=0.75
)

fig_hour.update_layout(
    font=dict(family="Arial", size=16),
    title_font=dict(size=22),
    plot_bgcolor='honeydew',
    paper_bgcolor='honeydew',
)


fig_day.add_annotation(
    text="🔥 Highest Avg Impressions",
    x=day_avg.loc[day_avg['Impressions'].idxmax(), 'Day'],
    y=day_avg['Impressions'].max(),
    showarrow=True,
    arrowhead=2,
    ax=0,
    ay=-50,
    font=dict(color="crimson", size=14)
)

# ✅ STEP 7: Show graphs
fig_day.show()


fig_hour.add_annotation(
    text="✨ Peak Hour",
    x=df.loc[df['Impressions'].idxmax(), 'Hour'],
    y=df['Impressions'].max(),
    showarrow=True,
    arrowhead=2,
    ax=40,
    ay=-40,
    font=dict(color="darkgreen", size=14)
)

fig_hour.show()


def categorize_post(text):
    text = str(text).lower()
    if any(word in text for word in ['tip', 'how to', 'guide', 'learn']):
        return 'Educational 🎓'
    elif any(word in text for word in ['sale', 'launch', 'offer', 'discount']):
        return 'Promotional 🛍️'
    elif any(word in text for word in ['inspire', 'motivation', 'mindset', 'believe']):
        return 'Inspirational 💡'
    elif any(word in text for word in ['shoutout', 'team', 'community', 'event']):
        return 'Community 🎉'
    elif any(word in text for word in ['aesthetic', 'vibe', 'look']):
        return 'Aesthetic 📸'
    elif any(word in text for word in ['lol', 'funny', 'meme', 'relatable']):
        return 'Entertaining 😄'
    else:
        return 'Other'

df['Intent'] = df['Caption'].apply(categorize_post)  # Replace 'Caption' with your column
intent_avg = df.groupby('Intent')[['Likes', 'Comments', 'Saves']].mean().reset_index()
import plotly.express as px

fig = px.bar(
    intent_avg.melt(id_vars='Intent', var_name='Interaction Type', value_name='Average'),
    x='Intent',
    y='Average',
    color='Interaction Type',
    barmode='group',
    title='📢 Engagement by Post Intent Category',
    color_discrete_sequence=['#6CA6CD', '#A2D2FF', '#B0E0E6', '#C3B1E1', '#D0F0C0']

)

fig.update_layout(
    font=dict(family="Poppins, sans-serif", size=14),
    title_font=dict(size=24, family="Poppins"),
    xaxis_title='Post Intent',
    yaxis_title='Average Interactions',
    plot_bgcolor='lightcyan',
    paper_bgcolor='lightcyan',
    xaxis=dict(showgrid=False),
    yaxis=dict(gridcolor='lightgrey', zeroline=False),

)
fig.update_traces(
    hovertemplate='<b>%{x}</b><br>Interaction: %{customdata[0]} 💬<br>Avg: %{y:.0f}',
    customdata=df[['Intent']]
)

fig.add_annotation(
    text="🎯 Educational posts drive consistent engagement!",
    x='Educational 🎓',
    y=intent_avg[intent_avg['Intent']=='Educational 🎓']['Likes'].values[0],
    showarrow=True,
    arrowhead=2,
    ax=0,
    ay=-60,
    bgcolor="lightcyan",
    font=dict(color="black", size=12)
)


fig.show()

import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv("Instagram-data.csv")

# Classify post intents
def classify_intent_detailed(caption):
    caption = str(caption).lower()
    if any(word in caption for word in ['project', 'portfolio', 'build', 'clone', 'app', 'website', 'design']):
        return 'Projects'
    elif any(word in caption for word in ['tips', 'how to', 'ways to', 'guide', 'tricks']):
        return 'Tips & Guides'
    elif any(word in caption for word in ['tool', 'library', 'framework']):
        return 'Tools & Tech'
    elif any(word in caption for word in ['motivation', 'inspiration', 'quote']):
        return 'Motivational'
    elif any(word in caption for word in ['career', 'job', 'resume']):
        return 'Career Advice'
    elif any(word in caption for word in ['course', 'learn', 'training']):
        return 'Educational'
    else:
        return 'Others'

# Apply classification
df['Intent'] = df['Caption'].apply(classify_intent_detailed)

# Group and sort
intent_followers = df.groupby('Intent')['Follows'].sum().reset_index()
intent_followers = intent_followers.sort_values(by='Follows', ascending=False)

# Use a new palette
colors = px.colors.qualitative.Safe

# Donut chart
fig = px.pie(
    intent_followers,
    names='Intent',
    values='Follows',
    title='🚀 New Followers by Post Intent',
    hole=0.2,
    color_discrete_sequence=colors
)

fig.update_traces(
    textinfo='label+percent',
    textposition='inside',
    hovertemplate='%{label}: %{value} followers',
    marker=dict(line=dict(color='white', width=1.5))
)

fig.update_layout(
    title_font_size=22,
    font=dict(size=14),
    showlegend=True,
    paper_bgcolor='cornsilk'
)

fig.show()



import pandas as pd
import plotly.express as px

# Load and preprocess data
df = pd.read_csv("Instagram-data.csv")
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])  # Drop rows with invalid dates

# Extract date parts
df['Month'] = df['Date'].dt.month_name()
df['DayOfWeek'] = df['Date'].dt.day_name()

# Average engagement per month
monthly_engagement = df.groupby('Month')[['Likes', 'Comments', 'Shares', 'Saves', 'Follows']].mean().reset_index()


# Sort months chronologically
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
monthly_engagement['Month'] = pd.Categorical(monthly_engagement['Month'], categories=month_order, ordered=True)
monthly_engagement = monthly_engagement.sort_values('Month')

# Plot engagement trends by month
fig = px.line(monthly_engagement, x='Month', y=['Likes', 'Comments', 'Shares', 'Saves', 'Follows'],
              title='📆 Monthly Average Engagement Metrics',
              markers=True)

fig.update_layout(yaxis_title='Average per Post', legend_title='Metric', paper_bgcolor = 'beige')
fig.update_traces(mode='lines+markers')
fig.show()

# ----------------------------

# Weekly pattern
weekly_engagement = df.groupby('DayOfWeek')[['Likes', 'Comments', 'Shares', 'Saves', 'Follows']].mean().reset_index()

# Sort weekdays
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekly_engagement['DayOfWeek'] = pd.Categorical(weekly_engagement['DayOfWeek'], categories=weekday_order, ordered=True)
weekly_engagement = weekly_engagement.sort_values('DayOfWeek')

# Plot engagement trends by weekday
fig2 = px.line(weekly_engagement, x='DayOfWeek',
               y=['Likes', 'Comments', 'Shares', 'Saves', 'Follows'],
               title='📈 Weekly Engagement Trends',
               markers=True)


fig2.update_layout(yaxis_title='Average Reach', xaxis_title='Day of Week',paper_bgcolor = 'lavender')
fig2.update_traces(mode='lines+markers')
fig2.show()

import pandas as pd

# Load original data and your updated post type/hour file
main_df = pd.read_csv("Instagram-data.csv")
type_hour_df = pd.read_csv("Instagram_PostType_Hour_Template.csv")

# Convert 'Date' columns to datetime for accurate merge
main_df['Date'] = pd.to_datetime(main_df['Date'])
type_hour_df['Date'] = pd.to_datetime(type_hour_df['Date'])

# Merge on 'Date'
merged_df = pd.merge(main_df, type_hour_df, on='Date', how='left')

# Save merged file
merged_df.to_csv("Instagram_merged.csv", index=False)



# Add day of week
merged_df['Day'] = df['Date'].dt.day_name()

# Engagement column
merged_df['Total_Engagement'] = df[['Likes', 'Comments', 'Shares', 'Saves']].sum(axis=1)

print(df.columns)

# 1. Which post type drives most followers for each day
followers_by_day_type = merged_df.groupby(['Day', 'Post_Type'])['Follows'].mean().unstack().fillna(0)
followers_by_day_type.to_csv("Followers_by_Day_and_Type.csv")

# 2. Post type that engages best
engagement_by_type = merged_df.groupby('Post_Type')['Total_Engagement'].mean().sort_values(ascending=False)
engagement_by_type.to_csv("Engagement_by_Type.csv")

# 3. Best posting hour for Impressions and Reach
hourly = merged_df.groupby('Post_Hour')[['Impressions']].mean().sort_values(by='Impressions', ascending=False)
hourly.to_csv("Best_Posting_Hours.csv")


print("\n📈 1. Followers Gained by Post Type and Day of Week:\n")
print(followers_by_day_type)

print("\n🔥 2. Engagement Metrics by Post Type:\n")
print(engagement_by_type)

print("\n⏰ 3. Best Hours to Post (Avg Impressions & Reach):\n")
print(hourly.head(10))  # Top 10 best hours

#plotting Total engangement per post type
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8, 6))
sns.histplot(data=merged_df, x='Total_Engagement', hue='Post_Type', multiple='stack', palette='muted', bins=30)
plt.title("Distribution of Total Engagement by Post Type")
plt.xlabel("Total Engagement")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Histogram_Engagement_by_Type.png")
plt.show()

# followers_by_day_type is already a pivot table
plt.figure(figsize=(10, 6))
sns.heatmap(followers_by_day_type, annot=True, fmt=".1f", cmap="coolwarm", linewidths=0.5)
plt.title("Followers Gained by Post Type and Day")
plt.xlabel("Post Type")
plt.ylabel("Day")
plt.tight_layout()
plt.savefig("Followers_Heatmap.png")
plt.show()

plt.figure(figsize=(8, 6))
sns.lineplot(data=hourly.reset_index(), x='Post_Hour', y='Impressions', marker='o')
plt.title("Impressions by Posting Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Average Impressions")
plt.xticks(rotation=45, ha='right')  # 🔧 This line fixes your issue
plt.tight_layout()
plt.show()



