# shopify-streamlit-dashboard
Example Shopify Streamlit Dashboard

## Setup

### Step 1: Setup this App
```sh
heroku create shoplit-dash
heroku git:remote -a shoplit-dash
git push heroku main
# or push another branch up:
git push heroku new_branch:main
# for deploying the dynos initially
heroku ps:scale web=1
```

### Step 2: Connect to the DB
The db that you made in step 4 here.

Set your db parameters as environmental variables in heroku
```sh
heroku config:set DB_HOST=db_host
heroku config:set DB=db_name
heroku config:set DB_USER=db_user_name
heroku config:set DB_PWD=db_password
# port is assumed to be 5432
```

If these are set we will try and grab the first 20 rows and show them.