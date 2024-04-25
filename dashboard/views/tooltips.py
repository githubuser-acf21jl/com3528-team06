# Plotly Dash modules
from dash import html
import dash_bootstrap_components as dbc

# As arrows comprise multiple lines spread across multiple rows and columns,
# and each tooltip requires a unique ID, tooltip messages must be repeated to occur along the entire arrow
# Instead, tooltips currently only appear for arrow terminators
dashboard_tooltips = html.Div([
	# Row 1
	dbc.Tooltip(
		'Motor pattern output',
		target='tooltip-top-sum'
	),

	# Row 3
	dbc.Tooltip(
		'Predicted state',
		target='tooltip-motor-action',
	),
	dbc.Tooltip(
		'Spatial priority',
		target='tooltip-spatial-action',
	),
	dbc.Tooltip(
		'Action success / failure',
		target='tooltip-action-affect',
	),
	dbc.Tooltip(
		'Downstream effects on affective state',
		target='tooltip-top-affect',
	),

	# Row 4
	# dbc.Tooltip(
	# 	'Perception',
	# 	target='tooltip-environment-filter',
	# ),
	dbc.Tooltip(
		'Spatial bias and inhibition of return',
		target='tooltip-top-spatial',
	),

	# Row 5
	dbc.Tooltip(
		'Current state',
		target='tooltip-sensory-spatial',
	),
	dbc.Tooltip(
		'Base arousal',
		target='tooltip-circadian-affect',
	),
	dbc.Tooltip(
		'Touch, sound, light, tilt',
		target='tooltip-bottom-affect',
	),

	# Row 6
	dbc.Tooltip(
		'Current pose',
		target='tooltip-sensory-motor',
	),

	# Row 7
	dbc.Tooltip(
		'Motor efferent',
		target='tooltip-motor-bottom',
	),
	dbc.Tooltip(
		'Motor afferent',
		target='tooltip-bottom-sensory',
	),
	dbc.Tooltip(
		'Light',
		target='tooltip-bottom-circadian',
	),
])
