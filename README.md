# Project Milestone 3 README.md

1. Installation instructions are up to date

2. Three technical problems are described in detail

3. Hardest part and most valuable learning of overall project is described

# Installation

1. On https://github.com/new, create a new repository
2. In your terminal, in your home directory, clone the repo: `git clone git@github.com:csc4350-sp22/project1-bduong2.git`
3. `cd` into the repository that is created
4. Then, connect this cloned repo to your new personal repo made in Step 1: `git remote set-url origin https://www.github.com/{your-username}/lect7.git` (be sure to change your username and remove the curly braces)
5. Run `git push origin main` to push the local repo to remote.
6. Create a .env file in your main directory
7. Create an account on https://www.themoviedb.org/
8. Add your TMDB key to your .env file
9. Go to https://dashboard.heroku.com/apps and click your App, then go to Settings, and click "Reveal Config Vars"
10. Add your secret key from .env with the matching variable name (TMDB_KEY) and value (your key, without quotation marks!)
11. Log in to Heroku: `heroku login -i`
12. Create a Heroku app: `heroku create`. This will create a new URL and associated host for you
13. run `heroku addons:create heroku-postgresql:hobby-dev -a app name`
14. run `heroku config -a app name` to get your Heroku DATABASE URL and then add that to your .env file (make sure you change it to postgresql)
15. Push your code to Heroku: `git push heroku main`. This will push your code to Heroku's remote repository
16. Run `heroku open` or refresh the URL if you have it open.

# Installation Project 3

1. Get started with Milestone 2 solution
2. Clone down the repo then come with hw7 files
3. Copy over your package.json, package-lock.json, src/, and public/ folders.
4. Take the blueprint (bp) from the starter code’s app.py, and place all the non-import logic in your routes.py before the actual `app.run()` call.
5. Add a link on your main page that directs to your new route so you can reach the new page you’re adding. Now that page should render your App.js’s contents.
6. Create a .env file in the top-level directory and enter the following as its contents: `export TMDB_API_KEY="<YOUR API KEY>"` and `export DATABASE_URL="<YOUR POSTGRESQL DB URL>"`
7. To get started run `npm build in` your project folder directory
8. To run the app, run `python3 app.py`

# Install Requirements

```python
pip install python-dotenv
pip install requests
pip install flask
sudo curl https://cli-assets.heroku.com/install.sh | sh # install Heroku
brew install postgresql
brew services start postgresql
pip3 install psycopg2-binary
pip3 install Flask-SQLAlchemy==2.1
pip install black
pip install -r requirements.txt
```

# Three technical problems

1.  One problem I faced when working on this project was the first step of making the api call onto the react server. I had trouble getting the neccessary information from the database "Rating" to render on the web page. To print the current reviews for the login user, I had to query the Rating db and filter by the current user that is logged in. Then i made an empty list and set up a for loop where i could append each element in the array into the list and return the data with Jsonify.

2.  Another problem I faced when working on Milestone 3 involved mainly the App.js file. I was able to print all the neccessary user information on the react web page but the issue was it was printing all of the comments, ratings, and user id's together instead of separately line by line. To fix this, in my return function, I used the map function to map each of the reviews by their index and display them each on different lines.

3.  The third problem I had was none of my buttons were able to fuction correctly. I was able to see changes onClick but when I refresh the page, the data doesnt completely change or render. To solve this, I made 3 extra app.routes for my Edit button, Delete button, and Save button and directly called on them in my App.js file by setting up multiple functions for each one of them.

# Hardest part and most valuable learning of overall project

1. The hardest part of this project was definitely learning about all the components involved in the App.js files work, and how the flask app backend connects hand in hand with the react server frontend. I certainly had a lot of trouble just trying to get my buttons to render, as that was the most fustrating part of this milestone, next to making the right api call in order for the correct user information to be rendered onto the web server.
