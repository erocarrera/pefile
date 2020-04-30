###########################################################
PEiD Signatures
###########################################################

Since version 1.2.6, *pefile* supports parsing PEiD's signatures. Comprehensive signature databases can be found around the web. The last official release from the creators of PEid "BobSoft" can be found here: `UserDB.zip <http://web.archive.org/web/20160507191641/http://woodmann.com/BobSoft/Download.php?file=Files%2FOther%2FUserDB.zip>`__.

Usage
===========================================================

Loading
-----------------------------------------------------------

First import the new module, *peutils*, included with *pefile*.

.. code-block:: python

    import peutils

Then, we need to load a signature database, we can do this in different ways.

1. Loading a database from a file in the local filesystem

.. code-block:: python

    signatures = peutils.SignatureDatabase('/path/to/signature.txt')

2. Loading a database directly from a URL

.. code-block:: python

    signatures = peutils.SignatureDatabase('http://url.to/signature/file.txt')

3. And finally, directly from data (for instance, if we have already read and loaded the contents of a database)

.. code-block:: python

    with file('/path/to/signature/file.txt', 'rt') as f: 
        sig_data = f.read()
    signatures = peutils.SignatureDatabase(data=sig_data)

It's also possible to aggregate more signatures to an already created instance by just using the :py:func:`load()` method:

.. code-block:: python

    signatures.load('/Users/ero/Devel/pefile/userdb-extra.txt')

Matching
-----------------------------------------------------------

Once we have a ``SignatureDatabase`` instance, we can run PE instances through it in order to find matching packer signatures:

.. code-block:: python

    matches = signatures.match(pe, ep_only = True)

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    ['Upack 0.24 - 0.27 beta / 0.28 alpha -> Dwing']

We can also get all possible matches found as the signature tree is walked. The last signature will always be the most precise (as more bytes will have been matched) and is the one returned by the :py:func:`match()` method.

.. code-block:: python

    matches = sig.match_all(pe, ep_only = True)

Output
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    [['Upack v0.1x - v0.2x -> Dwing'], 
    ['Upack v0.24 ~ v0.28 Alpha -> Dwing'], 
    ['Upack 0.24 - 0.27 beta / 0.28 alpha -> Dwing']]

Signature generation
-----------------------------------------------------------

Experimental and not specially intelligent when generating signatures, *peutils* is able to generate a signature for a given PE file.

One can generate signatures for the entry point of a PE file as follows:

.. code-block:: python

    signatures.generate_ep_signature(pe, 'Name of the signature', length_of_the_signature)

Alternatively signatures for all section in a PE file can be generated as follows:

.. code-block:: python

    signatures.generate_section_signatures(pe, 'Name of the signature', length_of_the_signature)

Both of those methods will return a string following the same format as any other PEiD signature. For instance (straight out of UserDB.txt):

.. code-block:: python

    [!EP (ExE Pack) V1.0 -> Elite Coding Group]
    signature = 60 68 ?? ?? ?? ?? B8 ?? ?? ?? ?? FF 10
    ep_only = true


    [$pirit v1.5]
    signature = ?? ?? ?? 5B 24 55 50 44 FB 32 2E 31 5D
    ep_only = true


    [* PseudoSigner 0.1 [32Lite 0.03] --> Anorganix]
    signature = 60 06 FC 1E 07 BE 90 90 90 90 6A 04 68 90 10 90 90 68 ?? ?? ?? ?? E9 ?? ?? ?? ??
    ep_only = true