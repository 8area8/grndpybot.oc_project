# The GrandPy bot project

![version](https://img.shields.io/badge/version-1.1.2-blue.svg?longCache=true&style=flat-square) ![version](https://img.shields.io/badge/python-3.6-ligh.svg?longCache=true&style=flat-square) ![version](https://img.shields.io/badge/project-web_app-orange.svg?longCache=true&style=flat-square)

## News

- 09/18/2018 : release **1.1.2**. Refactoring and css minification.
- 09/14/2018 : New release **1.1.1**, bug fixe on *title_from()* method.
- 09/15/2018 : The second release, **1.1** is done ! Look at the release description for more details.
- 09/13/2018 : release **1.0** done ! Application deployed.

## Presentation

![grandpybot example](https://image.ibb.co/eTu0Ge/grandpybot_example.jpg)

This project is a web application that allows you to chat with a robot. This robot attempts to return the address or location given in the user message, as well as an anecdote of the surroundings.

## Specificities

- A question / answer system in the form of a chat box
- an interactive Google map  in the answer
- an anecdote randomly drawn from the neighborhood of the place, taken from wikipedia
- a page "about"

## Getting Started

You can clone this repository to your local drive and then deploy it to heroku.

### Prerequisites

to use it, you'll need to install:

- python 3.6
- pipenv

### Installing

Run pipenv at the root of the repository to install dependencies.

>**NOTE:** The Javascript file ans CSS file are minified. I used a webpack environnment for frontend developement, and it is not given with this repository. You should recreate your own .js and .css files if you want to modify them.

## Running the tests

I use Pytest for tests. Simply write ```pipenv run python -m pytest``` in your shell, at the root of this repository.

## Deployment

Use heroku for deployment.  
You have to create a heroku account and set this project to a new heroku project. Then simply write ```git push heroku master``` to deploy your application.  
>**NOTE:** You'll have to set your own google key API. Set a heroku variable called ```"GOOGLE_KEY"``` for that.

## Built With

### Core dev

- python - back language.  
- npm, webpack - Front-end developement.  
- material design lite - css/js framework.  
- Jquery - Javascript framework.  
- flask - python web framework.  
- pytest - test framework.

### Third API

- Google (Place, Map JS)
- MediaWiki (Geocoding, rest_V1)

## Trello Scrum project

**Link to Trello:**
[![link to Trello](https://image.ibb.co/mvESX9/trello.jpg)](https://trello.com/b/SMatrUZV/scrum-board)

## Authors

Mikael Briolet - Initial work - OpenClassroom

Photo by Tim Mossholder on Unsplash

## License

There is actually no license for this project.
