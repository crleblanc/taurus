"""A nominal composition value."""
from taurus.entity.value.composition_value import CompositionValue


class NominalComposition(CompositionValue):
    """
    Nominal composition, represented as a map from the component names to the quantities.

    The quantities do not express an uncertainty but also do not imply that there is absolute
    certainty to their values.

    Parameters
    ----------
    quantities: Map[String, Number]
        A map from each component to its amount.  The quantities are not required to be expressed
        on a unit or fractional basis. The following are all acceptable:

        * dict(acetone=0.25, methanol=0.75)
        * dict(acetone=1, methanol=3)
        * dict(acetone=3.5, methanol=10.5)

    """

    typ = "nominal_composition"

    def __init__(self, quantities=None):
        self._quantities = None
        self.quantities = quantities

    @property
    def quantities(self):
        """Get a map from the components to their quantities."""
        return self._quantities

    @quantities.setter
    def quantities(self, quantities):
        if quantities is None:
            self._quantities = {}
        elif isinstance(quantities, dict):
            self._quantities = quantities
        elif isinstance(quantities, list):
            self._quantities = dict(quantities)
        else:
            raise TypeError("quantities must be dict or List of two-item lists or None")

    def as_dict(self):
        """
        Convert the composition to a dictionary.

        Overrides the ordinary
        :func:`as_dict() <taurus.entity.dict_serializable.DictSerializable.as_dict>` method in
        that the `quantities` field is turned into a list of lists,
        each of which has the form [component, quantity].
        """
        return {"type": self.typ, "quantities": list(list(x) for x in self.quantities.items())}
