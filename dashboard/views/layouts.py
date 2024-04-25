# Plotly Dash modules
import plotly.graph_objs as go

# MiRo dashboard modules
import dashboard_constants as con

dashboard_layouts = {
	# Action selection
	# TODO: Extract this list automatically
	'action_list'      : [
		'Mull',
		'Orient',
		'Approach',
		'Flee',
		'Avert',
		'Halt',
		'Retreat',
		'Special'
	],
	'action_layout'    : go.Layout(
		bargap=0.1,
		barmode='overlay',
		margin={
			'b': 40,
			'l': 60,
			'r': 0,
			't': 0
		},
		xaxis={
			'fixedrange': True,
			'range'     : [-1, 1],
			'ticktext'  : [1, 0.5, 0, 0.5, 1],
			'tickvals'  : [-1, -0.5, 0, 0.5, 1],
			'title'     : 'Salience'
		},
		yaxis={
			'fixedrange'   : True,
			'tickfont.size': 11
		}
	),

	# Affect
	'affect_layout'    : go.Layout(
		legend={
			'orientation': 'h',
			'x'          : 0.5,
			'xanchor'    : 'center',
			'y'          : 1.01,
			'yanchor'    : 'bottom',
		},
		margin={
			'b': 30,
			'l': 20,
			'r': 5,
			't': 0
		},
		showlegend=True,
		xaxis={
			'fixedrange'    : True,
			'linewidth'     : 0.5,
			'mirror'        : True,
			'range'         : [0, 1],
			'showgrid'      : False,
			'showticklabels': False,
			'title'         : 'Valence',
			'zeroline'      : False,
		},
		yaxis={
			'fixedrange'    : True,
			'linewidth'     : 0.5,
			'mirror'        : True,
			'range'         : [0, 1],
			'showgrid'      : False,
			'showticklabels': False,
			'title'         : 'Arousal',
			'zeroline'      : False,
		},
	),

	# Motivation
	'motivation_layout': go.Layout(
		legend={
			# 'font'       : {
			# 	'size': 3
			# },
			'orientation': 'h',
			'x'          : 1,
			'xanchor'    : 'right',
			'y'          : 1,
			'yanchor'    : 'bottom',
		},
		margin={
			'b': 20,
			'l': 20,
			'r': 0,
			't': 0
		},
		# showlegend=True,
		xaxis={
			'fixedrange'    : True,
			'range'         : [0, con.MOTIVATION_LENGTH],
			'showgrid'      : False,
			'showticklabels': False,
			'title'         : 'Time',
			'zeroline'      : True
		},
		yaxis={
			'fixedrange'    : True,
			'range'         : [0, 1],
			'showgrid'      : False,
			'showticklabels': False,
			'title'         : 'Energy',
			'zeroline'      : True
		}
	),

	# Aural
	'aural_layout'     : go.Layout(
		height=con.PRIW_HEIGHT,
		margin={
			'b': 0,
			'l': 0,
			'r': 0,
			't': 30
		},
		shapes=[
			{
				'line': {
					'color': 'silver',
					'dash' : 'dot',
					'width': 1,
				},
				'type': 'line',
				'x0'  : 0.5,
				'x1'  : 0.5,
				'xref': 'paper',
				'y0'  : 0,
				'y1'  : 1,
				'yref': 'paper'
			}
		],
		# images=priw_image,
		title={
			'pad'    : {
				'b': 10,
				'l': 0,
				'r': 0,
				't': 0
			},
			'text'   : 'Aural',
			'yanchor': 'bottom',
			'y'      : 1,
			'yref'   : 'paper'
		},
		xaxis={
			'fixedrange': True,
			'visible'   : False
		},
		yaxis={
			'fixedrange': True,
			'visible'   : False
		}
	),

	# Vision
	'camera_layout'    : go.Layout(
		height=con.CAM_HEIGHT,
		# images=cam_images,
		margin={
			'b': 10,
			'l': 0,
			'r': 0,
			't': 60
		},
		shapes=[{
			'line': {
				'color': 'black',
				'dash' : 'dot',
				'width': 1,
			},
			'type': 'line',
			'x0'  : 0.5,
			'x1'  : 0.5,
			'xref': 'paper',
			'y0'  : 0,
			'y1'  : 1,
			'yref': 'paper'
		}],
		title={
			'pad'    : {
				'b': 10,
				'l': 0,
				'r': 0,
				't': 0
			},
			'text'   : 'Visual',
			'yanchor': 'bottom',
			'y'      : 1,
			'yref'   : 'paper'
		},
		xaxis={
			'fixedrange': True,
			'visible'   : False
		},
		yaxis={
			'fixedrange': True,
			'visible'   : False
		}
	),

	# Camera images
	'caml_image'       : {
		'layer'  : 'below',
		'opacity': 1,
		'sizing' : 'contain',
		'sizex'  : 0.5,
		'sizey'  : 1,  # Overridden by 'constrain' property but must still be set
		# 'source' : caml,
		'x'      : 0,
		'xanchor': 'left',
		'xref'   : 'paper',
		'y'      : 0,
		'yanchor': 'bottom',
		'yref'   : 'paper',
	},
	'camr_image'       : {
		'layer'  : 'below',
		'opacity': 1,
		'sizing' : 'contain',
		'sizex'  : 0.5,
		'sizey'  : 1,
		# 'source' : camr,
		'x'      : 1,
		'xanchor': 'right',
		'xref'   : 'paper',
		'y'      : 0,
		'yanchor': 'bottom',
		'yref'   : 'paper',
	},
	'pril_image'       : {
		'layer'  : 'above',
		'opacity': 0.5,
		'sizing' : 'contain',
		'sizex'  : 0.5,
		'sizey'  : 1,
		# 'source' : pril,
		'x'      : 0,
		'xanchor': 'left',
		'xref'   : 'paper',
		'y'      : 0,
		'yanchor': 'bottom',
		'yref'   : 'paper',
	},
	'prir_image'       : {
		'layer'  : 'above',
		'opacity': 0.5,
		'sizing' : 'contain',
		'sizex'  : 0.5,
		'sizey'  : 1,
		# 'source' : prir,
		'x'      : 1,
		'xanchor': 'right',
		'xref'   : 'paper',
		'y'      : 0,
		'yanchor': 'bottom',
		'yref'   : 'paper',
	}
}

# Add modified layouts
# go.Layout creates a special type of dict that can't be copied using dict() methods
dashboard_layouts['sleep_layout'] = go.Layout(dashboard_layouts['affect_layout'])
dashboard_layouts['sleep_layout']['xaxis']['title'] = 'Wakefulness'
dashboard_layouts['sleep_layout']['yaxis']['title'] = 'Pressure'
