from mock import patch
from service import Service


@patch('service.Service.bad_random')
def test_bad_random(bad_random):
    service = Service()
    
    bad_random.return_value = 10
    assert service.bad_random() == 10

@patch('service.Service.bad_random')
def test_divide(bad_random):
    service = Service() 
    assert service.divide(1) == 10
    
    try:
        service.divide(0)
    except ZeroDivisionError:
        assert True
        
def test_abs_plus():
    service = Service()
    
    assert service.abs_plus(2) == 3
    assert service.abs_plus(0) == 1
    assert service.abs_plus(-2) == 3
    
@patch('service.Service.bad_random')
def test_complicated_function(divide, bad_random):
    service = Service()
    
    assert service.complicated_function(15) == (9, 3)
    
    try:
        service.complicated_function(0)
    except ZeroDivisionError:
        assert True
    assert service.complicated_function(-15) == (-9, 3)
