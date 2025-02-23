from taurus.util.impl import substitute_objects, recursive_foreach
from taurus.entity.object import ProcessRun, MaterialRun, MeasurementSpec
from taurus.entity.value.normal_real import NormalReal
from taurus.entity.attribute.parameter import Parameter
from taurus.entity.template.parameter_template import ParameterTemplate
from taurus.entity.template.measurement_template import MeasurementTemplate
from taurus.entity.link_by_uid import LinkByUID
from taurus.entity.bounds.real_bounds import RealBounds


def test_dictionary_substitution():
    """substitute_objects() should substitute LinkByUIDs that occur in dict keys and values."""
    proc = ProcessRun("A process", uids={'id': '123'})
    mat = MaterialRun("A material", uids={'generic id': '38f8jf'})

    proc_link = LinkByUID.from_entity(proc)
    mat_link = LinkByUID.from_entity(mat)
    index = {(mat_link.scope.lower(), mat_link.id): mat,
             (proc_link.scope.lower(), proc_link.id): proc}

    test_dict = {LinkByUID.from_entity(proc): LinkByUID.from_entity(mat)}
    substitute_objects(test_dict, index)
    assert test_dict[proc] == mat


def test_recursive_foreach():
    """Test that recursive_foreach() applies a method to every object."""
    new_tag = "Extra tag"

    def func(base_ent):
        """Adds a specific tag to the object."""
        base_ent.tags.extend([new_tag])
        return

    param_template = ParameterTemplate("a param template", bounds=RealBounds(0, 100, ''))
    meas_template = MeasurementTemplate("Measurement template", parameters=[param_template])
    parameter = Parameter(name="A parameter", value=NormalReal(mean=17, std=1, units=''))
    measurement = MeasurementSpec(name="name", parameters=parameter, template=meas_template)
    test_dict = {"foo": measurement}
    recursive_foreach(test_dict, func, apply_first=True)

    for ent in [param_template, meas_template, measurement]:
        assert new_tag in ent.tags
