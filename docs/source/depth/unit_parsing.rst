==========================
Unit Parsing
==========================

Unit parsing is performed using the Pint_ package.
By default, Pint supports a larger set of units than the Citrine Platform.
Therefore, we include a custom unit definition file in Taurus: `citrine_en.txt`_.
This file contains the most commonly used units and will grow over time.

Requests for support of additional units can be made by opening an issue in the `taurus repository`_ on github.

.. _Pint: https://pint.readthedocs.io/en/0.9/
.. _citrine_en.txt: https://github.com/CitrineInformatics/taurus/blob/master/taurus/units/citrine_en.txt
.. _taurus repository: https://github.com/CitrineInformatics/taurus