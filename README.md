# shopify-streamlit-dashboard
Example Shopify Streamlit Dashboard

## Heroku Setup
```sh
heroku create shoplit-dash
heroku git:remote -a shoplit-dash
git push heroku main
# or push another branch up:
git push heroku new_branch:main
# for deploying the dynos initially
heroku ps:scale web=1
```