import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

def createPieFig(_labels, _counts, _colors, _title):
    fig = go.Figure(data=[go.Pie(labels=_labels, values=_counts)])
    fig.update_layout(title_text=_title)
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=_colors, line=dict(color='black', width=3)))
    return fig

def createBarFig(_x, _y, _names, _colors, _traceNumber):
    fig = go.Figure()
    for i in range(_traceNumber):
        fig.add_trace(go.Bar(
        x=df[_x],
        y=df[_y[i]],
        name=_names[i],
        marker_color=_colors[i]))
    fig.update_layout(barmode='group', xaxis_tickangle=-45)
    return fig

df = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/dailyActivity_merged.csv")

df["ActivityDate"] = pd.to_datetime(df["ActivityDate"], format= "%m/%d/%Y")

df["TotalMinutes"] = df["VeryActiveMinutes"]+df["FairlyActiveMinutes"]+df["LightlyActiveMinutes"]+df["SedentaryMinutes"]

#print(df.describe())

fig_steps_calories = px.scatter(data_frame=df, x="Calories", y="TotalSteps",
                                size="VeryActiveMinutes", trendline="ols", title="Relationship Between Total Steps & Calories")

# Pie figure about rate of activity types
labels = ["Very Active Minutes", "Fairly Active Minutes", "Lightly Active Minutes", "Inactive Minutes"]
counts = df[["VeryActiveMinutes", "FairlyActiveMinutes", "LightlyActiveMinutes", "SedentaryMinutes"]].mean()
colors = ['gold','lightgreen', "pink", "blue"]

fig_minutes_rate = createPieFig(labels, counts, colors, "Active Minutes Rates")
fig_minutes_rate.show()

# Bar figure about activity types for days of week
df["Day"] = df["ActivityDate"].dt.day_name()

y= ["VeryActiveMinutes", "FairlyActiveMinutes", "LightlyActiveMinutes"]
names= ["Very Active", "Fairly Active", "Lightly Active"]
colors = ["pink", "blue", "green"]

fig_activeminutes_day = createBarFig("Day", y, names, colors, 3)
fig_activeminutes_day.show()

# Pie figure about inactive minutes for days of week
day= df["Day"].value_counts()
labels = day.index
counts = df["SedentaryMinutes"]
colors = ["cyan", "green", "gold", "blue", "pink", "orange", "purple"]

fig_inactiveminutes_daily = createPieFig(labels, counts, colors, "Inactive Minutes Daily Rates")
fig_inactiveminutes_daily.show()

#Pie figure about calories burned for days of week
day= df["Day"].value_counts()
labels = day.index
counts = df["Calories"]
colors = ["cyan", "green", "gold", "blue", "pink", "orange", "purple"]

fig_caloriesburned_daily = createPieFig(labels, counts, colors, "Burned Calories Daily Rates")
fig_caloriesburned_daily.show()