# Plotly Dash modules
from dash import html
import dash_bootstrap_components as dbc

# MiRo dashboard modules
from views.tabs import dashboard_tabs

dashboard_modals = html.Div([
	dbc.Modal(
		[
			dbc.ModalHeader('Action selection'),
			dbc.ModalBody(
				dbc.Tabs([
					dashboard_tabs['action_graph'],
					dashboard_tabs['action_info']
				])
			),
			dbc.ModalFooter(
				dbc.Button(
					'Close',
					id='action-modal-close',
					color='danger',
					className='ml-auto'
				)
			),
		],
		id='action-modal',
		centered=True,
		size='xl'
	),
	dbc.Modal(
		[
			dbc.ModalHeader('Affect'),
			dbc.ModalBody(
				dbc.Tabs([
					dashboard_tabs['affect_graph'],
					dashboard_tabs['affect_info']
				])
			),
			dbc.ModalFooter(
				dbc.Button(
					'Close',
					id='affect-modal-close',
					color='danger',
					className='ml-auto'
				)
			),
		],
		id='affect-modal',
		centered=True,
		size='xl'
	),
	dbc.Modal(
		[
			dbc.ModalHeader('Circadian rhythm'),
			dbc.ModalBody(dashboard_tabs['circadian_info']),
			dbc.ModalFooter(
				dbc.Button(
					'Close',
					id='circadian-modal-close',
					color='danger',
					className='ml-auto'
				)
			),
		],
		id='circadian-modal',
		centered=True,
		size='xl'
	),
	dbc.Modal(
		[
			dbc.ModalHeader('Motivation'),
			dbc.ModalBody(
				dbc.Tabs([
					dashboard_tabs['motivation_graph'],
					dashboard_tabs['motivation_info']
				])
			),
			dbc.ModalFooter(
				dbc.Button(
					'Close',
					id='motivation-modal-close',
					color='danger',
					className='ml-auto'
				)
			),
		],
		id='motivation-modal',
		centered=True,
		size='xl'
	),
	dbc.Modal(
		[
			dbc.ModalHeader('Spatial attention'),
			dbc.ModalBody(
				dbc.Tabs([
					dashboard_tabs['spatial_graph'],
					dashboard_tabs['spatial_info']
				])
			),
			dbc.ModalFooter(
				dbc.Button(
					'Close',
					id='spatial-modal-close',
					color='danger',
					className='ml-auto'
				)
			),
		],
		id='spatial-modal',
		centered=True,
		size='xl'
	)
])
