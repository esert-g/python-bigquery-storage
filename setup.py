# -*- coding: utf-8 -*-
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import io
import os

import setuptools

name = "google-cloud-bigquery-storage"
description = "BigQuery Storage API API client library"
version = "2.10.1"
release_status = "Development Status :: 5 - Production/Stable"
dependencies = [
    # NOTE: Maintainers, please do not require google-api-core>=2.x.x
    # Until this issue is closed
    # https://github.com/googleapis/google-cloud-python/issues/10566
    "google-api-core[grpc] >= 1.28.0, <3.0.0dev",
    "proto-plus >= 1.18.0",
    "libcst >= 0.2.5",
]
extras = {
    "pandas": ["pandas>=0.21.1"],
    "fastavro": ["fastavro>=0.21.2"],
    "pyarrow": ["pyarrow>=0.15.0"],
    "tests": ["freezegun"],
}

package_root = os.path.abspath(os.path.dirname(__file__))

readme_filename = os.path.join(package_root, "README.rst")
with io.open(readme_filename, encoding="utf-8") as readme_file:
    readme = readme_file.read()

packages = [
    package
    for package in setuptools.PEP420PackageFinder.find()
    if package.startswith("google")
]

namespaces = ["google"]
if "google.cloud" in packages:
    namespaces.append("google.cloud")

setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description=readme,
    author="Google LLC",
    author_email="googleapis-packages@google.com",
    license="Apache 2.0",
    url="https://github.com/googleapis/python-bigquery-storage",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
        "Topic :: Internet",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=packages,
    namespace_packages=namespaces,
    install_requires=dependencies,
    extras_require=extras,
    python_requires=">=3.6",
    scripts=["scripts/fixup_bigquery_storage_v1_keywords.py"],
    include_package_data=True,
    zip_safe=False,
)
