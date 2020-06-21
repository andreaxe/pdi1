from models.MyModel import TotalLoad, Session, ProductionType
from collections import defaultdict
from sqlalchemy.inspection import inspect
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html


def scatter_graph_forecast_error(country_name):

    df_forecast = df[df['country'] == country_name]
    observed = go.Scatter(x=df_forecast['datetime'], y=df_forecast['observed'], mode='lines', name='Observado')
    forecast = go.Scatter(x=df_forecast['datetime'], y=df_forecast['forecast'], mode='lines', name='Previsão')

    data = [observed, forecast]

    fig = go.Figure(data=data)
    fig.update_layout(title_text='Análise de Previsão')

    return fig


def scatter_graph_covid(country_name):

    df_covid = df[df['country'] == country_name]
    df_covid.set_index('datetime', inplace=True)
    country_2019 = df_covid.loc['2019-02-01':'2019-06-10']
    country_2020 = df_covid.loc['2020-02-01':'2020-06-10']

    trace2019 = go.Scatter(y=country_2019['observed'], mode='lines', name='Fev-Junho 2019')
    trace2020 = go.Scatter(y=country_2020['observed'], mode='lines', name='Fev-Junho 2020')

    data = [trace2019, trace2020]

    fig = go.Figure(data=data)
    fig.update_layout(title_text='Período de comparação: Fev-Junho de 2019 vs Fev-Junho de 2020')

    return fig


def donut(country_name):

    df_filtered = df_type_prod[df_type_prod['country'] == country_name]
    all_columns = df_type_prod.columns.to_list()
    labels = [e for e in all_columns if e not in ('country', 'year', 'total_grand_capacity')]

    # years = df_type_prod['year'].unique().tolist()
    years = [2015, 2017, 2019, 2020]

    fig = make_subplots(rows=1, cols=4, specs=[[{"type": "pie"}, {"type": "pie"}, {"type": "pie"}, {"type": "pie"}]])

    for i, year in enumerate(years):

        df_filtered_year = df_filtered[df_filtered['year'] == year]
        values = []

        for label in list(labels):
            try:
                value = int(df_filtered_year[label].values)
                if value == 0:
                    labels.remove(label)
                else:
                    values.append(value)
            except ValueError:
                labels.remove(label)

        fig.add_trace(go.Pie(labels=labels, values=values, name="{} - {}".format(country_name, year), hole=0.2),
                      row=1, col=i+1)

    fig.update_layout(title_text='Capacidade de Produção Instalada - Anos {}'.format(', '.join(map(str, years))))

    return fig


def query_to_dict(rset):
    result = defaultdict(list)
    for obj in rset:
        instance = inspect(obj)
        for key, x in instance.attrs.items():
            result[key].append(x.value)
    return result


# external CSS stylesheets
external_stylesheets = [
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css',
        'rel': 'stylesheet',
    }
]

app = dash.Dash(
    __name__,
    external_stylesheets=external_stylesheets
)
session = Session()

rset = session.query(TotalLoad).all()
df_total_load = pd.DataFrame(query_to_dict(rset))

type_production = session.query(ProductionType).all()
df_type_prod = pd.DataFrame(query_to_dict(type_production))
germany = df_type_prod[df_type_prod['country'] == 'Germany']

countries = []

rset = session.query(TotalLoad).all()
df = pd.DataFrame(query_to_dict(rset))

for country in df_type_prod['country'].unique():
    countries.append({'label': country, 'value': country})


app.layout = html.Div([
    html.Div([

        html.Div([
            html.H3('Carga Total'),
            dcc.DatePickerRange(id='date-picker',
                                start_date_placeholder_text='Inserir data inicial',
                                end_date_placeholder_text='Inserir data final',
                                min_date_allowed=df_total_load['datetime'].min(),
                                max_date_allowed=df_total_load['datetime'].max(),
                                start_date=df_total_load['datetime'].min(),
                                end_date=df_total_load['datetime'].max(),
                                style={'padding-left': '70px', 'margin-top': '20px'}
                        ),
            dcc.Graph(id='total-load'),

        ], className="col-6"),

        html.Div([
            html.H3('Análise do consumo elétrico'),
            dcc.Dropdown(
                id='country-dropdown-covid',
                options=countries,
                value=countries[0],
                style={'margin-top': '20px', 'width': '50%'},
                clearable=False
            ),
            dcc.Graph(id='g5', figure=scatter_graph_covid(countries[0]['value']))
        ], className="col-6"),

        html.Div([
            html.H3('Produção instalada'),
            dcc.Dropdown(
                id='country-dropdown',
                options=countries,
                value=countries[0],
                style={'margin-top': '20px', 'width': '50%'},
                clearable=False
            ),
            dcc.Graph(id='g2', figure=donut(countries[0]['value']))
        ], className="col-12"),

        html.Div([
            html.H3('Análise do erro de previsão'),
            dcc.Dropdown(
                id='country-dropdown-forecast',
                options=countries,
                value=countries[0],
                style={'margin-top': '20px', 'width': '50%'},
                clearable=False
            ),
            dcc.Graph(id='g4', figure=scatter_graph_forecast_error(countries[0]['value']))
        ], className="col-12"),

    ], className="row mt-4")
], className='container-fluid')


@app.callback(Output('g4', 'figure'),
              [Input('country-dropdown-forecast', 'value')])
def update_total_production_type(country_name):

    return scatter_graph_forecast_error(country_name)


@app.callback(Output('g2', 'figure'),
              [Input('country-dropdown', 'value')])
def update_total_production_type(country_name):
    print(country_name)
    return donut(country_name)


@app.callback(Output('g5', 'figure'),
              [Input('country-dropdown-covid', 'value')])
def update_total_load_covid(country_name):

    return scatter_graph_covid(country_name)


@app.callback(Output('total-load', 'figure'),
              [Input('date-picker', 'start_date'),
               Input('date-picker', 'end_date')])
def update_total_load(start_date, end_date):

    filtered_df = df_total_load[(df_total_load['datetime'] > start_date) & (df_total_load['datetime'] <= end_date)]
    traces = []

    for country in filtered_df['country'].unique():
        df_by_country = filtered_df[filtered_df['country'] == country]
        traces.append(go.Scatter(
            x=df_by_country['datetime'],
            y=df_by_country['observed'],
            mode='lines',
            opacity=0.7,
            name=country,
        ))

    return {'data': traces,
            'layout': go.Layout(title='Carga total por país - Fev 2019 / Jun 2020',
                                xaxis={'title': 'Time'},
                                yaxis={'title': 'Load Output'})}


if __name__ == "__main__":
    app.run_server()

# Query base de dados: envio de resultado para dic e posterior uso em PANDAS
# https://gist.github.com/garaud/bda10fa55df5723e27da
