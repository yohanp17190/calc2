"""Testing the Calculator"""
import pytest

from calculator.calculator import Calculator

#this is how you define a function that will run each time you pass it to a test, it is called a fixture
@pytest.fixture
def clear_history():
    Calculator.clear_history()

def test_calculator_add_first(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1,2) == 3

def test_calculator_add_second(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(2,2) == 4

def test_calculator_add_third(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(3,3) == 6

def test_calculator_history_count(clear_history):
    assert Calculator.count_history() ==0

def test_calculator_clear_history():
    assert Calculator.clear_history()==0

def test_calc_complete(clear_history):
    #The calculator is holding static properties and mothods i.e. history property there is only one history property
    #Additn Calculation Objects to the history
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 3) == 6
    assert Calculator.count_history() == 3
    #the numbers in [0] refers to the calculation object in that position and you can call the method on the object
    assert Calculator.history[0].getResult() == 3
    assert Calculator.history[1].getResult() == 4
    assert Calculator.history[2].getResult() == 6

def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1
    assert Calculator.subtract_number(1, 3) == -2
    assert Calculator.subtract_number(1, 4) == -3
    assert Calculator.count_history() == 3


def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1,2) == 2
    assert Calculator.multiply_numbers(2,2) == 4
    assert Calculator.multiply_numbers(3,2) == 6
    assert Calculator.multiply_numbers(4,2) == 8
    assert Calculator.count_history()  == 4
    assert Calculator.clear_history() == 0
