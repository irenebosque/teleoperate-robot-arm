# 🎮 Teleoperate simulated robot arm with a joystick
How to teleoperate a robot arm with a joystick using meta-world benchmark and MuJoco
For your machine learning projects

# Table of Contents
1. [Example](#example)
2. [Example2](#example2)
3. [Third Example](#third-example)
4. [Fourth Example](#fourth-examplehttpwwwfourthexamplecom)

# example
# Create a virtual environment for the project (optional)
```Shell
# Install virtualenv
sudo apt-get install python-virtualenv

# Create a virtual environment called metaworld and that uses python3.5
virtualenv --python=/usr/bin/python3.5 ~/metaworld

# Enter in the virual environment just created
source ~/metaworld/bin/activate


# Inside the virtual environment

# Check first python version
python

# Install tensor flow
pip install tensorflow==1.4.0
```

# Get a MuJOco license
This tutorial uses the <a href="https://meta-world.github.io/">meta-world</a> benchmark which is based in MuJoco
You can get a 30 days free <a href="https://www.roboti.us/license.html">MuJoco license</a> here. If you are a student, the license it is free. Note: It took me 1 week until they send me my student license.







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
    <a href="https://github.com/openai/mujoco-py">
      <img src="https://github-readme-stats.vercel.app/api/pin/?username=openai&repo=mujoco-py&show_owner=True" alt="GitHub Stats" />
    </a>
  </p>
</div>
