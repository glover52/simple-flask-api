# Project Information
This project implements a simple online cache to store documents of the form:
```
{
    “id”: int,
    “message”: string
}
```
### Storing the document
Documents are able to be stored in the cache by sending a `POST` request to the `/messages` endpoint. Documents stored in the cache have a default Time To Live (TTL) of thirty seconds. After this time has elapsed, the document is deleted from the cache and any attempts to retrieve it fail.

Messages that are malformed are rejected before they can be sent to the cache and optionally adding a `ttl` to the request body allows the TTL to be adjusted from its default setting.

### Retrieving the document
Sending a `GET` request to `/messages/<id>` where `<id>` is a valid document id returns the requested document to the user. Subsequently sending a `GET` request to the `/messages` endpoint returns a json structured list of all existing messages.

### Clearing the cache
Sending an empty `POST` request to the `/clearcache` endpoint flushes all existing data from the cache.

### Deploying to [Heroku][heroku]
Heroku Domain: [enigmatic-hollows-71380][heroku-project]
1. Install Heroku CLI and login using personal credentials
2. Clone the repository
`git clone https://github.com/glover52/simple-flask-api.git`
3. Create a virtualenv for Python3.6 and install the dependencies by running
`pip install -r requirements.txt`
4. Create a new Heroku project and call it whatever you want.
(Note: Leave blank for a generated name)
`heroku create <new-heroku-project>`
10. Install Heroku [MemCachier][heroku-memcachier] addon
`heroku addons:create memcachier:dev`
11. Use the terminal to deploy via git
`git push heroku master`


# Reference Material
Listed below is a complete list of all the reference material used in creating this project and any extra material that may be useful should you need any assistance. It includes official documentation as well as references from third party websites and articles. Read it carefully and adopt appropriately to similar projects!

### Heroku Python Tutorials
- [Official Documentation][heroku-python-getting-started]
- [Memcachier][heroku-memcachier-tutorial]

### Flask Tutorials/Documentation
- [Quick-start Guide][flask-quickstart]
- [Restful API Tutorial][flask-restful-api-tutorial] (Credit: Miguel Grinberg)
- [In-depth Restful API Tutorial][flask-mega-restful-api-tutorial] (Credit: Miguel Grinberg)
- [Deploying a Flask App][medium-deploying-a-python-flask-app] (Credit: John Kagga)

[flask-quickstart]: http://flask.pocoo.org/docs/1.0/quickstart/#a-minimal-application
[flask-restful-api-tutorial]: https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
[flask-mega-restful-api-tutorial]: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
[heroku]: https://heroku.com
[heroku-memcachier]: https://elements.heroku.com/addons/memcachier
[heroku-memcachier-tutorial]: https://devcenter.heroku.com/articles/memcachier
[heroku-project]: https://enigmatic-hollows-71380.herokuapp.com
[heroku-python-getting-started]: https://devcenter.heroku.com/articles/getting-started-with-python
[medium-deploying-a-python-flask-app]: https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0
