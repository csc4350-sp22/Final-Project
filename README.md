# Project Milestone 1 README.md

1. Explains how someone who clones the repository can set up and run your project locally (what to install, any extra files to add)

2. Detailed description of known problems and how you would address them if you had more time. If none exist, what additional features might you implement, and how?

3. Detailed description of technical issues and how you solved it (your process, what you searched, what resources you used)

# Heroku Movie Url
1. https://nameless-atoll-12538.herokuapp.com/

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
13. Push your code to Heroku: `git push heroku main`. This will push your code to Heroku's remote repository
14. Run `heroku open` or refresh the URL if you have it open.



# Install Requirements

```python
pip install python-dotenv
pip install requests
pip install flask
sudo curl https://cli-assets.heroku.com/install.sh | sh # install Heroku
```

# Detail description of technical issues
1.   I was getting a keyerror 'pageid' on the webpage when I was running my app.py in my local terminal. It was working on every other refresh and I wasn't too sure why. But, I figured out that one of the ID's was giving me the error everytime I refreshed onto it, so I eventually swapped it out with another movie ID and now it works perfectly.
2.  The second error I had showed up when i ran Pylint on my computer. I was getting a Missing module docstring pylint(missing-moule-docstring) [1,1] in my lines with import requests and import os. To solve this, I just added #pylint: disable = missing-module-docstring to the very top of the code that solved some of the Pylint errors I was recieving. 

# Detail descirption of known prolems
1. At this moment, I'm able to run my code and display it on Heroku without any issues. If i were to have more time, I would customize my webpage more to make it look more aestetically pleasing. 
2. Another thing I would add if i had more time would be a User input functionality as shown in the extra credits. Where users are able to have the ability to choose an actor among some options and then see a randomly chosen movie from that selected actor.