import logging

import gpio
from flask import Flask, render_template, request

# Flask server
app = Flask(__name__)

# Logging facility
logger = logging.getLogger('LEDMatrix')
logger.setLevel(logging.DEBUG)

# GPIO init
gpio.setmode(gpio.BCM)
gpio.setwarnings(True)

led = 26  # GPIO 26 = yellow LED

gpio.setup(led, gpio.OUT)
gpio.output(led, gpio.LOW)
logger.debug("GPIO initialized.")


def changeText(text):
    logger.debug("Changed text to: %s", text)
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
    logger.debug("entered '/'")
    data = request.form['display']
    changeText(data)
    return render_template('index.html')


@app.route('/<device>/<status>')
def action(device, status):
    if device == 'led':
        actuator = led
    elif device == 'matrix':
        # actuator = matrix
        pass
    else:
        actuator = led

    if status == 'on':
        gpio.output(actuator, gpio.HIGH)
    if status == 'off':
        gpio.output(actuator, gpio.LOW)
    render_template('done.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
