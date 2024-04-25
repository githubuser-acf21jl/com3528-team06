# Plotly Dash modules
from dash import html
import dash_bootstrap_components as dbc

# MiRo dashboard modules
from views.alerts import dashboard_alerts
from views.cards import dashboard_cards
from views.css import css
from views.data_displays import (
	action_selection,
	affect,
	circadian_rhythm,
	motivation,
	spatial_attention
)

dashboard_rows = {
	'Row_top': dbc.Row(
		dbc.Col(dashboard_alerts['to_higher']),
		##no_gutters=True
	),

	'Row_1'  : dbc.Row(
		[
			# Column 4
			dbc.Col(
				[
					html.Div(style=css['line_vertical']),
					html.Div(style=css['arrow_down']),
				],
				id='tooltip-top-sum',
				width={
					'size'  : 1,
					'offset': 3
				},
			),

			# Column 5
			dbc.Col(
				html.Div(style=css['line_vertical']),
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 6
			dbc.Col(
				[
					html.Div(style=css['line_vertical']),
					html.Div(style=css['arrow_down']),
				],
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 10
			dbc.Col(
				[
					html.Div(style=css['arrow_up']),
					html.Div(style=css['line_vertical']),
				],
				width={
					'size'  : 1,
					'offset': 3
				}
			),

			# Column 12
			dbc.Col(
				html.Div(style=css['line_vertical']),
				width={
					'size'  : 1,
					'offset': 1
				}
			),
		],
		##no_gutters=True
	),

	'Row_2'  : dbc.Row(
		[
			# Column 1-3
			dbc.Col(
				dashboard_alerts['intro'],
				width={
					'size'  : 3,
					'offset': 0
				},
			),

			# Column 4
			dbc.Col(
				[
					dashboard_cards['motor_sum'],
					html.Div(style=css['line_vertical']),
				],
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 5
			dbc.Col(
				[
					html.Div(style=css['line_horizontal']),
					html.Div(style=css['arrow_left']),
					html.Div(style=css['line_vertical']),
				],
				width={
					'size'  : 1,
					'offset': 0
				},
			),

			# Column 6-10
			dbc.Col(
				action_selection.card,
				width={
					'size'  : 5,
					'offset': 0
				}
			),

			# Column 12
			dbc.Col(
				html.Div(style=css['line_vertical']),
				width={
					'size'  : 1,
					'offset': 1
				}
			),
		],
		#no_gutters=True
	),

	'Row_3'  : dbc.Row(
		[
			# Column 4
			dbc.Col(
				html.Div(style=css['line_vertical']),
				width={
					'size'  : 1,
					'offset': 3
				}
			),

			# Column 5
			dbc.Col(
				html.Div(style=css['line_vertical']),
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 6
			dbc.Col(
				[
					html.Div(style=css['arrow_up']),
					html.Div(style=css['line_vertical']),
				],
				id='tooltip-motor-action',
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 8
			dbc.Col(
				[
					html.Div(style=css['arrow_up']),
					html.Div(style=css['line_vertical']),
				],
				id='tooltip-spatial-action',
				width={
					'size'  : 1,
					'offset': 1
				}
			),

			# Column 10
			dbc.Col(
				[
					html.Div(style=css['line_vertical']),
					html.Div(style=css['arrow_down']),
				],
				id='tooltip-action-affect',
				width={
					'size'  : 1,
					'offset': 1
				}
			),

			# Column 12
			dbc.Col(
				[
					html.Div(style=css['line_vertical']),
					html.Div(style=css['arrow_down']),
				],
				id='tooltip-top-affect',
				width={
					'size'  : 1,
					'offset': 1
				}
			)
		],
		#no_gutters=True
	),

	'Row_4'  : dbc.Row(
		[
			# Column 1
			dbc.Col(
				[
					html.Div('ENVIRONMENT', style=css['bar_left']),
					html.Div(style=css['line_horizontal_clear']),
					html.Div(style=css['arrow_right_clear']),
					html.Div(style=css['line_horizontal']),
					html.Div(style=css['arrow_right'], ),
					html.Div(style=css['line_horizontal_clear']),
					html.Div(style=css['arrow_right_clear']),
					html.Div(style=css['line_horizontal_clear']),
					html.Div(style=css['arrow_right_clear']),
					# Uncomment to enable motivation graph
					# Motivation START
					# html.Div(style=css['line_horizontal']),
					# html.Div(style=css['arrow_right']),
					# Motivation END
				],
				# dashboard_cards['environment'],
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 2-3
			dbc.Col(
				[
					dashboard_cards['motor_reafferent'],
					# Uncomment to enable motivation graph
					# Motivation START
					# html.Div(style=css['line_horizontal_clear']),
					# Motivation END
					# And remove display=none tag from motivation card
					motivation.card

				],
				width={
					'size'  : 2,
					'offset': 0
				}
			),

			# Column 4
			dbc.Col(
				[
					html.Div(style=css['line_horizontal_clear']),
					html.Div(style=css['arrow_right_clear']),
					html.Div(style=css['line_horizontal']),
					html.Div(style=css['arrow_right_clear']),
					html.Div(style=css['line_horizontal_clear']),
					html.Div(style=css['arrow_right_clear']),
					html.Div(style=css['line_horizontal_clear']),
					html.Div(style=css['arrow_right_clear']),
					# Uncomment to enable motivation graph
					# Motivation START
					# html.Div(style=css['line_horizontal']),
					# html.Div(style=css['arrow_right_clear']),
					# Motivation END
					html.Div(style=css['line_vertical']),
				],
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 5
			dbc.Col(
				html.Div(
					[
						html.Div(style=css['line_horizontal_clear_left']),
						html.Div(style=css['line_horizontal']),
						html.Div(style=css['arrow_right_clear']),
						html.Div(style=css['line_horizontal']),
						html.Div(style=css['arrow_right_clear']),
						html.Div(style=css['line_horizontal_clear']),
						html.Div(style=css['arrow_right_clear']),
						html.Div(style=css['line_horizontal_clear']),
						html.Div(style=css['arrow_right_clear']),
						# Uncomment to enable motivation graph
						# Motivation START
						# html.Div(style=css['line_horizontal']),
						# html.Div(style=css['arrow_right_clear']),
						# Motivation END
						html.Div(style=css['line_vertical']),
					]
				),
				width={
					'size'  : 1,
					'offset': 0
				},
			),

			# Column 6
			dbc.Col(
				[
					html.Div(style=css['line_horizontal']),
					html.Div(
						style=css['arrow_right'],
						id='tooltip-top-spatial'
					),
					html.Div(style=css['line_horizontal']),
					html.Div(style=css['arrow_right']),
					html.Div(style=css['line_horizontal_clear']),
					html.Div(style=css['arrow_right_clear']),
					html.Div(style=css['line_horizontal_clear']),
					html.Div(style=css['arrow_right_clear']),
					# Uncomment to enable motivation graph
					# Motivation START
					# html.Div(style=css['line_horizontal']),
					# html.Div(style=css['arrow_right']),
					# Motivation END
					html.Div(style=css['line_vertical']),
				],
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 7-9
			dbc.Col(
				spatial_attention.card,
				width={
					'size'  : 3,
					'offset': 0
				}
			),

			# Column 10-12
			dbc.Col(
				affect.card,
				width={
					'size'  : 3,
					'offset': 0
				}
			)
		],
		#no_gutters=True
	),

	'Row_5'  : dbc.Row(
		[
			# Column 4
			dbc.Col(
				html.Div(style=css['line_vertical']),
				width={
					'size'  : 1,
					'offset': 3
				}
			),

			# Column 6
			dbc.Col(
				html.Div(style=css['line_vertical']),
				width={
					'size'  : 1,
					'offset': 1
				}
			),

			# Column 8
			dbc.Col(
				[
					html.Div(style=css['arrow_up']),
					html.Div(style=css['line_vertical']),
				],
				id='tooltip-sensory-spatial',
				width={
					'size'  : 1,
					'offset': 1
				}
			),

			# Column 10
			dbc.Col(
				[
					html.Div(style=css['arrow_up']),
					html.Div(style=css['line_vertical']),
				],
				id='tooltip-circadian-affect',
				width={
					'size'  : 1,
					'offset': 1
				}
			),

			# Column 11
			dbc.Col(
				[
					html.Div(style=css['arrow_up']),
					html.Div(style=css['line_vertical']),
				],
				id='tooltip-bottom-affect',
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 12
			dbc.Col(
				[
					html.Div(style=css['line_vertical']),
					html.Div(style=css['arrow_down']),
				],
				width={
					'size'  : 1,
					'offset': 0
				}
			),
		],
		#no_gutters=True
	),

	'Row_6'  : dbc.Row(
		[
			# Column 4
			dbc.Col(
				html.Div(
					[
						html.Div(style=css['line_horizontal_clear_left']),
						html.Div(style=css['line_horizontal']),
						html.Div(style=css['line_vertical']),
					]
				),
				width={
					'size'  : 1,
					'offset': 3
				},
			),

			# Column 5
			dbc.Col(
				[
					html.Div(style=css['line_horizontal']),
					html.Div(style=css['arrow_right']),
				],
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 6
			dbc.Col(
				[
					dashboard_cards['motor_body_model'],
					html.Div(style=css['line_vertical'])
				],
				width={
					'size'  : 1,
					'offset': 0
				},
				style={'overflow': 'hidden'}
			),

			# Column 7
			dbc.Col(
				[
					html.Div(style=css['line_horizontal']),
					html.Div(style=css['arrow_left']),
				],
				id='tooltip-sensory-motor',
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 8
			dbc.Col(
				[
					dashboard_cards['sensory_body_model'],
					html.Div(
						style=css['arrow_up'],
						id='tooltip-bottom-sensory'
					),
					html.Div(style=css['line_vertical'])
				],
				width={
					'size'  : 1,
					'offset': 0
				},
				# Necessary to keep stretched arrows hidden
				style={'overflow': 'hidden'}
			),

			# Column 10
			dbc.Col(
				[
					circadian_rhythm.card,
					html.Div(
						style=css['arrow_up'],
						id='tooltip-bottom-circadian',
					),
					html.Div(style=css['line_vertical']),
				],
				width={
					'size'  : 1,
					'offset': 1
				},
				# Necessary to keep stretched arrows hidden
				style={'overflow': 'hidden'}
			),

			# Column 11
			dbc.Col(
				html.Div(style=css['line_vertical']),
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 12
			dbc.Col(
				[
					dashboard_cards['expression'],
					html.Div(style=css['line_vertical'])
				],
				width={
					'size'  : 1,
					'offset': 0
				},
				style={'overflow': 'hidden'}
			),
		],
		#no_gutters=True
	),

	'Row_7'  : dbc.Row(
		[
			# Column 1-3
			dbc.Col(
				dashboard_alerts['connections'],
				width={
					'size'  : 3,
					'offset': 0
				},
			),

			# Column 6
			dbc.Col(
				[
					html.Div(style=css['line_vertical']),
					html.Div(style=css['arrow_down']),
				],
				id='tooltip-motor-bottom',
				width={
					'size'  : 1,
					'offset': 2
				}
			),

			# Column 8
			dbc.Col(
				html.Div(style=css['line_vertical']),
				width={
					'size'  : 1,
					'offset': 1
				}
			),

			# Column 10
			dbc.Col(
				[
					# html.Div(style=css['arrow_up']),
					html.Div(style=css['line_vertical']),
				],
				# id='tooltip-bottom-circadian',
				width={
					'size'  : 1,
					'offset': 1
				}
			),

			# Column 11
			dbc.Col(
				html.Div(style=css['line_vertical']),
				width={
					'size'  : 1,
					'offset': 0
				}
			),

			# Column 12
			dbc.Col(
				[
					html.Div(style=css['line_vertical']),
					html.Div(style=css['arrow_down']),
				],
				width={
					'size'  : 1,
					'offset': 0
				}
			),
		],
		#no_gutters=True
	),

	'Row_btm': dbc.Row(
		dbc.Col(dashboard_alerts['to_lower']),
		#no_gutters=True
	)
}
