import gpio
from flask import Flask, render_template, request

app = Flask(__name__)

gpio.setmode(gpio.BCM)
gpio.setwarnings(True)

led = 26

gpio.setup(led, gpio.OUT)
gpio.output(led, gpio.LOW)


def changeText(text):
    pass


@app.route('/', methods=['GET', 'POST'])
def index():
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
