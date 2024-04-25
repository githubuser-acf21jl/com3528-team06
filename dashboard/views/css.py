# MiRo dashboard modules
import dashboard_constants as con

# Custom CSS for lines and arrows
css = {
	'arrow_down'                : {
		'border-left' : str(con.A_WIDTH) + 'px solid white',
		'border-right': str(con.A_WIDTH) + 'px solid white',
		'border-top'  : str(con.A_HEIGHT) + 'px solid ' + con.L_COLOUR,
		'height'      : 0,
		'margin'      : 'auto',
		'position'    : 'relative',
		'bottom'      : str(con.A_HEIGHT) + 'px',
		'width'       : 0
	},
	'arrow_left'                : {
		'border-bottom': str(con.A_WIDTH) + 'px solid white',
		'border-right' : str(con.A_HEIGHT) + 'px solid ' + con.L_COLOUR,
		'border-top'   : str(con.A_WIDTH) + 'px solid white',
		'float'        : 'left',
		'height'       : 0,
		'margin-top'   : str(con.A_VERT_OFFSET) + 'px',
		'width'        : 0
	},
	'arrow_right'               : {
		'border-bottom': str(con.A_WIDTH) + 'px solid white',
		'border-left'  : str(con.A_HEIGHT) + 'px solid ' + con.L_COLOUR,
		'border-top'   : str(con.A_WIDTH) + 'px solid white',
		'float'        : 'right',
		'height'       : 0,
		'margin-top'   : str(con.A_VERT_OFFSET) + 'px',
		'width'        : 0
	},
	'arrow_right_clear'         : {
		'border-bottom': str(con.A_WIDTH) + 'px solid transparent',
		'border-left'  : str(con.A_HEIGHT) + 'px solid transparent',
		'border-top'   : str(con.A_WIDTH) + 'px solid transparent',
		'float'        : 'right',
		'height'       : 0,
		'margin-top'   : str(con.A_VERT_OFFSET) + 'px',
		'width'        : 0
	},
	'arrow_up'                  : {
		'border-bottom': str(con.A_HEIGHT) + 'px solid ' + con.L_COLOUR,
		'border-left'  : str(con.A_WIDTH) + 'px solid white',
		'border-right' : str(con.A_WIDTH) + 'px solid white',
		'height'       : 0,
		'margin'       : 'auto',
		'width'        : 0
	},
	# TODO: Make text go from bottom to top
	'bar_left'                  : {
		'background-color'          : con.E_COLOUR,
		'border-top-right-radius'   : '10px',
		'border-bottom-right-radius': '10px',
		'color'                     : 'white',
		'float'                     : 'left',
		'font-weight'               : 'bold',
		'height'                    : '100%',
		'left'                      : 0,
		'position'                  : 'absolute',
		'text-align'                : 'center',
		'width'                     : str(con.E_WIDTH) + 'px',
		'writing-mode'              : 'sideways-lr'
	},
	'line_horizontal'           : {
		'background-color': con.L_COLOUR,
		'border-bottom'   : str(con.L_BORDER) + 'px white solid',
		'border-top'      : str(con.L_BORDER) + 'px white solid',
		'float'           : 'right',
		'height'          : str(con.H_WIDTH) + 'px',
		'width'           : '100%',
		'margin-top'      : str(con.L_VERT_OFFSET) + 'px',
	},
	'line_horizontal_clear'     : {
		'border-bottom': str(con.L_BORDER) + 'px white transparent',
		'border-top'   : str(con.L_BORDER) + 'px white transparent',
		'float'        : 'right',
		'height'       : str(con.H_WIDTH) + 'px',
		'width'        : '100%',
		'margin-top'   : str(con.L_VERT_OFFSET) + 'px',
	},
	'line_horizontal_clear_left': {
		'background-color': 'white',
		'border-right'    : str(con.V_WIDTH) + 'px ' + con.L_COLOUR + ' solid',
		'height'          : str(con.H_WIDTH - con.L_BORDER) + 'px',
		# 'width'           : '52%',
		'width': '52%',
		'position'        : 'absolute',
		# 'right'           : '48%',
		'right'           : '48.5%',
		'top'             : str(con.L_VERT_OFFSET) + 'px'
	},
	'line_vertical'             : {
		'background-color': con.L_COLOUR,
		'height'          : '100%',
		'width'           : str(con.V_WIDTH) + 'px',
		'margin'          : 'auto',
		'min-height'      : str(con.V_HEIGHT) + 'px',
	},
}
