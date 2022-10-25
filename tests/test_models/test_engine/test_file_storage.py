#!/usr/bin/python3
"""
Contains FileStorage test cases.
"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
	def setUp(self):
		self.storage = FileStorage()

	def test_storage(self):
		"""storage should be a FileStorage."""

		self.assertIsInstance(self.storage, FileStorage)

	def test_new_obj(self):
		"""It should add new object to storage."""

		my_model = BaseModel()
		self.storage.new(my_model)
		stored_model = self.storage.all().get("BaseModel.{}".format(my_model.id))
		self.assertEqual(my_model, stored_model)

	def test_new_other_objs(self):
		"""It should not add object to storage for none BaseModel objects."""

		old_size = len(self.storage.all())
		self.storage.new(None)
		self.storage.new(1)
		self.storage.new(1.5)
		self.storage.new([])
		self.storage.new([1,2,3,4])
		self.storage.new({})
		self.storage.new({'name': "jude"})
		self.storage.new(True)
		self.storage.new(False)
		new_size = len(self.storage.all())
		self.assertEqual(old_size, new_size)

	def test_all(self):
		"""It should return all objects stored in __objects."""

		objects = self.storage.all()
		self.assertIsInstance(objects, dict)
		if len(objects) > 0:
			for key in objects:
				obj = objects[key]
				self.assertIsInstance(obj, BaseModel)

	def test_save(self):
		"""It should save __objects to file.json"""

		my_model = BaseModel()
		my_model.name = "Test"
		my_model.magic = 101
		my_model.save()
		self.assertTrue(os.path.exists("file.json"))
		self.storage.reload()
		storedModel = self.storage.all().get("BaseModel.{}".format(my_model.id), None)
		self.assertIsNotNone(storedModel)

	def test_reload(self):
		"""It should reload objects from file.json into __objects"""

		self.storage.reload()
		objects = self.storage.all()
		self.assertIsInstance(objects, dict)

	def test_get_class(self):
		"""It should return the definition of a given class."""

		obj_class = self.storage.get_class("BaseModel")
		self.assertIs(BaseModel, obj_class)



if __name__ == "__main__":
	unittest.main(TestFileStorage)
