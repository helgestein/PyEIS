"""
PyEIS
=====

Generate symbolic and lambda functions from the string representation of an electronic circuit in order to compute EIS data.

The module aims to be make the computation of EIS data or fitting of experimental data easier and faster by abstracting
the procedure of computing the analytic complex expressions of the immittance (Z(w) or Y(w)) and turning them into lambda functions.

The module contains also a fully operational procedure for fitting experimental data. 

The documentation is 80% completed and the code is still under active development. However, great care is taken
in avoiding backward incompatibilities.

How to install
--------------
Download the zip or tarball file and extract it locally. Install the package by using the setup.py file.

.. code-block:: python

    python setup.py install

Numpy, Scipy, Sympy and Matplotlib are required dependencies:
 * Numpy >=1.8
 * Scipy >=0.14
 * Sympy >=0.7.5
 * Matplotlib >=1.2
 * PrettyTables >=0.7.2

License information
-------------------

See the file ``LICENSE`` for information on the history of this
software, terms & conditions for usage, and a DISCLAIMER OF ALL
WARRANTIES.
"""

from __future__ import absolute_import

from . import eis_functions as eis
from . import circuit_decomposition as cdp
from . import version

__version__ = version.version

