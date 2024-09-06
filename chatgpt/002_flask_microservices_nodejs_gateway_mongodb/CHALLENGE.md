### Challenge: Build a Microservices Architecture with a Node.js API Gateway and Two Flask Microservices

**Task:**
You will build a microservices architecture that includes:
- **Node.js API Gateway** that handles incoming requests and forwards them to the appropriate microservice.
- **Two Flask microservices**:
  - **User Service**: Manages user data (create, read, update, delete users).
  - **Product Service**: Manages product data (create, read, update, delete products).
- **MongoDB** as the database for the Flask services.

The services and database should run in separate Docker containers, orchestrated with Docker Compose.

### Step-by-Step:

1. **Create the User Service (Flask)**
   - This service should expose routes to manage users (`/users`):
     - GET `/users` (list all users)
     - POST `/users` (create a new user)
     - PUT `/users/<id>` (update a user)
     - DELETE `/users/<id>` (delete a user)

2. **Create the Product Service (Flask)**
   - This service should expose routes to manage products (`/products`):
     - GET `/products` (list all products)
     - POST `/products` (create a new product)
     - PUT `/products/<id>` (update a product)
     - DELETE `/products/<id>` (delete a product)

3. **Create the API Gateway (Node.js)**
   - The API Gateway will route requests to the correct microservice based on the request path:
     - Requests starting with `/users` should be routed to the **User Service**.
     - Requests starting with `/products` should be routed to the **Product Service**.
   - You can use Express in Node.js to create this gateway.

4. **Database (MongoDB)**
   - Both Flask microservices should connect to separate MongoDB collections (one for users, one for products).
   - The MongoDB instance should run in a separate container.

5. **Docker Compose**
   - Use Docker Compose to orchestrate the API Gateway, the two Flask microservices, and the MongoDB database.

6. **Testing the System**
   - You should be able to interact with the entire system by sending requests through the API Gateway.

### Acceptance Criteria:

1. **API Gateway Routing:**
   - The Node.js API Gateway must correctly route requests to `/users` and `/products` to the corresponding Flask microservices.
   - If an invalid route is hit (e.g., `/invalid`), the gateway should return a `404` status code.

2. **User Service:**
   - When accessing `/users` via the API Gateway, you should be able to:
     - **Create a new user** (e.g., POST a user with `name`, `email`).
     - **List all users**.
     - **Update a user** (by ID).
     - **Delete a user** (by ID).

3. **Product Service:**
   - When accessing `/products` via the API Gateway, you should be able to:
     - **Create a new product** (e.g., POST a product with `name`, `price`).
     - **List all products**.
     - **Update a product** (by ID).
     - **Delete a product** (by ID).

4. **Database Persistence:**
   - User and product data must be persisted in MongoDB.
   - You should be able to restart the services and still see the previously added users and products in MongoDB.

5. **Containerization:**
   - The entire system must be orchestrated with Docker Compose.
   - You should be able to start all containers with one command: `docker-compose up`.

6. **Bonus (Optional):**
   - Add logging in the API Gateway to track requests and responses, including the forwarded routes and services they hit.
   - Add health checks to ensure the Flask services are healthy before they start processing requests.

### File Structure:

```
microservices_project/
│
├── api_gateway/
│   ├── index.js         # Node.js API Gateway
│   ├── package.json     # Dependencies for the API Gateway
│
├── user_service/
│   ├── app.py           # Flask app for the User Service
│   ├── requirements.txt # Dependencies for the User Service
│
├── product_service/
│   ├── app.py           # Flask app for the Product Service
│   ├── requirements.txt # Dependencies for the Product Service
│
├── docker-compose.yml   # Docker Compose file to orchestrate everything
```

### Tips:

- Use **MongoDB Docker image** for the database.
- The **Node.js API Gateway** can use `axios` or similar to make HTTP requests to the Flask services.
- Set up **different collections** in MongoDB for users and products.

Good luck! This should challenge both your Docker and API orchestration skills!