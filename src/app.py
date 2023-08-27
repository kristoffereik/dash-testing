from dash import Dash, dcc, html, Input, Output
import plotly.express as px

df = px.data.gapminder()

app = Dash(__name__)
server = app.server

app.layout = html.Div(
    [
        html.H4("Country's key performance analytics"),
        html.P("Select data on y-axis:"),
        dcc.Dropdown(
            id="y-axis",
            options=["lifeExp", "pop", "gdpPercap"],
            value="gdpPercap",
        ),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(
    Output("graph", "figure"),
    Input("y-axis", "value"),
)
def display_area(y):
    countries = df.country.drop_duplicates().sample(n=10, random_state=42)
    dff = df[df.country.isin(countries)]
    fig = px.area(dff, x="year", y=y, color="continent", line_group="country")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)