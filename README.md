# Product information and shopping cart management system

This is a Web application based on the Django framework that displays product information, manages the user's shopping cart, and allows users to simulate purchases.

## Start

The following guide will help you get the project up and running in a local environment for development and testing.

## Prerequisites

Before you start, you need to install the following software:

- Python 3.10
- Django 4.1.2
- For other dependencies, refer to the requirements.txt file

###You can install the required Python package with the following command:

        pip install -r requirements.txt

        git clone https://github.com/chuanwangLuo/solo_assessment.git

        cd solo Assessment


## First, create the basics
Create a new project folder called 'temperature_stories' and then cd into the folder via the terminal and execute these commands:

        pyenv local 3.10.7 # this sets the local version of python to 3.10.7
        python3 -m venv .venv # this creates the virtual environment for you
        source .venv/bin/activate # this activates the virtual environment
        pip install --upgrade pip [ this is optional]  # this installs pip, and upgrades it if required.

We will use Django (https://www.djangoproject.com) as our web framework for the application. We install that with 
        
        pip install Django==4.1.2
    
And that will install django version 4.1.2 (or pick a different version if there's something newer) with its associated dependencies. We can now start to build the application.

## Start the Server
We can now use the manage.py command tool to start the development server by entering this command in the terminal:

        python3 manage.py runserver

If you're doing this on another platform, then you might need to use this instead (change the port number from 8000 as required):

        python3 manage.py runserver 0.0.0.0:8001

## Run the test
Run the automated tests with the following command:

        python manage.py test

## Deployment

the website is :

        t04cl23.pythonanywhere.com

## The technology used

* [Django] (https://www.djangoproject.com/) - Web framework
* [Pandas] (https://pandas.pydata.org/) - data analysis
* [Numpy](https://numpy.org/) - numerical calculation tool
