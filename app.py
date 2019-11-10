from flask import Flask
from flask import render_template
from network.simple_network import SimpleNetwork

app = Flask(__name__)


@app.route('/<string:element>/', methods=['GET'])
def get_load_results(element):
    if element == 'generator':
        element = 'gen'
    try:
        return simple_net.get(element)
    except:
        return render_template('404.html'), 404


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
    app.run(debug=True, host='0.0.0.0', port=8000)
