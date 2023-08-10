# Football Data API Project :soccer:

This project is designed to create a REST API that interacts with the Football-data.org API, imports the data locally to a MongoDB database, and exposes endpoints for fetching the said data. 

## Tech Stack 🛠️

- 🐍 **Python** - Chosen for its simplicity and readability, making the code easy to write and maintain.
- 🌶️ **Flask** - A lightweight and versatile micro web framework suitable for small to medium applications.
- 🍃 **MongoDB** - A popular NoSQL database, known for its scalability and flexibility when dealing with large amounts of data and complex software applications.
- 🐳 **Docker** - Simplifies the process of creating, deploying, and running applications using containers. It enables developers to package an application and its dependencies into a single container.

## Getting Started :rocket:

### Prerequisites:
- Ensure that Docker and Docker Compose are installed on your machine.

### Running the project:

1. First of all, clone this repository;

2. Make sure to get a personal token for test on [Football Data API](https://www.football-data.org/client/register);

3. Add your token to API_TOKEN environment variable:
```
export API_TOKEN=your_token_here
```

3. Build and run the project using docker-compose:
```
docker-compose up --build
```

4. Once the server is running, you can access the API at http://localhost:5000.

For a better experince test it using Postman or other tool of your preference.

API Endpoints :link:

* /import-league/\<leagueCode\>
* /players/\<leagueCode\>
* /team/\<teamName\>
* /players-of-team/\<teamName\>

License :page_with_curl:
This project is licensed under the MIT License.
