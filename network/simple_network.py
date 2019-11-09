import pandapower as pp
from pandapower.plotting import to_html


class SimpleNetwork:
    # create empty net
    net = pp.create_empty_network()

    def setup(self):
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

    def calc(self):
        return pp.runpp(self.net)

    def get(self, element):
        return eval('self.net.res_' + element + '.to_html()')

    def render_to_html(self):
        to_html(self.net, './templates/index.html')

