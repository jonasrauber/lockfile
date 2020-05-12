.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black

======================================================================================
lockfile
======================================================================================

🔥 Why lockfile
----------------

**lockfile** provides a minimalistic and modern
implementation of a simple file-based lock mechanism.

- **Minimalistic**: lockfile does one thing, and one thing only
- **Modern**: lockfile supports :code:`pathlib.Path` objects
- **Type annotated**: lockfile provides comprehensive type annotations
- **Convinient**: lockfile automatically appendx a :code:`.lock` suffix if needed
- **Clean**: all code is formatted with Black and checked with MyPy and flake8

There are a number of alternatives such as
`py-filelock <https://github.com/benediktschmitt/py-filelock>`_ and
`FileLock <https://github.com/dmfrey/FileLock>`_ that actually inspired
this project but are more complex and somewhat outdated.


📖 Documentation
-----------------

Just look at this README and the code, it's really simple.


🚀 Quickstart
--------------

No installation, just copy
`lockfile.py <https://github.com/jonasrauber/lockfile/raw/master/lockfile.py>`_
to your project. It has zero dependencies beyond Python 3.6 or newer.

If you think an installable package might be useful, just open an issue.


🎉 Example
-----------

You can safely run the following code in two separate processes:

.. code-block:: python

   from pathlib import Path
   from lockfile import Lock

   path = Path("example.txt")
   with Lock(path):
       # Note: you don't need to use the lock to write to that specific file,
       # it can be used for anything

       with open(path, "w") as f:
           f.write("Hello!")


🗺 Use cases
------------

Whenever you need a simple, file-based locking mechanism in Python, for example
when you want to write to the same file from different processes, possibly
even from different machines using a shared file system (Note: NFS will
usually not provide the necessary guarantees, but there are other shared
(cluster) file systems that do).


🐍 Compatibility
-----------------

Python 3.6 and newer
