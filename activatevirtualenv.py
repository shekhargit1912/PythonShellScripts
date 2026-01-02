import os 
import subprocess


#crete virtual env 
subprocess.run(["python3", "-m", "venv", "myenv"])

#activate virtual env
os.system("source myenv/bin/activate")
