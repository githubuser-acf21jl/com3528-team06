# Plotly Dash modules
import dash_bootstrap_components as dbc

# MiRo dashboard modules
import dashboard_constants as con

# Static information cards only; dynamic data cards are in .data_displays
dashboard_cards = {
	'environment'       : dbc.Card(
		[
			dbc.CardHeader('Environment'),
			dbc.CardImg(
				src=con.ASSET_PATH + 'icon_park.png',
				bottom=True
			)
		],
		color='light',
		className='ml-1',
	),
	'expression'        : dbc.Card(
		[
			dbc.CardHeader('Expression'),
			dbc.CardBody(
				dbc.ListGroup(
					[
						dbc.ListGroupItem(
							[
								'Ears',
								dbc.CardImg(
									src=con.ASSET_PATH + 'express_ear.png',
									className='float-right',
									style={'width': '20px'}
								),
							],
							className='py-1'
						),
						dbc.ListGroupItem(
							[
								'Eyelids',
								dbc.CardImg(
									src=con.ASSET_PATH + 'express_eye.png',
									className='float-right',
									style={'width': '20px'}
								),
							],
							className='py-1'
						),
						dbc.ListGroupItem(
							[
								'Lights',
								dbc.CardImg(
									src=con.ASSET_PATH + 'express_lights.png',
									className='float-right',
									style={'width': '20px'}
								),
							],
							className='py-1'
						),
						dbc.ListGroupItem(
							[
								'Tail',
								dbc.CardImg(
									src=con.ASSET_PATH + 'express_dog.png',
									className='float-right',
									style={'width': '20px'}
								),
							],
							className='py-1'
						),
						dbc.ListGroupItem(
							[
								'Vocalisation',
								dbc.CardImg(
									src=con.ASSET_PATH + 'express_speaker.png',
									className='float-right',
									style={'width': '20px'}
								),
							],
							className='py-1'
						),
					],
					className='small',
					flush=True,
				),
				className='border-0 m-0 p-0'
			),
			dbc.CardFooter(
				'➡ Self-activity reports',
				style={'font-size': 'x-small'}
			)
		],
		color='light',
		className='mx-1',
	),
	'motor_body_model'  : dbc.Card(
		[
			dbc.CardBody('Motor body model'),
			dbc.CardFooter(
				'➡ Self-activity reports',
				style={'font-size': 'x-small'}
			)
		],
		color='light'
	),
	'motor_reafferent'  : dbc.Card(
		[
			dbc.CardBody('Motor reafferent noise filter'),
			dbc.CardFooter(
				'➡ Self-activity reports',
				style={'font-size': 'x-small'}
			),
		],
		color='light'
	),
	'motor_sum'         : dbc.Card(
		dbc.CardBody('Sum of current motor output and selected action'),
		color='light',
	),
	'sensory_body_model': dbc.Card(
		dbc.CardBody('Sensory body model'),
		color='light'
	),
}
