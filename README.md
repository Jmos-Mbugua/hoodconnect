# Hoodconnect


## Description
Hoodconnect allows users to join a neghbourhood, advertise businesses, create posts and views other users' posts. 


## Author


* [**John Mbugua**](https://github.com/Jmos-Mbugua)

## Features


As a user of the application you will be able to:

1. See all posts from other neighbours
2. See neighbourhood's businesses, contacts, and posts.
3. Submit posts
4. Create profile and edit profile
5. Search for a business by name

## Specifications
| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| Login to admin  | **username**: jmos , **password** : jmosmbugua | view and make changes to the admin | 
Signup to the application | Click on `Signup` | A sign up page appears with a sign up form |
|  Login to the site | Click on `Log in`  | Redirected to the login page with a login form |
|  Search in the search field | Input keywords to be searched then click SEARCH | Search page is loaded and displays with the searched results |
|Submit a post|click on `Upload Post`| An upload page appears with an upload form containing different fields|
|View profile|click `account` link in the navbar|Redirects to profile page with an option to edit profile|
|View businesses|click `businesses`|businesses page with the businesses in the neighbourhood|


## Getting started
### Prerequisites
* python3.6
* virtual environment
* pipenv
* django 2.2.7

## admin credentials
USERNAME: jmos
PASSWORD: jmosmbugua

### Cloning
* In your terminal:
        
        $ git clone https://hoodconnect.herokuapp.com/
        $ cd Hoodconnect

## Running the Application
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ pipenv shell`
* Download pip in our environment using `$ pip3 install pipenv`
* Install all the dependencies from the requirements.txt file by running `python3.6 pipenv install -r requirements.txt`
* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations -app-name-
        $ python3.6 manage.py migrate -app-name-

* To run the application, in your terminal:

        $ python3.6 manage.py runserver
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 manage.py test 
        
## Known Bugs
 * The rate functionality is not fully working. The process of making it work is ongoing.
## Technologies Used
* Python3.6
* Django 2.2.7
* HTML
* Bootstrap

This application is developed using [Python3.6](https://www.python.org/doc/), [Django](https://www.djangoproject.com/), [HTML](https://getbootstrap.com/) and [Bootstrap](https://getbootstrap.com/)


## Support and Team
John Mbugua


### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
