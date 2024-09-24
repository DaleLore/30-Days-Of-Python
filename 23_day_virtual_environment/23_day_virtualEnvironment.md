<!-- Day 23: 30 Days of python programming -->

# Exercises - Day 23

# Notes - Virtual Environments
- A virtual environment in Python is an isolated environment that allows you to manage dependencies for different projects separately, without interfering with each other
    - This is especially useful when different projects require different versions of the same package thus avoiding conflicts

- If we use virtualenv, we will access only oackages which are specific to that project

```
# Install the virtualenv package
pip install virtualenv

# To create a virtual environment / Confirm the virtual environment with ls

virtualenv venv

# Activate the virtual environment
source venv/bin/activate

## The virtual environment now will start with (venv)

#  Install packages in this project by writing pip freeze; for this project we'll install a flask package to the project
pip install Flask

# Now freeze!
pip freeze

# Deactivate from the environment
deactivate

## The necessary modules to work with flask are installed. Now your project directory is ready for a flask project. You should include the venv to your .gitignore file not to push it to github
```