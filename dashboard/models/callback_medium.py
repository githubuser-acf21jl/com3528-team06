# Plotly Dash modules
from dash.dependencies import Input, Output

# MiRo dashboard modules
from app import app
import dashboard_constants as con

# MiRo interface modules
from models.basic_functions import miro_ros_interface as mri

# Other modules
import base64
import cv2

# Initialise MiRo clients
miro_core = mri.MiRoCore()
miro_perception = mri.MiRoPerception()


@app.callback(
	[
		Output('audio-pri-wide', 'src'),
		Output('camera-img-left', 'src'),
		Output('camera-img-right', 'src'),
		Output('camera-pri-left', 'src'),
		Output('camera-pri-right', 'src'),
		Output('camera-img-left-large', 'src'),
		Output('camera-img-right-large', 'src'),
		Output('camera-pri-left-large', 'src'),
		Output('camera-pri-right-large', 'src'),
	],
	[
		Input('interval-medium', 'n_intervals'),
		Input('cam-toggle', 'on'),
		Input('cam-toggle-large', 'on')
	]
)
def callback_medium(_, toggle, toggle_large):
	def process_frame(frame, scale):
		# Resize image for speedier updates
		frame_sml = cv2.resize(frame, tuple(int(dim / scale) for dim in frame.shape[:2]))

		# Create base64 URI from OpenCV image: https://jdhao.github.io/2020/03/17/base64_opencv_pil_image_conversion/
		_, im_arr = cv2.imencode('.png', frame_sml)
		im_bytes = im_arr.tobytes()
		im_b64 = base64.b64encode(im_bytes)

		return 'data:image/png;base64,{}'.format(im_b64.decode())

	if miro_perception.caml is not None:
		caml = miro_perception.caml
		camr = miro_perception.camr
		pril = miro_core.pril
		prir = miro_core.prir
		priw = miro_core.priw

		caml_image = process_frame(caml, con.CAM_SCALE)
		camr_image = process_frame(camr, con.CAM_SCALE)

		if pril is not None and (toggle or toggle_large):
			pril_image = process_frame(pril, 1)
			prir_image = process_frame(prir, 1)
		else:
			pril_image = prir_image = None

		# TODO: Change to EAF method
		if priw is not None:
			priw_image = process_frame(priw, 1)
		else:
			priw_image = con.ASSET_PATH + 'test_priw.png'

	else:
		# Show test patterns
		caml_image = camr_image = con.ASSET_PATH + 'test_cam_sml.png'
		pril_image = prir_image = None
		priw_image = con.ASSET_PATH + 'test_priw.png'

	# Return all outputs
	return \
		priw_image, \
		caml_image, \
		camr_image, \
		pril_image, \
		prir_image, \
		caml_image, \
		camr_image, \
		pril_image, \
		prir_image
