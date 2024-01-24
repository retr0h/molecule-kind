# Copyright (c) 2021 John Dewey <john@dewey.ws>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.
"""Kind Driver Module."""

from molecule_plugins.docker import driver


class Kind(driver.Docker):
    """
    Kind Driver Class.

    The class responsible for managing `kind`_.

    Molecule leverages Ansible's `command`_ module, by mapping
    variables from ``molecule.yml`` into ``create.yml`` and ``destroy.yml``.

    .. code-block:: yaml

        driver:
          name: molecule-kind
        platforms:
          - name: molecule-cluster

    .. _`kind`: https://github.com/kubernetes-sigs/kind
    """  # noqa

    def __init__(self, config=None) -> None:
        """Construct kind."""
        super().__init__(config)
        self._name = "molecule-kind"

    @property
    def default_safe_files(self):
        return []

    def login_options(self, instance_name):
        return {"instance": f"{instance_name}-control-plane"}

    def reset(self):
        # TODO(mnaser): Remove all "kind" clusters owned by Molecule
        pass
