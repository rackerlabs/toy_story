# Copyright (c) 2014 Rackspace, Inc.
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

"""WSGI callable for WSGI containers

This app should be used by external WSGI
containers. For example:

    $ gunicorn toystory.transport.app:app

NOTE: As for external containers, it is necessary
to put config files in the standard paths. There's
no common way to specify / pass configuration files
to the WSGI app when it is called from other apps.
"""

from oslo.config import cfg

from toystory import bootstrap


conf = cfg.CONF
conf(project='toystory', prog='toystory', args=[])

app = bootstrap.Bootstrap(conf).transport.app