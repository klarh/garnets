
## Introduction

`garnets` is a very simple wrapper over the
[garnett](https://github.com/glotzerlab/garnett) package. In version
0.7, the API of garnett changed to rename some frame attributes
(positions, orientations, velocities) to their singular
form.

If the new API is detected, `garnets` modifies the `Frame` class of
`garnett` when imported to add property setters and getters in order
to reduce the chance of breaking script compatibility. It also renames
the new API `types` property to `type_names` to remove the ambiguity
introduced by changing the meaning of the frame `types` attribute.

If the old API is detected, `garnets` adds `type_names` (list of
per-type name strings) and `typeid` (array of per-particle integer
indices) read-only properties for the sake of compatibility.