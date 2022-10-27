#!/usr/bin.python3
"""Contains all test cases of HBNBCommand console"""

import re
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """defines test cases for HBNBCommand"""

    def test_count(self):
        """It should return instance count of User
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            self.assertGreaterEqual(int(f.getvalue()), 0)

    def test_create_cmd(self):
        """It should create a User
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            self.assertEqual(len(obj_id), 36)

    def test_create_cmd_missing_class(self):
        """It should fail to create
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            msg = f.getvalue().strip()
            self.assertEqual(msg, "** class name missing **")

    def test_create_cmd_class_not_exists(self):
        """It should fail to create MyModel
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            msg = f.getvalue().strip()
            self.assertEqual(msg, "** class doesn't exist **")

    def test_all_cmd(self):
        """It should display all instances
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("all")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)

    def test_all_users_cmd(self):
        """It should display all User instances
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create Place")
            HBNBCommand().onecmd("all User")
            output = f.getvalue().strip()
            self.assertGreater(len(output), 0)
            match = re.search(r"Place", output)
            self.assertIsNone(match)

    def test_show_cmd(self):
        """It should display a User with given id
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            HBNBCommand().onecmd("show User {}".format(obj_id))
            output = f.getvalue().strip()
            match = re.search(r"User", output)
            self.assertIsNotNone(match)

    def test_show_cmd_missing_class(self):
        """It should fail to show
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_show_cmd_class_not_exists(self):
        """It should fail to show
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_cmd(self):
        """It should update User first_name
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj_id = f.getvalue().strip()
            cmd = 'update User {} "first_name" "Betty"'
            HBNBCommand().onecmd(cmd.format(obj_id))
            HBNBCommand().onecmd("show User {}".format(obj_id))
            output = f.getvalue().strip()
            match = re.search(r"first_name", output)
            self.assertIsNotNone(match)


if __name__ == "__main__":
    unittest.main(TestHBNBCommand)
