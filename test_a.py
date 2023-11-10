import subprocess

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    with open("/tmp/test_on_server.txt", "w") as f:
        version = subprocess.run(['python --version'], encoding='utf-8', stdout=subprocess.PIPE)
        for line in version.stdout.split('\n'):
            f.write(line)
        f.write(str(subprocess.run("pwd", shell=True)))
        f.write(str(subprocess.run("pip freeze", shell=True)))
    assert inc(20) == 21
