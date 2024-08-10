A Call of Cthulhu character generator
=====================================

.. toctree::
   :hidden:
   :maxdepth: 1

   license
   reference

Installation
------------

For now only source installation is supported and `poetry <https://python-poetry.org/>`_ needs to be installed.

.. code-block:: console

   $ git clone https://github.com/MrShark/coc-generator.git
   $ cd coc-generator
   $ poetry install

Usage
-----

.. click:: coc_gen.cli:investigator
    :prog: investigator
    :nested: full
