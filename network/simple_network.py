import pandapower as pp
from pandapower.plotting import to_html


class SimpleNetwork:
    """SimpleNetwork class is the entry point into simple network topology"""

    def __init__(self):
        """
        Initialize SimpleNetwork Class by creating new empty network
        This class has a hard-coded topology parameters.
        This topology has 3 buses, one generator 0.2MWs, a load, an
        external grid, and a transformer and wired as follows:
            * The external grid is connected to bus1
            * The load and the generator is connected to bus3
            * A transformer is connected to bus2 and bus1
            * Finally, A 100 meters line is connected to bu2, bus3
        """
        self.net = pp.create_empty_network()

    def setup(self):
        """
        Setup the topology, parameters are hardcoded.
        :return: network object that holds the topology
        """
        # create buses
        bus1 = pp.create_bus(self.net, vn_kv=20., name="Bus 1")
        bus2 = pp.create_bus(self.net, vn_kv=0.4, name="Bus 2")
        bus3 = pp.create_bus(self.net, vn_kv=0.4, name="Bus 3")

        # create bus elements
        pp.create_ext_grid(self.net, bus=bus1, vm_pu=1.02, name="Grid Connection")
        pp.create_load(self.net, bus=bus3, p_mw=0.100, q_mvar=0.05, name="Load")
        pp.create_gen(self.net, bus3, p_mw=0.02, name="generator")
        # create branch elements
        pp.create_transformer(self.net, hv_bus=bus1, lv_bus=bus2, std_type="0.4 MVA 20/0.4 kV", name="Trafo")
        pp.create_line(self.net, from_bus=bus2, to_bus=bus3, length_km=0.1, std_type="NAYY 4x50 SE", name="Line")

        return self.net

    def run(self):
        """
        calculate the power flow results. this results will cached
        and served through APIs.
        :return: power flow results
        """
        return pp.runpp(self.net)

    def get(self, element):
        """
        retrieves the cached results for each component in the topology
        :return: results for specific component
        """
        return eval('self.net.res_' + element + '.to_html()')

    def render(self):
        """
        Generate an index.html file which contains the whole topology results
        """
        to_html(self.net, './templates/index.html')

