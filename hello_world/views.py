from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request

my_name = "Lukasz"
msg = "Greetings from DevOps class!"

@app.route('/')
def index():
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, my_name, output.lower())

@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)

