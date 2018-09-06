from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    #test 404 with /
    resp = app.request("/")
    assert_response(resp,status="404")

    #test GET request
    resp = app.request("/hello")
    assert_response(resp)

    #make sure default work for form
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="Nobody")

    #test with expected values
    data = {'name':'Arjun','greet':'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Arjun")
