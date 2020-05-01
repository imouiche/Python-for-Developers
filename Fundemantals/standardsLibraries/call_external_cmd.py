
import subprocess


result = subprocess.run(["ls", "-l"])
print(type(result))
