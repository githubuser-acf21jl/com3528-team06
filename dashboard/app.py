# Plotly Dash modules
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

# MiRo dashboard modules
from views.modals import dashboard_modals
from views.rows import dashboard_rows
from views.tooltips import dashboard_tooltips
from controllers.intervals import dashboard_intervals

# See other included themes: https://bootswatch.com
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = 'MiRo Dashboard'
app.layout = html.Div([
	dashboard_rows['Row_top'],
	dashboard_rows['Row_1'],
	dashboard_rows['Row_2'],
	dashboard_rows['Row_3'],
	dashboard_rows['Row_4'],
	dashboard_rows['Row_5'],
	dashboard_rows['Row_6'],
	dashboard_rows['Row_7'],
	dashboard_rows['Row_btm'],
	dashboard_modals,
	dashboard_tooltips,
	dashboard_intervals,
	dcc.Store(
		id='motivation_memory',
		data={
			'social': [],
			'ball'  : [],
		}
	),
])
