# FastAPI Social Media App Clone

This repository contains a backend clone of a social media application using **FastAPI**. The application includes key routes for managing posts, users, authentication, and likes.

## API Routes

The API provides four main routes:

### 1. Post Route
- **Functionality**: Create, update, delete, and retrieve posts.
- **Endpoints**:
  - `POST /posts`: Create a new post.
  - `GET /posts`: Get All Post with filters
  - `GET /posts/{id}`: Retrieve a specific post by ID.
  - `DELETE /posts/{id}`: Delete a post by ID.
  - `PUT /posts/{id}`: Update a post by ID.

### 2. Users Route
- **Functionality**: User management including creation and retrieval.
- **Endpoints**:
  - `POST /users`: Create a new user.
  - `GET /users/{id}`: Retrieve a user by ID.

### 3. Auth Route
- **Functionality**: User authentication and login.
- **Endpoints**:
  - `POST /auth/login`: User login and access token generation.

### 4. Like Route
- **Functionality**: Voting system to upvote posts.
- **Endpoints**:
  - `POST /like`: Like and unlike a post.

## Features
- **Authentication**: Implemented via JWT (JSON Web Token) for secure login and session management.
- **CRUD Operations**: Full CRUD (Create, Read, Update, Delete) support for posts and users.
- **Like System**: Users can upvote posts, similar to the "like" feature on social media.


## Running the App Locally

### 1. Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Docker (optional for containerization)
- Git

### 2. Clone the Repository
```bash
git clone https://github.com/Ajay2521/fastapi.git
cd fastapi
```

### 3. Set Up Environment Variables
Create a .env file in the root directory and add the following:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
SECRET_KEY=your_secret_key
```

### 4. Install Dependencies
Create a virtual environment and install the dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Apply Database Migrations
Use Alembic to apply the database migrations:

```
alembic upgrade head
```

### 6. Run the Application
To start the application locally, run:

```
uvicorn app.main:app --reload
```

Visit http://127.0.0.1:8000/docs for the API documentation powered by Swagger.

### 7. Running with Docker
If you prefer using Docker, run the following commands:

```
docker-compose up --build
```

### 8. Testing
The project includes tests using pytest. To run the tests:

```
pytest -v
```

### Continuous Integration and Deployment
This repository uses GitHub Actions for CI/CD and can be deployed to Heroku. Ensure that environment variables are properly configured in your CI pipeline.
