from app.models.planet import Planet
import pytest

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "New Planet",
        "description": "The Best!",
        "distance_from_sun": 69
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "The Best!"
    assert new_planet.distance_from_sun == 69

def test_from_dict_with_no_title():
    # Arrange
    planet_data = {
        "description": "The Best!"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'name'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "New Planet"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "New Planet",
        "description": "The Best!",
        "distance_from_sun": 69,
        "another": "last value"
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "New Planet"
    assert new_planet.description == "The Best!"
    assert new_planet.distance_from_sun == 69
    
    
    
    

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id = 1,
                    name="Lulu Moon",
                    description="The smallest and hottest planet to the Sun",
                    distance_from_sun= 69)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Lulu Moon"
    assert result["description"] == "The smallest and hottest planet to the Sun"
    assert result["distance_from_sun"] == 69

def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Lulu Moon",
                    description="The smallest and hottest planet to the Sun",
                    distance_from_sun= 69)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Lulu Moon"
    assert result["description"] == "The smallest and hottest planet to the Sun"
    assert result["distance_from_sun"] == 69

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id=1,
                    description="The smallest and hottest planet to the Sun",
                    distance_from_sun= 69)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "The smallest and hottest planet to the Sun"
    assert result["distance_from_sun"] == 69

def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id = 1,
                    name="Lulu Moon", 
                    distance_from_sun= 69)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Lulu Moon"
    assert result["description"] is None
    assert result["distance_from_sun"] == 69
    
    








