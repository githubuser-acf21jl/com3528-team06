# Plotly Dash modules
from app import app

# MiRo dashboard modules
# PyCharm will complain these imports are unused, but they definitely are
# Comment these out to test / modify basic layout without a running ROS core
import models.callback_fast
import models.callback_medium
import models.callback_slow
import models.callback_modal

# Separation of app.py and index.py required to allow definition of callbacks in separate files
# See bottom of https://dash.plotly.com/urls

# TODO: Package into easy-install app bundle
# TODO: Move from Scatter() to ScatterGL() (see: https://plot.ly/python/webgl-vs-svg/)

if __name__ == '__main__':
	# Issue the following command to kill the server 
	# sudo fuser 8050/tcp -k
	#
	# Enable to suppress warnings TEMPORARILY
	# app.config['suppress_callback_exceptions'] = True

	# "debug=False" because hot reloading causes "IOError: [Errno 11] Resource temporarily unavailable" errors
	# "host='0.0.0.0'" allows connections from non-localhost addresses
	# I *think* "threaded=True" gives a performance boost to multiple callbacks

	# If running inside WSL, replace 0.0.0.0 with the IP address of your WSL instance

	app.run_server(debug=False, host='0.0.0.0', threaded=True)
