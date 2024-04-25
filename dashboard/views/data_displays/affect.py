# Plotly Dash modules
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

card = dbc.Card(
	[
		dbc.CardHeader(
			[
				'Affect',
				dbc.Button(
					'＋',
					id='affect-modal-open',
					color='light',
					size='sm',
					style={'float': 'right'}
				)
			],
			className='bg-info font-weight-bold lead'
		),
		dbc.CardBody(
			dcc.Graph(
				id='affect-graph',
				# 'Animate' property is incompatible with changing background images
				# animate=True,
				config={'displayModeBar': False},
				style={
					# FIXME: Ideally this shouldn't be a hardcoded value
					'height': '300px',
					'width' : '100%',
				}
			)
		)
	],
	color='info',
	className='mx-1',
	inverse=True,
	outline=True,
	style={'height': '100%'}
)

modal_tab = dbc.Tab(
	dbc.Table(
		html.Tr(
			[
				html.Td(
					dcc.Graph(
						id='affect-graph-large',
						# 'Animate' property is incompatible with changing background images
						# animate=True,
						config={'displayModeBar': False},
						style={
							'height': '500px',
							'width' : '500px',
						}
					)
				),
				html.Td(
					dcc.Graph(
						id='sleep-graph-large',
						# 'Animate' property is incompatible with changing images
						# animate=True,
						config={'displayModeBar': False},
						style={
							'height': '500px',
							'width' : '500px',
						}
					)
				)
			]
		),
		borderless=True
	),
	label='Live data'
)
