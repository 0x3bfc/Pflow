from flask import Flask
from flask import render_template
from network.simple_network import SimpleNetwork

app = Flask(__name__)

# /gsy/api/v1.0/load
# /gsy/api/v1.0/generator


@app.route('/<string:element>/', methods=['GET'])
def get_load_results(element):
    if element == 'generator':
        element = 'gen'
    return simple_net.get(element)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # setup network
    simple_net = SimpleNetwork()
    simple_net.setup()
    # calc power flow
    simple_net.calc()
    simple_net.render_to_html()
    # start server
    app.run(debug=True, port=8000)
