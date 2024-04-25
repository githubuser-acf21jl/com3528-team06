# Plotly Dash modules
import dash_daq as daq
from dash import html
import dash_bootstrap_components as dbc

# MiRo dashboard modules
import dashboard_constants as con

card = dbc.Card(
	[
		dbc.CardHeader(
			[
				'Spatial attention',
				dbc.Button(
					'＋',
					id='spatial-modal-open',
					color='light',
					size='sm',
					style={'float': 'right'}
				),
			],
			className='bg-success font-weight-bold lead'
		),
		dbc.CardBody(
			[
				html.Div(
					[
						html.H6(
							'Aural',
							className='card-subtitle',
							style={
								'color'     : 'black',
								'text-align': 'center'
							}
						),
						html.Img(
							id='audio-pri-wide',
							style={
								'height': con.PRIW_HEIGHT,
								'width' : '100%',
							}
						),
					],
					style={
						'display'      : 'block',
						'margin-left'  : 'auto',
						'margin-right' : 'auto',
						'margin-bottom': '20px',
						# 'width'        : con.PRIW_WIDTH
						'width'        : '100%',
					}
				),
				html.Div(
					[
						html.H6(
							'Visual',
							className='card-subtitle',
							style={
								'color'     : 'black',
								'text-align': 'center'
							}
						),
						html.Div(
							[
								html.Img(
									id='camera-img-left',
									style={
										# 'height': con.CAM_HEIGHT,
										# 'width' : con.CAM_WIDTH,
										'max-height': con.CAM_HEIGHT,
										'width'     : '50%',
									}
								),
								html.Img(
									id='camera-img-right',
									style={
										# 'height': con.CAM_HEIGHT,
										# 'width' : con.CAM_WIDTH
										'max-height': con.CAM_HEIGHT,
										'width'     : '50%',
									}
								),
								html.Div(
									[
										html.Img(
											id='camera-pri-left',
											style={
												# 'height' : con.CAM_HEIGHT,
												# 'width'  : con.CAM_WIDTH,
												'max-height': con.CAM_HEIGHT,
												'opacity'   : con.PRI_OPACITY,
												'width'     : '50%',

											}
										),
										html.Img(
											id='camera-pri-right',
											style={
												# 'height' : con.CAM_HEIGHT,
												# 'width'  : con.CAM_WIDTH,
												'max-height': con.CAM_HEIGHT,
												'opacity'   : con.PRI_OPACITY,
												'width'     : '50%',
											}
										),
									],
									style={
										'float'   : 'left',
										'position': 'absolute',
										'left'    : '0px',
										'top'     : '0px',
										'z-index' : '2'
									}
								)
							],
							style={
								'display' : 'block',
								'margin'  : 'auto',
								# Necessary for attention image to overlay vision
								'position': 'relative',
								# 'width'   : con.CAM_WIDTH * 2
								'width'   : '100%',
							}
						)
					],
				),
			],
		),

		# dashboard_alerts['ball'],
		# dashboard_alerts['face'],
		# 	]
		# ),
		# TODO: Remove camera toggle from small mode to reduce vertical space
		dbc.CardFooter(
			daq.BooleanSwitch(
				# Matches the Flatly theme 'success' colour used in the attention header
				color='#18BC9C',
				id='cam-toggle',
				label='Visual attention',
				labelPosition='bottom',
				style={'color': 'black'},
			),
			className='py-1'
		)
	],
	color='success',
	inverse=True,
	outline=True,
	# Some cards are forced to 100% height so that arrows always connect cleanly
	style={'height': '100%'}
),

modal_tab = dbc.Tab(
	[
		# dashboard_graphs['aural_large'],
		dbc.CardBody(
			[
				# html.H6(
				# 	'Visual',
				# 	className='card-subtitle',
				# 	style={
				# 		'color'     : 'black',
				# 		'text-align': 'center'
				# 	}
				# ),
				html.Div(
					[
						html.Img(
							id='camera-img-left-large',
							style={
								'height': con.CAM_HEIGHT_LARGE,
								'width' : con.CAM_WIDTH_LARGE
							}
						),
						html.Img(
							id='camera-img-right-large',
							style={
								'height': con.CAM_HEIGHT_LARGE,
								'width' : con.CAM_WIDTH_LARGE
							}
						),
						html.Div(
							[
								html.Img(
									id='camera-pri-left-large',
									style={
										'height' : con.CAM_HEIGHT_LARGE,
										'width'  : con.CAM_WIDTH_LARGE,
										'opacity': con.PRI_OPACITY,
									}
								),
								html.Img(
									id='camera-pri-right-large',
									style={
										'height' : con.CAM_HEIGHT_LARGE,
										'width'  : con.CAM_WIDTH_LARGE,
										'opacity': con.PRI_OPACITY,
									}
								),
							],
							style={
								'float'   : 'left',
								'position': 'absolute',
								'left'    : '0px',
								'top'     : '0px',
								'z-index' : '2'
							}
						)
					],
					# Necessary for attention image to overlay vision
					style={'position': 'relative'}
				),
			],
		),
		daq.BooleanSwitch(
			color='#18BC9C',
			id='cam-toggle-large',
			label='Visual attention',
			labelPosition='bottom',
		),
		# dashboard_alerts['ball_large'],
		# dashboard_alerts['face_large'],
	],
	label='Live data'
)
