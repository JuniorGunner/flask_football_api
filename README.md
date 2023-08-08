# Football Data API Project :soccer:

This is a project to create a REST API that interacts with the Football-data.org API, imports the data locally to a database and expose endpoints for getting the data. 

## Tech Stack :computer:

The project uses the following technologies:

- **Python 3.9** - A versatile language with a wide range of uses, from scripting to web development.
- **Flask** - A lightweight web framework for Python.
- **SQLAlchemy** - A SQL toolkit and ORM for Python.
- **Docker** - A platform to develop, ship, and run applications within containers.

## Tech Stack 🛠️

-  🐍 **Python** was chosen for its simplicity and readability, making the code easy to write and maintain.
- 🌶️ **Flask** is a simple and lightweight framework which is great for small to medium applications.
- 🗄️ **SQLAlchemy** is a powerful ORM that provides high-level and pythonic interface to SQL databases, providing a lot of flexibility and reducing the need to write raw SQL.
- 🐳 **Docker** makes it easier to create, deploy, and run applications by using containers, which allows a developer to package up an application with all the parts it needs, such as libraries and other dependencies, and ship it all out as one package.

## Getting Started :rocket:

You can run the project locally with Docker and Docker Compose:

```bash
docker-compose up
```

This will build the Docker image and start the server at http://localhost:5000.

API Endpoints :link:

/import-league/<leagueCode>
/players/<leagueCode>
/team/<teamName>
/players-of-team/<teamName>

License :page_with_curl:
This project is licensed under the MIT License.
