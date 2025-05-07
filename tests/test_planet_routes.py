import pytest

def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []
    

def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Lulu Moon",
        "description": "The smallest and hottest planet to the Sun",
        "distance_from_sun": 69
    }
    

    
def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "New Planet",
        "description": "Not The Best!",
        "distance_from_sun": 77
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Planet",
        "description": "Not The Best!",
        "distance_from_sun": 77
    }   
    
def test_create_one_planet_no_name(client):
    # Arrange
    test_data = {"description": "The Best!"}

    # Act 
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing name'}

def test_create_one_planet_no_description(client):
    # Arrange
    test_data = {"name": "New Planet"}

    # Act 
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()
    
    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing description'}


def test_create_one_planet_with_extra_keys(client):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name": "New Book",
        "description": "The Best!",
        "distance_from_sun": 66,
        "another": "last value"
    }

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "New Book",
        "description": "The Best!",
        "distance_from_sun": 66
    }
    


# When we have records, `get_all_books` returns a list containing a dictionary representing each `Book`
def test_get_all_planets_with_two_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
        "id": 1,
        "name": "Lulu Moon",
        "description": "The smallest and hottest planet to the Sun",
        "distance_from_sun": 69
    }
    assert response_body[1] == {
        "id": 2,
        "name": "Venus",
        "description": "Venus as a boy",
        "distance_from_sun": 85
    }

# When we have records and a `title` query in the request arguments, `get_all_books` returns a list containing only the `Book`s that match the query
def test_get_all_planets_with_title_query_matching_none(client, two_saved_planets):
    # Act
    data = {'name': 'Desert Planet'}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# When we have records and a `title` query in the request arguments, `get_all_books` returns a list containing only the `Book`s that match the query
def test_get_all_books_with_title_query_matching_one(client, two_saved_planets):
    # Act
    data = {'name': 'Lulu Moon'}
    response = client.get("/planets", query_string=data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "name": "Lulu Moon",
        "description": "The smallest and hottest planet to the Sun",
        "distance_from_sun": 69.0
    }

# When we call `get_one_book` with a numeric ID that doesn't have a record, we get the expected error message
def test_get_one_planet_missing_record(client, two_saved_planets):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "planet 3 not found"}

# When we call `get_one_book` with a non-numeric ID, we get the expected error message
def test_get_one_planet_invalid_id(client, two_saved_planets):
    # Act
    response = client.get("/planets/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "planet cat invalid"}   
    
    
