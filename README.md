
# Person API

The Person API is a simple RESTful API that allows you to perform CRUD (Create, Read, Update, Delete) operations on person records. This README provides instructions on setting up, running, and using the API.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
  - [Create a Person](#create-a-person)
  - [Retrieve a Person](#retrieve-a-person)
  - [Update a Person](#update-a-person)
  - [Delete a Person](#delete-a-person)
- [Testing the API](#testing-the-api)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.6+
- pip (Python package manager)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.x/)
- MySQL (or an alternative database, based on your choice)

## Getting Started

### Installation

1. Clone this repository to your local machine:
git clone https://github.com/yourusername/person-api.git ------- Navigate to the project directory:


cd person-api ------- Install the required Python packages:
pip install -r requirements.txt


Running the API
Ensure your database is set up and running.

Run the following command to create the database tables:


python create_db.py ------ Start the API server:


python app.py -------- The API should now be running locally at http://localhost:5000.

API Endpoints