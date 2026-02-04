import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the CSV file
df = pd.read_csv("final_output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Initialize the Dash app
app = Dash(__name__)

# Layout of the app
app.layout = html.Div([
    # Header
    html.H1(
        "Pink Morsel Sales Visualiser",
        style={"textAlign": "center", "color": "#2c3e50", "margin-bottom": "30px"}
    ),
    
    # Region selector
    html.Div([
        html.Label("Select Region:", style={"fontWeight": "bold", "margin-right": "10px"}),
        dcc.RadioItems(
            id="region-radio",
            options=[
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
