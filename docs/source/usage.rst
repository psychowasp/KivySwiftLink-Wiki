Usage
=====

.. _installation:

Installation
------------

Download a release.
Open a terminal and goto the folder you downloaded KivySwiftLink to.

.. code-block:: console

   chmod +x KivySwiftLink
   ./KivySwiftLink install


it will ask you if you want to copy the file as **ksl** to **/usr/local/bin/**

so from now on you just have to run KivySwiftLink like this:

```sh
ksl <commands>
```


Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

