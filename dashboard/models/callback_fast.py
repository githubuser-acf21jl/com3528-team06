# Plotly Dash modules
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

# MiRo dashboard modules
from app import app
import dashboard_constants as con
from views.faces import affect_faces, sleep_faces
from views.layouts import dashboard_layouts

# MiRo interface modules
from models.basic_functions import miro_ros_interface as mri

# Other modules
import numpy as np

# Initialise MiRo clients
miro_core = mri.MiRoCore()


@app.callback(
	[
		# FIXME: Update alert code in MRI
		# Output('ball-alert', 'is_open'),
		# Output('ball-alert-large', 'is_open'),
		# Output('face-alert', 'is_open'),
		# Output('face-alert-large', 'is_open'),
		Output('action-graph', 'figure'),
		Output('action-graph-large', 'figure'),
		Output('affect-graph', 'figure'),
		Output('affect-graph-large', 'figure'),
		Output('sleep-graph-large', 'figure'),
		Output('motivation-graph', 'figure'),
		Output('motivation-graph-large', 'figure'),
		Output('motivation_memory', 'data')
	],
	[Input('interval-fast', 'n_intervals')],
	[State('motivation_memory', 'data')]
)
def callback_fast(_, data):
	# Initialise output data dictionary
	output = {}

	# FIXME: Update or remove ball and face alerts
	# # Ball alert
	# if (miro_ros_data.core_detect_ball_l is not None) and (miro_ros_data.core_detect_ball_r is not None):
	# 	if (len(miro_ros_data.core_detect_ball_l.data) > 1) or (len(miro_ros_data.core_detect_ball_r.data) > 1):
	# 		output['ball-alert'] = True
	# 		output['ball-alert-large'] = True
	# 	else:
	# 		output['ball-alert'] = False
	# 		output['ball-alert-large'] = False
	#
	# # Face alert
	# if (miro_ros_data.core_detect_face_l is not None) and (miro_ros_data.core_detect_face_r is not None):
	# 	if (len(miro_ros_data.core_detect_face_l.data) > 1) or (len(miro_ros_data.core_detect_face_r.data) > 1):
	# 		output['face-alert'] = True
	# 		output['face-alert-large'] = True
	# 	else:
	# 		output['face-alert'] = False
	# 		output['face-alert-large'] = False

	# Action selection
	if (miro_core.selection_priority is not None) and (miro_core.selection_inhibition is not None):
		action_inhibition = np.array(miro_core.selection_inhibition.data)
		# Priority is made negative so it appears to the left of the bar chart
		action_priority = np.array([-x for x in miro_core.selection_priority.data])
	else:
		action_inhibition = [0]
		action_priority = [0]

	action_data = [
		go.Bar(
			hoverinfo='text+y',
			# Format input label to three decimal places
			# hovertext=np.round(-action_priority, decimals=3),
			marker={'color': '#F39C12'},  # Match header colour
			name='Input',
			orientation='h',
			x=action_priority,
			y=dashboard_layouts['action_list']
		),
		go.Bar(
			hoverinfo='none',
			marker={'color': '#95a5a6'},  # Match Flatly theme grey
			name='Output',
			orientation='h',
			x=action_inhibition,
			y=dashboard_layouts['action_list'],
		)
	]

	output['action-graph'] = {
		'data'  : action_data,
		'layout': dashboard_layouts['action_layout']
	}
	output['action-graph-large'] = {
		'data'  : action_data,
		'layout': dashboard_layouts['action_layout']
	}

	# Affect
	if miro_core.emotion is not None:
		affect_data = {
			'emotion': go.Scatter(
				# TODO: Make hovertext show both X and Y values together
				marker={
					'color': 'steelblue',
					'size' : 15,
					'line' : {
						'width': 0.5,
						'color': 'black'
					}
				},
				mode='markers',
				name='Emotion',
				opacity=0.7,
				x=np.array(np.round(miro_core.emotion.valence, decimals=3)),
				y=np.array(np.round(miro_core.emotion.arousal, decimals=3)),
			),
			'mood'   : go.Scatter(
				marker={
					'color': 'seagreen',
					'size' : 15,
					'line' : {
						'width': 0.5,
						'color': 'black'
					}
				},
				mode='markers',
				name='Mood',
				opacity=0.7,
				x=np.array(np.round(miro_core.mood.valence, decimals=3)),
				y=np.array(np.round(miro_core.mood.arousal, decimals=3)),
			),
			'sleep'  : go.Scatter(
				marker={
					'color': 'salmon',
					'size' : 15,
					'line' : {
						'width': 0.5,
						'color': 'black'
					}
				},
				mode='markers',
				name='Wakefulness',
				opacity=0.7,
				x=np.array(np.round(miro_core.sleep.wakefulness, decimals=3)),
				y=np.array(np.round(miro_core.sleep.pressure, decimals=3)),
			)
		}

		# Get the appropriate face from the 'faces' dictionary based on current mood values
		for x in np.arange(0, 1, 0.2):
			for y in np.arange(0, 1, 0.3):
				# TODO: Change this, shouldn't be an if statement
				if (x < affect_data['mood'].x <= x + 0.2) and (y < affect_data['mood'].y <= y + 0.3):
					# Round the results to nearest 0.1 to prevent floating point errors; inaccurate but unimportant
					affect_face = affect_faces['{0:.1f}'.format(x)]['{0:.1f}'.format(y)]

		for x in np.arange(0, 1, 0.25):
			# TODO: Change this, shouldn't be an if statement
			if x < affect_data['sleep'].x <= x + 0.25:
				sleep_face = sleep_faces['{0:.2f}'.format(x)]

		# Update faces
		dashboard_layouts['affect_layout']['images'] = [{
			'layer'  : 'below',
			'opacity': 0.8,
			'sizing' : 'contain',
			'sizex'  : 0.3,
			'sizey'  : 0.3,
			'source' : affect_face,
			'x'      : 0.5,
			'y'      : 0.5,
			'xanchor': 'center',
			'yanchor': 'middle'
		}]

		# TODO: If possible, just modify the 'source' attribute
		dashboard_layouts['sleep_layout']['images'] = [{
			'layer'  : 'below',
			'opacity': 0.8,
			'sizing' : 'contain',
			'sizex'  : 0.3,
			'sizey'  : 0.3,
			'source' : sleep_face,
			'x'      : 0.5,
			'y'      : 0.5,
			'xanchor': 'center',
			'yanchor': 'middle'
		}]

		affect_figure = {
			'data'  : [
				affect_data['emotion'],
				affect_data['mood'],
				affect_data['sleep']
			],
			'layout': dashboard_layouts['affect_layout']
		}

		affect_figure_large = {
			'data'  : [
				affect_data['emotion'],
				affect_data['mood'],
			],
			'layout': dashboard_layouts['affect_layout']
		}

		sleep_figure_large = {
			'data'  : [affect_data['sleep']],
			'layout': dashboard_layouts['sleep_layout']
		}

		output['affect-graph'] = affect_figure
		output['affect-graph-large'] = affect_figure_large
		output['sleep-graph-large'] = sleep_figure_large

	else:
		# TODO: Tidy up layout when no data is present
		pass

		output['affect-graph'] = {'layout': dashboard_layouts['affect_layout']}
		output['affect-graph-large'] = {'layout': dashboard_layouts['affect_layout']}
		output['sleep-graph-large'] = {'layout': dashboard_layouts['affect_layout']}

	# Motivation
	motivation_input = data
	if miro_core.motivation is not None:
		motivation_input['social'].append(miro_core.motivation.data[0])
		motivation_input['ball'].append(miro_core.motivation.data[1])

		# Trim data to plot length
		if len(motivation_input['social']) >= con.MOTIVATION_LENGTH:
			motivation_input['social'].pop(0)
			motivation_input['ball'].pop(0)

		motivation_data = {
			'social': go.Scatter(
				hoverinfo='none',
				marker={
					'color': 'steelblue',
					'size' : 15,
					'line' : {'width': 0.5}
				},
				mode='lines',
				name='Social',
				opacity=0.7,
				x=np.arange(0, con.MOTIVATION_LENGTH, 1),
				y=np.array(motivation_input['social']),
			),
			'ball'  : go.Scatter(
				hoverinfo='none',
				marker={
					'color': 'mediumseagreen',
					'size' : 15,
					'line' : {'width': 0.5}
				},
				mode='lines',
				name='Ball',
				opacity=0.7,
				x=np.arange(0, con.MOTIVATION_LENGTH, 1),
				y=np.array(motivation_input['ball']),
			),
		}

		motivation_figure = {
			'data'  : [
				motivation_data['social'],
				motivation_data['ball'],
			],
			'layout': dashboard_layouts['motivation_layout']
		}

		motivation_figure_large = {
			'data'  : [
				motivation_data['social'],
				motivation_data['ball'],
			],
			'layout': dashboard_layouts['motivation_layout']
		}

		output['motivation-graph'] = motivation_figure
		output['motivation-graph-large'] = motivation_figure_large

	else:
		output['motivation-graph'] = {'layout': dashboard_layouts['motivation_layout']}
		output['motivation-graph-large'] = {'layout': dashboard_layouts['motivation_layout']}

	# Return all outputs
	return \
		output['action-graph'], \
		output['action-graph-large'], \
		output['affect-graph'], \
		output['affect-graph-large'], \
		output['sleep-graph-large'], \
		output['motivation-graph'], \
		output['motivation-graph-large'], \
		motivation_input

# FIXME: Alerts are broken until MRI is updated
# output['ball-alert'], \
# output['ball-alert-large'], \
# output['face-alert'], \
# output['face-alert-large'], \
# output['action-graph'], \
# output['action-graph-large'], \
# output['affect-graph'], \
# output['affect-graph-large'], \
# output['sleep-graph-large']
