from contextlib import contextmanager, redirect_stdout
from io import StringIO
from importlib.machinery import SourceFileLoader
import os
import sys
from textwrap import dedent
from tempfile import NamedTemporaryFile
import unittest


class INI2CSV(unittest.TestCase):

    """Tests for ini2csv.py"""

    maxDiff = None

    def test_two_groups(self):
        contents = dedent("""
            [*.py]
            indent_style = space
            indent_size = 4

            [*.js]
            indent_style = space
            indent_size = 2
        """).lstrip()
        expected = dedent("""
            *.py,indent_style,space
            *.py,indent_size,4
            *.js,indent_style,space
            *.js,indent_size,2
        """).lstrip()
        with make_file(contents) as ini_file, make_file() as csv_file:
            stdout = run_program('ini2csv.py', args=[ini_file, csv_file])
            self.assertEqual(stdout, '')
            with open(csv_file) as csv:
                output = csv.read()
        self.assertEqual(expected, output)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_collapsed(self):
        contents = dedent("""
            [*.py]
            indent_style = space
            indent_size = 4

            [*.js]
            indent_style = space
            indent_size = 2
        """).lstrip()
        expected = dedent("""
            header,indent_style,indent_size
            *.py,space,4
            *.js,space,2
        """).lstrip()
        with make_file(contents) as ini_file, make_file() as csv_file:
            run_program('ini2csv.py', args=['--collapsed', ini_file, csv_file])
            with open(csv_file) as csv:
                output = csv.read()
        self.assertEqual(expected, output)


def run_program(path, args=[]):
    """Run program at given path with given arguments."""
    old_args = sys.argv
    assert all(isinstance(a, str) for a in args)
    try:
        sys.argv = [path] + args
        with redirect_stdout(StringIO()) as output:
            try:
                if '__main__' in sys.modules:
                    del sys.modules['__main__']
                SourceFileLoader('__main__', path).load_module()
            except SystemExit as e:
                if e.args != (0,):
                    raise
            del sys.modules['__main__']
            return output.getvalue()
    finally:
        sys.argv = old_args


@contextmanager
def make_file(contents=None):
    """Context manager providing name of a file containing given contents."""
    with NamedTemporaryFile(mode='wt', encoding='utf-8', delete=False) as f:
        if contents:
            f.write(contents)
    try:
        yield f.name
    finally:
        os.remove(f.name)


if __name__ == "__main__":
    unittest.main(verbosity=2)