import plotly.graph_objects as go
import plotly.io as pio

# Create a simple scatter plot
fig = go.Figure(
    data=[go.Scatter(x=[1, 2, 3, 4], y=[10, 15, 13, 17])],
    layout_title_text="A Simple Plotly Chart"
)

# Convert the figure to HTML and save it
html_string = pio.to_html(fig, full_html=False)
with open('plotly_chart.html', 'w', encoding='utf-8') as f:
    f.write(html_string)