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

import os

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
        connection_opts = self.ansible_connection_options(instance_name)
        return {"instance": connection_opts["ansible_host"]}

    def ansible_connection_options(self, instance_name):
        opts = super().ansible_connection_options(instance_name)

        # Cluster name is set from "MOLECULE_KIND_CLUSTER_NAME" environment
        # variable or defaults to the name of the molecule scenario.
        cluster_name = os.environ.get(
            "MOLECULE_KIND_CLUSTER_NAME", self._config.scenario.name
        )

        # Get list of platforms and figure out what role this instance is.
        platforms = self._config.config.get("platforms", [])
        platform = next((p for p in platforms if p["name"] == instance_name), None)
        if not platform:
            raise RuntimeError(f"Unable to find platform with name {instance_name}")

        # Group the platforms by role and figure out the index of this instance
        # in the list of instances for the role.
        role = platform.get("role", "control-plane")
        role_platforms = [
            p for p in platforms if p.get("role", "control-plane") == role
        ]
        role_instance_index = role_platforms.index(platform)

        # Generate the "ansible_host" option based on the role and instance index.
        opts["ansible_host"] = f"{cluster_name}-{role}"
        if role_instance_index != 0:
            opts["ansible_host"] += str(role_instance_index + 1)

        return opts

    def reset(self):
        # TODO(mnaser): Remove all "kind" clusters owned by Molecule
        pass
