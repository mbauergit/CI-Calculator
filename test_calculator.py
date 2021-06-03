"""
Tests for calc app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(2, 3)

    def test_sub(self):
        assert 5 == calculator.sub(7, 2)

