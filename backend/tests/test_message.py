from src.message import Message

def test_update_message():
    msg = Message()
    msg.update_message("test")
    assert msg.message == "test"

def test_remove_spec_char():
    msg = Message("this * is _ a - test")
    msg.remove_spec_char()
    assert msg.message == "thisisatest"

def test_format_text_to_number():
    msg = Message("test")
    msg.format_text_to_number()
    assert msg.message == [20, 5, 19, 20]

def test_format_number_to_text():
    msg = Message([20, 5, 19, 20])
    msg.format_number_to_text()
    assert msg.message == ['T', 'E', 'S', 'T']

def test_obtain_cypher_text():
    msg = Message([2, 4, 6, 20])
    msg.obtain_cypher_text([3, 2, 20, 8])
    assert msg.message == [5, 6, 26, 2]