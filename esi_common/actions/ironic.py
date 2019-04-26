#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from ConfigParser import ConfigParser

from ironicclient import client as ironicclient
from mistral_lib import actions


class IronicAction(actions.Action):

    def __init__(self):
        super(IronicAction, self).__init__()

    def get_baremetal_client(self):
        config = ConfigParser()
        config.read('/etc/esi/esi.conf')

        kwargs = {
            'username': config.get('ironic', 'username'),
            'password': config.get('ironic', 'password'),
            'auth_url': config.get('ironic', 'auth_url'),
            'tenant_name': config.get('ironic', 'project_name'),
            'user_domain_name': config.get('ironic', 'user_domain_name'),
            'project_domain_name': config.get('ironic', 'project_domain_name'),
            'insecure': 'true',
            'max_retries': 12,
            'retry_interval': 5,
            'os_ironic_api_version': '1.52',
        }

        return ironicclient.get_client(1, **kwargs)


class NodeCreateAction(IronicAction):
    def __init__(self,  **kwargs):
        super(NodeCreateAction, self).__init__()
        self.kwargs = kwargs

    def run(self, context):
        return self.get_baremetal_client().node.create(**self.kwargs)


class NodeUpdateAction(IronicAction):
    def __init__(self, node_id, patch):
        super(NodeUpdateAction, self).__init__()
        self.node_id = node_id
        self.patch = patch

    def run(self, context):
        return self.get_baremetal_client().node.update(self.node_id, self.patch)


class NodeGetAction(IronicAction):
    def __init__(self, node_id):
        super(NodeGetAction, self).__init__()
        self.node_id = node_id

    def run(self, context):
        return self.get_baremetal_client().node.get(self.node_id)


class NodeSetProvisionStateAction(IronicAction):
    def __init__(self, node_uuid, state):
        super(NodeSetProvisionStateAction, self).__init__()
        self.node_uuid = node_uuid
        self.state = state

    def run(self, context):
        return self.get_baremetal_client().node.set_provision_state(self.node_uuid, self.state)


class PortCreateAction(IronicAction):
    def __init__(self, **kwargs):
        super(PortCreateAction, self).__init__()
        self.kwargs = kwargs

    def run(self, context):
        return self.get_baremetal_client().port.create(**self.kwargs)
