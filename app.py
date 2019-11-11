from flask import Flask
from flask import render_template
from network.simple_network import SimpleNetwork

app = Flask(__name__)
simple_net = SimpleNetwork()


@app.route('/<string:element>/', methods=['GET'])
def get_results(element):
    """
    get the cached results of a component. It will return 404 page
    if the component doesn't exist
    :param element: topology component (load, generator, line, bus, etc)
    :return: html response that has the component results
    """
    if element == 'generator':
        element = 'gen'
    try:
        return simple_net.get(element)
    except:
        return render_template('404.html'), 404


@app.route('/', methods=['GET'])
def index():
    """
    loads the index.html
    :return:  index.html
    """
    return render_template('index.html')


if __name__ == '__main__':
    # setup network
    simple_net.setup()
    # calc power flow
    simple_net.run()
    # generate index.html
    simple_net.render()
    # start server
    app.run(debug=True, host='0.0.0.0', port=8000)
