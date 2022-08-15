Generate PDF using library XHTML2PDF
==============

The documentation of xhtml2pdf is available at `Read the Docs <http://xhtml2pdf.readthedocs.io>`__.


Installation
============

This is tested on Python 3.9 and guaranteed to work.


Development environment
=======================

#. If you don't have it, install ``pip``, the python package installer::

    sudo easy_install pip

   For more information about ``pip`` refer to http://www.pip-installer.org

#. We will recommend using ``virtualenv`` for development.

#. Create a virtualenv for the project. This can be inside the project directory, but cannot be under version control::

    python -m venv xhtml2pdfenv

#. Activate your virtualenv::

    source xhtml2pdfenv/bin/activate

   Later to deactivate it use::

    deactivate

#. The next step will be to install/upgrade dependencies from the ``requirements.txt`` file::

    pip install -r requirements.txt

#. Run::

    python main.py