# Plotly Dash modules
from dash import dcc
import dash_bootstrap_components as dbc

card = dbc.Card(
	[
		dbc.CardHeader(
			[
				'Motivation',
				dbc.Button(
					'＋',
					id='motivation-modal-open',
					color='light',
					size='sm',
					style={'float': 'right'}
				),
			],
			className='bg-danger font-weight-bold lead'
		),
		dbc.CardBody(
			dcc.Graph(
				id='motivation-graph',
				config={'displayModeBar': False},
				style={
					'height': '120px',
					'width' : '100%'
				}
			)
		),
		dbc.CardFooter(
			'➡ Internal drives',
			style={
				'color'    : 'black',
				'font-size': 'x-small'
			}
		)
	],
	color='danger',
	inverse=True,
	outline=True,
	# REMOVE THIS TO ENABLE MOTIVATION GRAPH
	style={'display': 'none'}
)

modal_tab = dbc.Tab(
	dcc.Graph(
		id='motivation-graph-large',
		# 'Animate' property is incompatible with changing images
		# animate=True,
		config={'displayModeBar': False},
		style={
			'height': '500px',
			'width' : '100%',
		}
	),
	label='Live data'
)
