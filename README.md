# shopify-streamlit-dashboard
Example Streamlit Dashboard for a Shopify App.

See the rest of the Shopify App here: https://github.com/parker84/shopify-streamlit-example

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
