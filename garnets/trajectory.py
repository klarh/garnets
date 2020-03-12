import functools

import numpy as np

from garnett.trajectory import Frame as GarnettFrame

def _plural_getter(self, name):
    return getattr(self, name)

def _plural_setter(self, value, name):
    setattr(self, name, value)

_attrs = ['positions', 'orientations', 'velocities']

_singular_map = dict(velocities='velocity')

if not hasattr(GarnettFrame, 'positions'):
    for attr in _attrs:
        singular_name = _singular_map.get(attr, attr[:-1])
        prop = property(functools.partial(_plural_getter, name=singular_name),
                        functools.partial(_plural_setter, name=singular_name))
        setattr(GarnettFrame, attr, prop)

    prop = property(functools.partial(_plural_getter, name='types'),
                    functools.partial(_plural_setter, name='types'))
    GarnettFrame.type_names = prop
else:
    def _get_type_names(self):
        # self.types is a per-particle list of type names
        return list(sorted(set(self.types)))

    def _get_type_ids(self):
        type_map = {k: i for (i, k) in enumerate(self.type_names)}
        result = [type_map[t] for t in self.types]
        return np.array(result, dtype=np.uint32)

    GarnettFrame.type_names = property(_get_type_names)
    GarnettFrame.typeid = property(_get_type_ids)
