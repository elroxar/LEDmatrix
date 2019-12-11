import logging

import gpio
import werkzeug
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
ledStat = 0 # LED is off

gpio.setup(led, gpio.OUT)
gpio.output(led, gpio.LOW)
logger.debug("GPIO initialized.")


def changeText(text):
    logger.debug("Changed text to: %s", text)
    pass


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handleBadRequest():
    return render_template('done.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    logger.debug("entered '/'")
    if request.method == 'POST':
        data = request.form['display']
        logger.debug("Changing text to %s", data)
        changeText(data)
    return render_template('index.html')


@app.route('/<device>/<status>')
def action(device, status):
    global ledStat
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
    if status == 'toggle':
        if gpio.input(actuator) == 0:
            gpio.output(actuator, gpio.HIGH)
        else:
            gpio.output(actuator, gpio.LOW)
    return render_template('done.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
