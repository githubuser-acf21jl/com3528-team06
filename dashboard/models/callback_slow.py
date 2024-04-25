# Plotly Dash modules
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# MiRo dashboard modules
from app import app

# MiRo interface modules
from models.basic_functions import miro_ros_interface as mri

# Initialise MiRo clients
miro_core = mri.MiRoCore()


@app.callback(
	Output('circadian-graph', 'figure'),
	[Input('interval-slow', 'n_intervals')]
)
def callback_slow(_):
	# Initialise output data dictionary
	output = {}

	# Circadian graph
	if miro_core.time is not None:
		time_raw = miro_core.time_raw
	else:
		time_raw = 0

	# Multiply fractional day by 720 to get 12-hour time
	# Subtract 30 because polar clock display uses 1 as the origin
	circ_hrs = (time_raw * 720) - 30

	# Remainder from raw time * 24 == minutes
	_, raw_min = divmod(time_raw * 24, 1)
	circ_min = (raw_min * 360) - 30

	# Set clock hand width and length
	hand_width = 40
	hr_hand_length = 0.6
	min_hand_length = 0.9

	# TODO: Disable polar plot zoom
	circ_data = [
		# Minute hand
		go.Scatterpolar(
			fill='toself',
			fillcolor='lightsteelblue',
			hoverinfo='none',
			line={
				'color': 'black',
				'width': 0.5,
			},
			mode='lines',
			# name='Minutes',
			r=[0, 0.1, min_hand_length, 0.1, 0],
			theta=[
				0,
				circ_min - hand_width,
				circ_min,
				circ_min + hand_width,
				0
			]
		),
		# Hour hand
		go.Scatterpolar(
			fill='toself',
			fillcolor='steelblue',
			hoverinfo='none',
			line={
				'color': 'black',
				'width': 0.5,
			},
			mode='lines',
			# name='Hours',
			r=[0, 0.1, hr_hand_length, 0.1, 0],
			theta=[
				0,
				circ_hrs - hand_width,
				circ_hrs,
				circ_hrs + hand_width,
				0
			]
		)
	]

	# circ_axis = {
	# 	'fixedrange'    : True,
	# 	'linewidth'     : 0,
	# 	'mirror'        : True,
	# 	'range'         : [0, 1],
	# 	'showgrid'      : False,
	# 	'showticklabels': False,
	# 	'zeroline'      : False,
	# }

	circ_layout = go.Layout(
		# images=[{
		# 	'opacity': 1,
		# 	'sizing' : 'contain',
		# 	'sizex'  : 1,
		# 	'sizey'  : 1,
		# 	'source' : con.ASSET_PATH + 'clock_' + str(circ_input) + '.png',
		# 	'x'      : 0.5,
		# 	'y'      : 0.5,
		# 	'xanchor': 'center',
		# 	'yanchor': 'middle'
		# }],
		margin={
			'b': 20,
			'l': 20,
			'r': 20,
			't': 20
		},
		# xaxis=circ_axis,
		# yaxis=circ_axis,
		polar={
			'angularaxis': {
				'direction': 'clockwise',
				'rotation' : 60,
				'showgrid' : False,
				'thetaunit': 'degrees',
				'tickmode' : 'array',
				'ticktext' : ['{:d}'.format(hr) for hr in range(1, 13)],
				'tickvals' : [d for d in range(0, 360, 30)],
				'type'     : 'linear'
			},
			'radialaxis' : {
				'range'  : [0, 1],
				'visible': False
			},
		},
		showlegend=False
	)

	output['circadian-graph'] = {
		'data'  : circ_data,
		# 'data'  : None,
		'layout': circ_layout
	}

	# Return all outputs
	return output['circadian-graph']
