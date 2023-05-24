from pytest import approx
from math import sqrt
from shadow.polyedr import Polyedr
from common.tk_drawer import TkDrawer

tk = TkDrawer()

class TestPolyedr:

    def test_0(self):
        assert Polyedr(f"data/ccc.geom").sum_of_edges() == 0.0

    def test_1(self):
        assert Polyedr(f"data_tests/test1.geom").sum_of_edges() == 0.0

    def test_2(self):
        assert Polyedr(f"data_tests/test2.geom").sum_of_edges() == 0.0

    def test_3(self):
        assert Polyedr(f"data_tests/test3.geom").sum_of_edges() == 400.0

    def test_4(self):
        assert Polyedr(f"data_tests/test4.geom").sum_of_edges() == 50.0

    def test_5(self):
        assert Polyedr(f"data_tests/test5.geom").sum_of_edges() == 600.0

    def test_6(self):
        assert Polyedr(f"data_tests/test6.geom").sum_of_edges() == 50.0

    def test_7(self):
        assert Polyedr(f"data_tests/test7.geom").sum_of_edges() == 0.0
