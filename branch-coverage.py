import subprocess

subprocess.run(["coverage", "run", "--branch", "-m", "pytest", "tests"])
subprocess.run(["coverage", "report"])