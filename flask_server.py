from flask import Flask, render_template, request
import jsonreg
#import services.gpio as GPIO
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/set')
def set():
    pin = request.args.get("pin", type=str)
    mode = request.args.get("mode", type=str)
    print(pin)
    #GPIO.configure(pin,mode)
    return "200"

@app.route('/src/gpio')
def gpio():
    return render_template("gpio.js")

if __name__ == "__main__":
    app.run(port=jsonreg.read("app_config/rpi-gpio-port.json")[0],debug=jsonreg.read("app_config/rpi-gpio-debug.json")[0])
