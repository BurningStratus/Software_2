import sys, subprocess
import os
from subprocess import Popen, PIPE

exe_str = "C:/Windows/System32/cmd"
another_string = "ping google.com"


print(os.system(another_string))