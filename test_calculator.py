"""
Tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(2, 3)

    def test_sub(self):
        assert 5 == calculator.sub(7, 2)

    def test_mul(self):
        assert 10 == calculator.mul(5, 2)

    def test_div(self):
        assert 4 == calculator.div(12, 3)
