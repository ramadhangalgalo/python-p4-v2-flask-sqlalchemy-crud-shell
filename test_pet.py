#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'server'))

from app import app
from models import db, Pet

def test_pet_model():
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Test creating a pet
        pet = Pet(name="Fido", species="Dog")
        db.session.add(pet)
        db.session.commit()
        
        # Test querying
        found_pet = Pet.query.filter_by(name="Fido").first()
        assert found_pet is not None
        assert found_pet.name == "Fido"
        assert found_pet.species == "Dog"
        
        # Test updating
        found_pet.name = "Fido the mighty"
        db.session.commit()
        
        updated_pet = Pet.query.filter_by(id=found_pet.id).first()
        assert updated_pet.name == "Fido the mighty"
        
        # Test deleting
        db.session.delete(updated_pet)
        db.session.commit()
        
        deleted_pet = Pet.query.filter_by(id=found_pet.id).first()
        assert deleted_pet is None
        
        print("✅ All tests passed!")

if __name__ == "__main__":
    test_pet_model()