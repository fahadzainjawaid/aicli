#run bedrockcli inline "Hello, world!" command

import os
import sys

import subprocess


subprocess.run([
    sys.executable, "-m", "bedrockcli", "inline", "Hello, world!"
], check=True)
