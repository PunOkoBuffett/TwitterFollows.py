To use this script you need the following installed or set up:

Python 3

Python Requests Library

Access to the twitter API  library


To set up Python3 on your local machine you can follow this [guide]
(https://docs.python.org/3/using/index.html)

One that is installed you may need to install [PIP 3](https://docs.python.org/3/installing/index.html)

From a command line you can type pip --version to see if this is needed

After both of these are download and installed you will have to install the requests library through pip
`python -m pip install requests`

Next you will need to get access to the Twitter API. You can fill in some basic information [here]
(https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api)

Follow the steps for a standard user. Write down the following when prompted -

API Key
API Secret key
Bearer Token

You must treat these credentials as "secrets" such as passwords and such as anyone who 
has access to these values can access the Twitter API with your credentials

With all of these set up you are ready to run this project.

If you want to run the script through an IDE and don't want to 
deal with the export line in Influencer.py change this line
```
def auth():
    return os.environ.get("BEARER_TOKEN")
```

to
```
def auth():
    return "Bearer token string"
```

Please note this is a very unsafe practice as you could be leaking
the bearer token if you commit the code in any places. It is okay 
fine for local runs however. You can just uncomment the line and put
your bearer token there to not have to worry about it in the future.

Finally you can either use the Github CLI or download this repository locally
to get the python file onto your machine. The Download button is there if you click the CODE
button.

I would also suggest working through an IDE such as
[PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/#section=windows)