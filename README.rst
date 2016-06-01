==========
pyocbc
==========


==========
Installing
==========

You can install or upgrade pyocbc with

.. code:: shell

    $ git clone https://github.com/connect2ocbc/pyocbc.git
    $ python setup.py install

==========
How to run
==========

.. code:: shell

    >>> import ocbc 
    >>> forex = ocbc.Forex("https://api.ocbc.com:8243/Forex/1.0", "<TOKEN>")
    >>> for rate in forex.all():
    >>>     print rate
   
    >>> branches = ocbc.Branches("https://api.ocbc.com:8243/branch_locator/1.0", "<TOKEN>")
    >>> for branch in branches.all():
    >>>     print branch

    >>> atms = ocbc.Atms("https://api.ocbc.com:8243/atm_locator/1.0", "<TOKEN>")
    >>> for atm in atms.all():
    >>>     print atm
   
    >>> ccsuggest = ocbc.CCSuggest("https://api.ocbc.com:8243/CC/1.0", "<TOKEN>")
    >>> for creditcard in ccsuggest.suggest('Dining'):
    >>>     print creditcard
   
