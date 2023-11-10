# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    f = open("myfile.txt", "w")
    f.write("HOHOHO\n")
    assert inc(20) == 21
