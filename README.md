[![Build Status](https://travis-ci.org/mwinel/stackoverflow-lite.svg?branch=stackoverflow-lite-travis-ci)](https://travis-ci.org/mwinel/stackoverflow-lite)  [![Coverage Status](https://coveralls.io/repos/github/mwinel/stackoverflow-lite/badge.svg?branch=master)](https://coveralls.io/github/mwinel/stackoverflow-lite?branch=master)  [![Maintainability](https://api.codeclimate.com/v1/badges/1eb372f598d4bfd45f3f/maintainability)](https://codeclimate.com/github/mwinel/stackoverflow-lite/maintainability)

# stackoverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

### Installation and Set Up

Clone the repo from GitHub:

```
git clone https://github.com/mwinel/stackoverflow-lite.git
cd stackoverflow-lite
```

Create and activate virtualenv

```
python -m venv venv
venv/Scripts/activate
```

Install necessary requirements

```
pip install -r requirements
```

Run the app and access the application at the address **http://localhost:5000/**

```
python manage.py runserver
```

Run unit tests

```
python manage.py tests
```

### Testing

Test the resources in postman to see how they work.

### API Endpoints

| Resource URL | Methods | Description | Requires Token |
| -------- | ------------- | --------- |--------------- |
| `/api/v1/` | `GET`  | The index | `FALSE` |
| `/api/v1/index` | `GET`  | The index | `FALSE` |
| `/api/v1/questions` | `GET, POST` | Add & Fetch questions | `FALSE` |
| `/api/v1/questions/<questionId>` | `GET, PUT, DELETE` | Manipulate a single question | `FALSE` |
| `/api/v1/questions/<questionId>/answers` | `POST` | Add answer | `FALSE` |

### Sample Requests

Index;
```

http GET http://localhost:5000/api/v1/index

HTTP/1.0 200 OK
Content-Length: 85
Content-Type: application/json
Date: Sun, 19 August 2018 11:06:36 GMT
Server: Werkzeug/0.14.1 Python/3.6.5

{
    "message": "Welcome to StackOverflow-Lite"
}

```

### UI
[Check out the project user interface](https://mwinel.github.io/stackoverflow-lite/UI/index.html)

The UI has the following necessary pages as specified below.

- [user signup](https://mwinel.github.io/stackoverflow-lite/UI/signup.html), enables user to create an account.
- [user login](https://mwinel.github.io/stackoverflow-lite/UI/login.html), enables user to login into the app.
- [index page](https://mwinel.github.io/stackoverflow-lite/UI/index.html), enables user to view recently asked questions and to search for questions and answers.
- [question page](https://mwinel.github.io/stackoverflow-lite/UI/question.html), enables user to view a question with all its answers posted for it and add an answer.
- [ask page](https://mwinel.github.io/stackoverflow-lite/UI/ask.html), enables user to post a question.
- [user profile page](https://mwinel.github.io/stackoverflow-lite/UI/user_profile.html), shows the users number of questions asked, number of anwers given by the user, a list of questions asked by the user with the most answers and the list of recently asked questions by the user.
- [search results page](https://mwinel.github.io/stackoverflow-lite/UI/search_results.html), enable users to view their search results.
