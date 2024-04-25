# Plotly Dash modules
from dash import html
import dash_bootstrap_components as dbc

dashboard_alerts = {
	# 'ball': dbc.Alert(
	# 	"⚽",
	# 	id='ball-alert',
	# 	color='info',
	# 	className='m-0 large text-center',
	# 	is_open=False,
	# ),
	# 'ball_large': dbc.Alert(
	# 	"⚽",
	# 	id='ball-alert-large',
	# 	color='info',
	# 	className='m-0 large text-center',
	# 	is_open=False,
	# ),
	# 'face': dbc.Alert(
	# 	"😀",
	# 	id='face-alert',
	# 	color='success',
	# 	className='m-0 large text-center',
	# 	is_open=False,
	# ),
	# 'face_large': dbc.Alert(
	# 	"😀",
	# 	id='face-alert-large',
	# 	color='success',
	# 	className='m-0 large text-center',
	# 	is_open=False,
	# ),
	'intro'      : dbc.Alert(
		[
			html.H4('MiRo Dashboard', className='alert-heading'),
			html.P('This visual representation of MiRo\'s \"cognitive architecture\" reveals some of the '
			       'data and processes driving the robot\'s behaviour.'),
			html.P('Note component connections, observe what happens to each plot as you interact with '
			       'MiRo, and click any of the \'＋\' buttons for more information.')
		],
		className='mx-5 shadow-lg',
		color='primary',
	),
	'connections': dbc.Alert(
		'Many up– and downstream connections have been omitted for clarity',
		className='mx-5 shadow small',
		color='light',
		style={'float': 'left'}
	),
	'to_higher'  : dbc.Alert(
		'⬆ To higher functions ⬆',
		color='dark',
		className='my-0 py-0 text-center'
	),
	'to_lower'   : dbc.Alert(
		'⬇ To lower functions ⬇',
		color='dark',
		className='my-0 py-0 text-center'
	),
}
