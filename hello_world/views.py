from hello_world import app
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST


my_name = "Lukasz"
msg = "Greetings from DevOps class!"

REQUEST_COUNTER = Counter(
    "hello_world_requests_total",
    "Total number of HTTP requests handled by the demo application",
    ["endpoint"]
)


@app.route('/')
def index():
    REQUEST_COUNTER.labels(endpoint="/").inc()
    output = request.args.get('output')
    if not output:
        output = PLAIN
    return get_formatted(msg, my_name, output.lower())


@app.route('/outputs')
def supported_output():
    REQUEST_COUNTER.labels(endpoint="/outputs").inc()
    return ", ".join(SUPPORTED)


@app.route('/metrics')
def metrics():
    REQUEST_COUNTER.labels(endpoint="/metrics").inc()
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
