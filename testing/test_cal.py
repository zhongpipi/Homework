import pytest
import yaml

from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()
        print("开始测试")

    def teardown_class(self):
        print("结束测试")

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('datas.yml'))[0])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert abs(result - expect)<0.00001

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('datas.yml'))[1])
    def test_cub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert abs(result - expect)<0.00001

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('datas.yml'))[2])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert abs(result - expect)<0.00001

    @pytest.mark.parametrize('a,b,expect', yaml.safe_load(open('datas.yml'))[3])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert abs(result - expect)<0.00001

    def exception_div(self, a, b):
        result = self.calc.div(a, b)

    @pytest.mark.parametrize('a,b', yaml.safe_load(open('datas.yml'))[4])
    def test_excption_div(self, a, b):
        with pytest.raises(ArithmeticError):
            self.exception_div(a, b)
