#!/usr/bin.python3
"""Contains all test cases of HBNBCommand console"""

import re
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.user import User


class TestHBNBCommand(unittest.TestCase):
    """defines test cases for HBNBCommand"""

    def test_do_count(self):
        """It should return instance count of User
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count_user(self):
        """It should return instance count of User
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_do_count_missing_class(self):
        """It should fail to count
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_count_class_not_exists(self):
        """It should fail to count
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_count__class_not_exists(self):
        """It should fail to count
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.count()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_create(self):
        """It should create a User using `create User` cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, User)

    def test_do_create_user(self):
        """It should create a User using User.create() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, User)

    def test_do_create_missing_class(self):
        """It should fail to create
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            msg = f.getvalue().strip()
            self.assertEqual(msg, "** class name missing **")

    def test_do_create_class_not_exists(self):
        """It should fail to create MyModel
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            msg = f.getvalue().strip()
            self.assertEqual(msg, "** class doesn't exist **")

    def test_do_create_user(self):
        """It should create a User using User.create() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            obj = storage.all().get(key)
            self.assertIsInstance(obj, User)

    def test_do_create_model_not_exists(self):
        """It should fail to create MyModel
        MyModel.create()
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.create()")
            msg = f.getvalue().strip()
            self.assertEqual(msg, "** class doesn't exist **")

    def test_do_all(self):
        """It should display all instances using all cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)

    def test_do_all_users(self):
        """It should display only User instances using
        cmd all User
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"Place", output)
            self.assertIsNone(match)

            HBNBCommand().onecmd("User.all()")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"Place", output)
            self.assertIsNone(match)

    def test_do_all__users(self):
        """It should display only User instances using
        cmd User.all()
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Place")

            HBNBCommand().onecmd("User.all()")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"Place", output)
            self.assertIsNone(match)

    def test_do_all_class_not_exists(self):
        """It should fail to display MyModel
        instances
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_all__class_not_exists(self):
        """It should fail to display MyModel
        instances
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.all()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_show(self):
        """It should display a User with given id using
        show User id cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("show User {}".format(obj_id))
            output = f.getvalue().strip()
            match = re.search(r"User", output)
            self.assertIsNotNone(match)

    def test_do_show_user(self):
        """It should display a User with given id using
        User.show(id) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("User.show({})".format(obj_id))
            output = f.getvalue().strip()
            match = re.search(r"User", output)
            self.assertIsNotNone(match)

    def test_do_show_missing_class(self):
        """It should fail to show
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_show_class_not_exists(self):
        """It should fail to show MyModel
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do__show_class_not_exists(self):
        """It should fail to MyModel.show()
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("MyModel.show()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_show_missing_id(self):
        """It should fail to show User with missing id
        using show User cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_show_user_missing_id(self):
        """It should fail to show User with missing id
        using User.show() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_show_user_invalid_id(self):
        """It should fail to show User with invalid id
        using show User "test-1234" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('show User "test-1234"')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_show__user_invalid_id(self):
        """It should fail to show User with invalid id
        using User.show("test-1234") cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.show("test-1234")')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_update(self):
        """It should update User first_name using
        update User id "first_name" "Betty" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'update User {} "first_name" "Betty"'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_user(self):
        """It should update User first_name using
        User.update("id", "first_name", "Betty") cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'User.update({}, "first_name", "Betty")'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_user_dict(self):
        """It should update User first_name using
        User.update("id", {"first_name": "Betty"}) cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            before_update = str(storage.all().get(key))
            data = '{"first_name": "Betty"}'
            cmd = 'User.update("{}", {})'
            HBNBCommand().onecmd(cmd.format(obj_id, data))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_missing_class(self):
        """It should fail to update using cmd
        update
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update")
            self.assertEqual(f.getvalue().strip(), "** class name missing **")

    def test_do_update_class_not_exists(self):
        """It should fail to update using cmd
        update MyModel
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update MyModel")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_do_update_id_not_exists(self):
        """It should fail to update using cmd
        update User
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("update User")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update_no_attribute(self):
        """It should fail to update using cmd
        update User id
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("update User {}".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** attribute name missing **")

    def test_do_update_no_value(self):
        """It should fail to update using cmd
        update User id
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            command = 'update User {} "first_name"'
            HBNBCommand().onecmd(command.format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** value missing **")

    def test_do_update_user(self):
        """It should update User first_name using
        User.update("id", "first_name", "Betty") cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            before_update = str(storage.all().get(key))
            cmd = 'User.update({}, "first_name", "Betty")'
            HBNBCommand().onecmd(cmd.format(obj_id))
            after_update = str(storage.all().get(key))
            self.assertNotEqual(before_update, after_update)

    def test_do_update_model_not_exists(self):
        """It should fail to update using cmd
        MyModel.update()
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("MyModel.update()")
            self.assertEqual(f.getvalue().strip(), "** class doesn't exist **")

    def test_do_update_user_missing_id(self):
        """It should fail to update using cmd
        User.update()
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("User.update()")
            self.assertEqual(f.getvalue().strip(), "** instance id missing **")

    def test_do_update_user_invalid_id(self):
        """It should fail to update using cmd
        update User "test-1234"
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd('update User "test-1234"')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_do_update__user_invalid_id(self):
        """It should fail to update using cmd
        User.update("test-1234")
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd('User.update("test-1234")')
            self.assertEqual(f.getvalue().strip(), "** no instance found **")

    def test_do_update_user_missing_attribute(self):
        """It should fail to update using cmd
        User.update(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd('User.update("{}")'.format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** attribute name missing **")

    def test_do_update_user_missing_value(self):
        """It should fail to update using cmd
        User.update(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:

            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            command = 'User.update({}, "first_name")'
            HBNBCommand().onecmd(command.format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** value missing **")

    def test_do_update_user_empty_dict(self):
        """It should not have any effect on user using
        User.update(id, {})
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            key = "User.{}".format(obj_id)
            before_update = str(storage.all().get(key))
            data = '{}'
            cmd = 'User.update("{}", {})'
            HBNBCommand().onecmd(cmd.format(obj_id, data))
            after_update = str(storage.all().get(key))
            self.assertEqual(before_update, after_update)

    def test_do_destroy(self):
        """It should delete a user using the cmd
        destroy User id
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("destroy User {}".format(obj_id))
            HBNBCommand().onecmd("show User {}".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_user(self):
        """It should delete a user using the cmd
        User.destroy(id)
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("User.destroy({})".format(obj_id))
            HBNBCommand().onecmd("User.show({})".format(obj_id))
            output = f.getvalue().strip().split("\n")[-1]
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy_missing_class(self):
        """It should fail to destroy
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_do_destroy_class_not_exists(self):
        """It should fail to destroy MyModel
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_do_destroy_missing_id(self):
        """It should fail to destroy User with missing id
        using destroy User cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_destroy_user_missing_id(self):
        """It should fail to destroy User with missing id
        using User.destroy() cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy()")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_do_destroy_user_invalid_id(self):
        """It should fail to destroy User with missing id
        using destroy User "test-1234" cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('destroy User "test-1234"')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_do_destroy__user_invalid_id(self):
        """It should fail to destroy User with missing id
        using User.destroy("test-1234") cmd
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd('User.destroy("test-1234")')
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


if __name__ == "__main__":
    unittest.main(TestHBNBCommand)
