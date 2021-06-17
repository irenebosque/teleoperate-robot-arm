# 🎮 Teleoperate simulated robot arm with a joystick
How to teleoperate a robot arm with a joystick using meta-world benchmark and MuJoco
For your machine learning projects

# Get a MuJOco license
This tutorial uses the metaworld benchmark which is based in MuJoco
You can get a 30 days free MuJoco license here. If you are a student, the license it is free. Note: It took me 1 week until they send me my student license.

# Create a virtual environment for the project (optional)
```Shell
# Install virtualenv
sudo apt-get install python-virtualenv

# Create a virtual environment called tf14 and that uses python3.5
virtualenv --python=/usr/bin/python3.5 ~/tf14

# Enter in the virual environment just created
source ~/tf14/bin/activate


# Inside the virtual environment

# Check first python version
python

# Install tensor flow
pip install tensorflow==1.4.0
```

# How to run it
1. 🎮🕹️ Connect your joystick to the computer
2. Open a new terminal, go to the root directory of the project and do:

```
python main.py
```


Check out the GitHub repository:

<div>
  <p>
    <a href="https://github.com/rlworkgroup/metaworld">
      <img src="https://github-readme-stats.vercel.app/api/pin/?username=rlworkgroup&repo=metaworld&show_owner=True" alt="GitHub Stats" />
    </a>
  </p>
</div>
