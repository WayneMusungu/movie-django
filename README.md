# Wayne Movie

#### By Wayne Musungu 

## Table of Content

- [Description](#Description)
- [Installation Requirement](#Installation)
- [Technologies Used](#Technologies-Used)
- [License](#LICENSE)

## Description 

This is a movie website that users can get to search for Movies and Tv Shows, view their detailed information and get recommendation of various Movies and Tv Shows.

##### Link to Live Site

(https://waynemovie.herokuapp.com/)
 
#### Website Demo
![LANDING PAGE](Home.gif)


#### Technologies used
    - Python 3.8
    - TMBD API
    - HTML
    - Bootstrap 5
    - Heroku


# Installation

### Requirements


Go to [The Movie Database] (https://www.themoviedb.org/) and sign up for an acount 

1. Go to your accounts settings page
2. Click on the API menu 
3. Click on create an API Key to generate a new API KEY





#### Install dependancies
First create `.env` file inside this file you need to store your API Key. Below is how the `.env` file should look like:
`MOVIE_API_KEY="your_tmdb_api_key"`
`SECRET_KEY='django_secret_key'`

Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`


#### Run the app
```bash
python manage.py runserver
```

# License

Copyright (c) 2022 WayneMusungu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
