# Pizza Restaurant Code Challenge - Implementation Complete

## What I've Implemented

### 1. Models (server/models.py)
- **Restaurant**: Added relationships and serialization rules
- **Pizza**: Added relationships and serialization rules  
- **RestaurantPizza**: Added foreign keys, relationships, validation, and serialization rules

### 2. Relationships
- Restaurant has many Pizzas through RestaurantPizza
- Pizza has many Restaurants through RestaurantPizza
- RestaurantPizza belongs to Restaurant and Pizza
- Configured cascade deletes

### 3. Validation
- RestaurantPizza price must be between 1 and 30

### 4. API Routes (server/app.py)
- **GET /restaurants** - Returns all restaurants (id, name, address only)
- **GET /restaurants/<id>** - Returns restaurant with restaurant_pizzas or 404 error
- **DELETE /restaurants/<id>** - Deletes restaurant and associated RestaurantPizzas or 404 error
- **GET /pizzas** - Returns all pizzas (id, name, ingredients only)
- **POST /restaurant_pizzas** - Creates new RestaurantPizza with validation

### 5. Error Handling
- Proper HTTP status codes (200, 201, 204, 400, 404)
- Validation error messages match test expectations
- Restaurant not found errors

### 6. Serialization
- Configured to prevent infinite recursion
- Proper field inclusion/exclusion for each endpoint

## To Run the Application

1. Install dependencies: `pipenv install`
2. Activate environment: `pipenv shell`
3. Initialize database: `cd server && python init_db.py`
4. Seed database: `python seed.py`
5. Run server: `python app.py`
6. Test with Postman collection or run `pytest -x`

## API Endpoints Ready for Testing

All endpoints are implemented according to the requirements and should pass the provided tests once the dependency issues are resolved.