# Jungle Devs - Django Challenge #001

## Description

**Challenge goal**: The purpose of this challenge is to give an overall understanding of a backend application. You’ll be implementing a simplified version of a news provider API. The concepts that you’re going to apply are:

- REST architecture;
- Authentication and permissions;
- Data modeling and migrations;
- PostgreSQL database;
- Query optimization;
- Serialization;
- Production builds (using Docker).

**Target level**: This is an all around challenge that cover both juniors and experience devs based on the depth of how the concepts were applied.

**Final accomplishment**: By the end of this challenge you’ll have a production ready API.

## Acceptance criteria

- Clear instructions on how to run the application in development mode
- Clear instructions on how to run the application in a Docker container for production
- A good API documentation or collection
- Login API: `/api/login/`
- Sign-up API: `/api/sign-up/`
- Administrator restricted APIs:
  - CRUD `/api/admin/authors/`
  - CRUD `/api/admin/articles/`
- List article endpoint `/api/articles/?category=:slug` with the following response:
```json
[
  {
    "id": "39df53da-542a-3518-9c19-3568e21644fe",
    "author": {
      "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
      "name": "Author Name",
      "picture": "https://picture.url"
    },
    "category": "Category",
    "title": "Article title",
    "summary": "This is a summary of the article"
  },
  ...
]
```
- Article detail endpoint `/api/articles/:id/` with different responses for anonymous and logged users:

    **Anonymous**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>"
    }
    ```

    **Logged user**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>",
      "body": "<div><p>Second paragraph</p><p>Third paragraph</p></div>"
    }
    ```

## Instructions - Development

1. First clone the repository using:
```git clone https://github.com/btmluiz/django-challenge-001```
2. Create your virtual environment.
3. Install the requirements: ```pip install -r build/development/django/requirements.txt```
4. Run docker-compose: ```docker-compose -f "build/development/docker-compose.yml" up -d```
5. The application will be served in [http://localhost:8000/api/](http://localhost:8000/api)

You can use Postman to send the requests to application using the postman collection 
````Django-Challenger.postman_collection.json```` and postman environment ```Django-challenger.postman_environment.json```
attached in root project directory (just remember to change the port in postman environment to 8000 if in development or
to 8080 if in production)

## Instructions - Production
1. First clone the repository using:
```git clone https://github.com/btmluiz/django-challenge-001```
2. Run docker-compose: ```docker-compose -f "build/production/docker-compose.yml" up -d```
3. The application will be served in [http://localhost:8080/api/](http://localhost:8000/api)

You can use Postman to send the requests to application using the postman collection 
````Django-Challenger.postman_collection.json```` and postman environment ```Django-challenger.postman_environment.json```
attached in root project directory (just remember to change the port in postman environment to 8000 if in development or
to 8080 if in production)