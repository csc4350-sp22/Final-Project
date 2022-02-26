# Project Milestone 2 README.md

1. Explains how someone who clones the repository can set up and run your project locally (what to install, any extra files to add)

2. Detailed description of how implementing your project differed from your expectations during project planning.

3. Detailed description of technical issues and how you solved it (your process, what you searched, what resources you used)

# Heroku Movie Url

1. https://pure-wildwood-21546.herokuapp.com/

# Deploying to Heroku

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
```

# Detail description of technical issues

1.  When I created my comment section for my main page, it kept printing duplicate posts everytime I ran it. To solve it I added a print statement for each of the variables: rating, comment, movie, and username, and with that I was able to fix that problem.
2.  Another probem I faced was when I made the Comment database, I was unable to call on the username from within class to make it print alongside with the comments. But to solve this, I made a user session inside my login route to track the user when they login and initialize the variable within my app.route to print it correctly.

# Experience working on Milestone 2

1. From this Milestone compared to the last, this was severely more difficult for me because it involved a lot of databases. I had the most difficulty figuring out how to call on the database and the right values to display on my html. I was able to get the flask login/signup function pretty easily but everything else was pretty much difficult to setup.
