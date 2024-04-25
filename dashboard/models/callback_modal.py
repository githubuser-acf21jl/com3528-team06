# Plotly Dash modules
from dash.dependencies import Input, Output, State

# MiRo dashboard modules
from app import app


@app.callback(
	Output('action-modal', 'is_open'),
	[Input('action-modal-open', 'n_clicks'), Input('action-modal-close', 'n_clicks')],
	[State('action-modal', 'is_open')]
)
def modal_action(n1, n2, is_open):
	if n1 or n2:
		return not is_open
	return is_open


@app.callback(
	Output('affect-modal', 'is_open'),
	[Input('affect-modal-open', 'n_clicks'), Input('affect-modal-close', 'n_clicks')],
	[State('affect-modal', 'is_open')]
)
def modal_affect(n1, n2, is_open):
	if n1 or n2:
		return not is_open
	return is_open


@app.callback(
	Output('circadian-modal', 'is_open'),
	[Input('circadian-modal-open', 'n_clicks'), Input('circadian-modal-close', 'n_clicks')],
	[State('circadian-modal', 'is_open')]
)
def modal_circadian(n1, n2, is_open):
	if n1 or n2:
		return not is_open
	return is_open


@app.callback(
	Output('motivation-modal', 'is_open'),
	[Input('motivation-modal-open', 'n_clicks'), Input('motivation-modal-close', 'n_clicks')],
	[State('motivation-modal', 'is_open')]
)
def modal_spatial(n1, n2, is_open):
	if n1 or n2:
		return not is_open
	return is_open


@app.callback(
	Output('spatial-modal', 'is_open'),
	[Input('spatial-modal-open', 'n_clicks'), Input('spatial-modal-close', 'n_clicks')],
	[State('spatial-modal', 'is_open')]
)
def modal_spatial(n1, n2, is_open):
	if n1 or n2:
		return not is_open
	return is_open
