### Challenge: Build and Orchestrate a Flask Application with a PostgreSQL Database

**Task:**
You will build a web service using Flask (Python) that uses a PostgreSQL database to manage user data. The web service should run in a Docker environment where both the application and the database are in separate containers.

#### Step-by-Step:

1. **Create a Flask Application**
   - Develop a simple Flask application with at least one route (`/users`) that can display and add users to the database.
   - Use SQLAlchemy to interact with the PostgreSQL database.

2. **PostgreSQL Database**
   - Launch a PostgreSQL container in Docker and connect it to the Flask application.
   - Create a `users` table with fields such as `id`, `name`, and `email`.

3. **Dockerfile for Flask Application**
   - Write a Dockerfile for your Flask application that includes all dependencies and starts the Flask server.

4. **Docker Compose**
   - Use Docker Compose to orchestrate both the Flask application and the PostgreSQL database so they can communicate with each other.
   - Ensure that the Flask container waits for the PostgreSQL container to be ready before starting.

5. **Test the Application**
   - Make sure you can bring up everything with a single command (`docker-compose up`) and that you can add and view users via the web service.

6. **Bonus (Optional):**
   - Add a frontend with HTML and JavaScript that can communicate with your Flask API to display and add users.

#### File Structure:
```
my_flask_app/
│
├── app/
│   ├── app.py          # Flask application
│   ├── requirements.txt # Flask libraries and dependencies
│
├── Dockerfile           # Dockerfile for Flask application
├── docker-compose.yml   # Docker Compose file
```

#### Tips:
- Flask and PostgreSQL can be connected using an environment variable configured in the `docker-compose.yml`.
- Use health checks to ensure that PostgreSQL is ready before Flask starts.

Good luck!
