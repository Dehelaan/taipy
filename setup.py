# Copyright 2023 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

"""The setup script."""

from setuptools import find_namespace_packages, find_packages, setup


with open("README.md", "rb") as readme_file:
    readme = readme_file.read().decode("UTF-8")

test_requirements = ["pytest>=3.8"]

setup(
    author="Avaiga",
    author_email="dev@taipy.io",
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    description="An open-source repository contains Taipy templates and scaffoldings.",
    license="Apache License 2.0",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="taipy",
    name="taipy",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src") + find_packages(include=["taipy"]),
    include_package_data=True,
    test_suite="tests",
    url="https://github.com/avaiga/taipy-templates",
    zip_safe=False,
)
