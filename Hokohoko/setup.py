#   hokohoko/setup.py
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
#   This script contains the setup parameters for the main hokohoko
#   package.
#

import datetime
import os
import setuptools

from pathlib import Path

here = Path(os.path.abspath(__file__)).parent.absolute()

with open(here.joinpath("README.md"), "r", encoding="utf8") as fh:
	long_description = fh.read()

with open(here.joinpath("VERSION"), "r", encoding="utf8") as fv:
	version = fv.read().strip() + f"_{int(datetime.datetime.utcnow().timestamp())}"

setuptools.setup(
	name="hokohoko",
	version=version,
	author="Neil Bradley",
	author_email="neil.bradley@bebecom.co.nz",
	description="Provides a consistent interface to benchmark FOREX prediction projects.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/nc-bradley/Hokohoko",
	package_dir={"": "Hokohoko"},
	packages=["hokohoko", "hokohoko.entities", "hokohoko.standard"],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.7",
	install_requires=['numpy']
)
