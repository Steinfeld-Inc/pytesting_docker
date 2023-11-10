import subprocess

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    with open("/tmp/test_on_server.txt", "w") as f:
        f.write(str(subprocess.run("python --version", shell=True)))
        f.write(str(subprocess.run("pwd", shell=True)))
        f.write(str(subprocess.run("pip freeze", shell=True)))
    assert inc(20) == 21
