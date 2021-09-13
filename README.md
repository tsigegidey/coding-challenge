<h1> Shapes Library </h1>
<p>A general purpose Python library that provides clients with intuitive object-oriented APIs for 2D and 3D shapes.</p>

<h2> Developer Installation </h2>
<p>**Note that all below commands should be run within the project root directory (/path/to/coding-challenge)**</p>

Firstly, install all the required primary and testing dependencies with the following commands from the root directory:

- <code> pip install -r requirements.txt </code>
- <code> pip install -r requirements_test.txt </code>

**shapes_library** can be installed into your local Python package registry with the following command: <code> pip install -e . </code>

You should now be able to use functionality offered by the **shapes_module** Python module by importing shape APIs directly:

<code>
from shapes_library.shapes_package.shapes_module import Circle
</code>

<h3> Testing </h3>
Developers can test the library source with the following commands assuming the aforementioned dependencies have been installed:

- With coverage: <code> pytest --cov=shapes_library [tests/] </code>
- Without coverage: <code> pytest [tests/]</code>
