import gpio
from flask import Flask, render_template

app = Flask(__name__)

gpio.setmode(gpio.BCM)
gpio.setwarnings(True)

led = 26
ledStatus = 0

gpio.setup(led, gpio.OUT)
gpio.output(led, gpio.LOW)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<device>/<status>')
def action(device, status):
    if device == 'matrix':
        actuator = 'matrix'
    else:
        actuator = 'matrix'

    if status == 'on':
        gpio.output(actuator, gpio.HIGH)
    if status == 'off':
        gpio.output(actuator, gpio.LOW)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
