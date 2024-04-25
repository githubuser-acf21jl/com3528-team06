# Plotly Dash modules
from dash import dcc
import dash_bootstrap_components as dbc

card = dbc.Card(
	[
		dbc.CardHeader(
			[
				'Action selection',
				dbc.Button(
					'＋',
					id='action-modal-open',
					color='light',
					size='sm',
					style={'float': 'right'}
				),
			],
			className='bg-warning font-weight-bold lead'
		),
		dbc.CardBody(
			dcc.Graph(
				id='action-graph',
				config={'displayModeBar': False},
				style={
					'height': '150px',
					'width' : '100%',
				}
			)
		)
	],
	color='warning',
	inverse=True,
	outline=True,
)

modal_tab = dbc.Tab(
	dcc.Graph(
		id='action-graph-large',
		config={'displayModeBar': False},
		style={
			'height': '300px',
			'width' : '100%',
		}
	),
	label='Live data'
)
