[![Build Status](https://travis-ci.org/mwinel/stackoverflow-lite.svg?branch=stackoverflow-lite-travis-ci)](https://travis-ci.org/mwinel/stackoverflow-lite)

# stackoverflow-lite
StackOverflow-lite is a platform where people can ask questions and provide answers.

## Installation and Set Up

Clone the repo from GitHub:

```
https://github.com/mwinel/stackoverflow-lite.git
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

## Testing

Test the resources in postman to see how they work.

## UI
[Check out the project user interface](https://mwinel.github.io/stackoverflow-lite/UI/index.html)

The UI has the following necessary pages as specified below.

- [user signup](https://mwinel.github.io/stackoverflow-lite/UI/signup.html), enables user to create an account.
- [user login](https://mwinel.github.io/stackoverflow-lite/UI/login.html), enables user to login into the app.
- [index page](https://mwinel.github.io/stackoverflow-lite/UI/index.html), enables user to view recently asked questions and to search for questions and answers.
- [question page](https://mwinel.github.io/stackoverflow-lite/UI/question.html), enables user to view a question with all its answers posted for it and add an answer.
- [ask page](https://mwinel.github.io/stackoverflow-lite/UI/ask.html), enables user to post a question.
- [user profile page](https://mwinel.github.io/stackoverflow-lite/UI/user_profile.html), shows the users number of questions asked, number of anwers given by the user, a list of questions asked by the user with the most answers and the list of recently asked questions by the user.
- [search results page](https://mwinel.github.io/stackoverflow-lite/UI/search_results.html), enable users to view their search results.
