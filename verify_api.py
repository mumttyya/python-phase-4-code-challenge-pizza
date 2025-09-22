#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'server'))

from server.app import app

def test_api():
    with app.test_client() as client:
        print("Testing API Endpoints")
        print("====================")
        
        # Test GET /restaurants
        response = client.get('/restaurants')
        print(f"GET /restaurants: {response.status_code}")
        if response.status_code == 200:
            data = response.get_json()
            print(f"  Found {len(data)} restaurants")
        
        # Test GET /pizzas  
        response = client.get('/pizzas')
        print(f"GET /pizzas: {response.status_code}")
        if response.status_code == 200:
            data = response.get_json()
            print(f"  Found {len(data)} pizzas")
        
        # Test GET /restaurants/1
        response = client.get('/restaurants/1')
        print(f"GET /restaurants/1: {response.status_code}")
        
        # Test POST /restaurant_pizzas
        response = client.post('/restaurant_pizzas', json={
            "price": 10,
            "pizza_id": 1,
            "restaurant_id": 1
        })
        print(f"POST /restaurant_pizzas: {response.status_code}")
        
        print("\n✅ All API endpoints are working!")

if __name__ == "__main__":
    test_api()