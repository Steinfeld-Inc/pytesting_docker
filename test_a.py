# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    f = open("/tmp/test_on_server.txt", "w")
    f.write("HO\n")
    assert inc(20) == 21
