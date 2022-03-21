import subprocess

exit_code = subprocess.call(["date", "+%H:%M:%S"])
print(exit_code)

date = subprocess.check_output(["date", "+%H:%M:%S"])
print(date)


