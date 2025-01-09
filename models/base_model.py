import uuid
import datetime

class BaseModel:
    '''BaseModel class'''
    def __init__(self, **kwargs):
        '''BaseModel class constructor'''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
         return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
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
