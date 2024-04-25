from dash import dcc
from dash import html

dashboard_intervals = html.Div([
	dcc.Interval(
		id='interval-fast',
		# Too short an interval causes issues as not all plots can be updated before the next callback
		# Every tenth of a second
		interval=0.1 * 1000,
		n_intervals=0
	),
	dcc.Interval(
		id='interval-medium',
		# Every fifth of a second
		interval=0.2 * 1000,
		n_intervals=0
	),
	dcc.Interval(
		id='interval-slow',
		# Every minute
		interval=60 * 1000,
		n_intervals=0
	)
])
