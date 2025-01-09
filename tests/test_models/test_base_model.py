#!usr bin/env python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    '''Test the BaseModel class'''

    def test_save(self):
        """Test save method updates updated_at."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(instance.updated_at, old_updated_at)
        self.assertTrue(instance.updated_at > old_updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertEqual(instance_dict["id"], instance.id)
        self.assertEqual(
            instance_dict["created_at"], instance.created_at.isoformat()
        )
        self.assertEqual(
            instance_dict["updated_at"], instance.updated_at.isoformat()
        )

    def test_id(self):
        """Test id attribute is unique and a string."""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertIsInstance(instance1.id, str)
        self.assertIsInstance(instance2.id, str)
        self.assertNotEqual(instance1.id, instance2.id)

    def test_created_at(self):
        """Test created_at attribute is a datetime object."""
        instance = BaseModel()
        self.assertIsInstance(instance.created_at, datetime)

    def test_str(self):
        """Test __str__ method."""
        instance = BaseModel()
        expected_str = f"[BaseModel] ({instance.id}) {instance.__dict__}"
        self.assertEqual(str(instance), expected_str)


if __name__ == '__main__':
    unittest.main()