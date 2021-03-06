#   generate_tests.sh
#
#   Copyright 2020 Neil Bradley
#
#   This file is part of Hokohoko.
#
#   Hokohoko is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Hokohoko is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY# without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Hokohoko.  If not, see <https://www.gnu.org/licenses/>.
#
#   ====================================================================
#
#   hokohoko.utils provides an @generate_tests decorator, which this
#   script uses to find missing unit tests within the hokohoko projects.
#   Any missing tests are auto-generated with automatic failure status.
#   This script assumes it has been run within the base directory.
#

import ast
import os
import re
import sys
from collections import deque


def build_file(path, fq_filename, test_cases):

    # 1. Check if the file exists. If it does, load it, otherwise
    #    generate a new file.
    oops = fq_filename.split("\\")[1:]
    oops[-1] = "test_" + oops[-1].replace("_", "")
    target = os.sep.join((path, *oops))
    print(target)
    if os.path.isfile(target):
        with open(target, "rt") as of:
            lines = of.read()
    else:
        lines = f"# Generated by generate_tests.\n" \
                f"import unittest as ut\n\n\n"

    module = fq_filename.split("\\")[-1].replace(".py", "").replace("_", "").title()
    cls = f"class Test{module}(ut.TestCase):\n"
    tail = f"\nif __name__ == '__main__':\n    ut.main()\n"

    # 2. Generate the new test methods.
    to_add = ""
    filename = fq_filename.rsplit("\\")[-1]
    for method, line, tcs in test_cases:
        tcs = [t.strip() for t in tcs.replace("\\n", "\n").split("\n")]

        for tc in tcs:
            if tc[0] == '#':
                continue
            c = "_".join(["test", method.replace("__", ""), tc.replace(" ", "_")])
            c = "    def " + re.sub(r'\W+', '', c) + "(self):\n"
            comment = f'        """Auto-generated from {filename}:{line}"""\n'
            nyi = "        self.fail('TODO: Implement me!')\n\n"

            if c not in lines:
                to_add += c + comment + nyi

    # 3. Add into lines.
    if cls not in lines:
        to_add = cls + to_add

    if "\nif __name__ == " in lines:
        index = lines.index("\nif __name__ == ")
        start = lines[:index]
        tail = lines[index:]
    else:
        start = lines

    # 4. Write it out.
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "wt") as of:
        of.write(start + to_add + tail)
        print("Wrote out: ", target)


def get_hokohoko_test_cases(body):
    """
    Build the list of items recursively.

    :param body:    The first body from the parsed file.

    :returns:       All the test cases in the file.
    """
    test_cases = []
    queue = deque([body])
    while len(queue) > 0:
        z = queue.popleft()
        for b in z:
            if isinstance(b, ast.ClassDef):
                queue.append(b.body)
            if isinstance(b, ast.FunctionDef):
                queue.append(b.body)
                if len(b.decorator_list) > 0:
                    for dl in b.decorator_list:
                        if hasattr(dl, 'func'):
                            if isinstance(dl.func, ast.Name):
                                if dl.func.id == 'generate_tests':
                                    test_cases.append((b.name, dl.args[0].lineno, dl.args[0].value.strip()))
                            elif isinstance(dl.func, ast.Attribute):
                                if dl.func.attr == 'generate_tests':
                                    test_cases.append((b.name, dl.args[0].lineno, dl.args[0].value.strip()))
    return test_cases


if __name__ == "__main__":

    file_list = []
    for packages in ["Assessors", "Hokohoko", "Predictors"]:
        for p, d, files in os.walk(os.sep.join([os.curdir, packages])):
            if "__pycache__" in p:
                continue
            for f in files:
                if ".py" in f:
                    file_list.append((p, f))

    to_test = {}
    for p, f in file_list:
        fq_name = os.sep.join((p, f))
        with open(fq_name, "rt") as o:
            print(fq_name)
            a = ast.parse(o.read(), filename=f)
            htc = get_hokohoko_test_cases(a.body)
            if len(htc) > 0:
                to_test[fq_name] = htc

    root = os.sep.join([*(os.getcwd().split(os.sep)), "Tests"])
    for filepath, cases in to_test.items():
        build_file(root, filepath, cases)

    sys.exit()
