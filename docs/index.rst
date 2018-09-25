.. Fabenv documentation master file, created by
   sphinx-quickstart on Sat Sep 22 10:42:53 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Fabenv!
==================================

What is Fabenv?
----------------

Fabenv is a high-level Python (3.4+) library which provides functions for creating
virtualenvs on remote servers, as well as installing packages to them, and running
other fabric operations in the context of the virtualenv.

.. code-block:: python

   from fabric import task
   from fabric import virtualenv

   @task
   def helloworld(c):
      with virtualenv("/tmp/virtenv"):
         c.run("which python")


It builds on top of Fabric2 (Fabric is a high level Python (2.7, 3.4+) library designed
to execute shell commands remotely over SSH).

How is it used?
---------------

Core use cases for Fabenv include (but are not limited to):

- Simple work in given virtualenv

.. code-block:: python

   @task
   def helloworld(c):
      with virtualenv("/tmp/virtenv"):
         c.run("which python")

- You can use other tools then virtualenv (e.g pipenv)

.. code-block:: python

   @task
   def helloworld(c):
      with pipenv("/tmp/virtenv"):
         c.run("which python")

- Easy package install

.. code-block:: python

   @task
   def helloworld(c):
      with virtualenv("/tmp/virtenv") as v:
         v.update()

.. toctree::
   :maxdepth: 2

   changelog
   faq
   install
   development
   routemap
   contact
