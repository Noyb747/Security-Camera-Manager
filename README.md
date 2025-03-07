# Security Camera Manager

A simple camera display program build in python.

# Install
* Windows: Run :
  ```sh
  git clone https://github.com/Noyb747/Security-Camera-Manager.git
  ```
  to install the program and if you're using the python file and not the precompiled version run:
  ```sh
  pip install -r "./Security-Camera-Manager/bin/requirements.txt"
  ```

# Usage
On Windows: ```scmanager <cameras>```
* ```scmanager 0,1``` selects camera ```0``` and ```1```
* ```scmanager 1-4``` selects all cameras from ```1``` to ```4``` (including)
* ```scmanager 0-2,4-7``` selects all cameras from ```0``` to ```2``` and from ```4``` to ```7```
