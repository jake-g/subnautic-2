import subprocess
import os

os.chdir("/Users/jakegarrison/Downloads/projects/subnautica-2")
subprocess.run(["git", "add", "-A"])
subprocess.run(["git", "commit", "-m", "style: fix mypy and pylint linting feedback and format test suite"])

# Push to both remotes
subprocess.run(["git", "push", "origin", "main"])
subprocess.run(["git", "push", "personal", "main"])
