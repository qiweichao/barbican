# Copyright (c) 2013 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Simple Worker API implementation.
"""
from barbican.queue.resources import StartCSRMessage
import barbican.openstack.common.log as logging

LOG = logging.getLogger(__name__)


class StartCSRProcessor(object):
    """Process the start of CSR processing."""

    def process(self, message):
        LOG.debug("Processing CSR with ID = ", message.csr_id)


PROCESSES = {StartCSRMessage: StartCSRProcessor()}


def process(message):
    """
    Handle the specified message but simply passing
    through to the Worker Resource.
    """
    processor = PROCESSES[message.__class__]
    processor.process(message)