# Plotly Dash modules
from dash import dcc
import dash_bootstrap_components as dbc

card = dbc.Card(
	[
		dbc.CardHeader(
			[
				'Circadian rhythm',
				dbc.Button(
					'＋',
					id='circadian-modal-open',
					color='light',
					size='sm',
					style={'float': 'right'}
				)
			],
			className='bg-primary font-weight-bold lead'
		),
		dbc.CardBody(
			dcc.Graph(
				id='circadian-graph',
				animate=True,
				config={'displayModeBar': False},
				style={
					'height': '115px',
					'width' : '100%',
				}
			)
		)
	],
	color='primary',
	className='mx-1',
	inverse=True,
	outline=True,
)
