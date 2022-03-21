import subprocess

res = subprocess.call(["date", "+%H:%M:%S"])
print(res)

output = subprocess.check_output(["cal"])
print(output)
