# Copyright 2018 F5 Networks Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

from f5.bigip.tm.sys.connection import Connection


class TestConnection(object):
    def test_load_refresh(self, mgmt_root):
        h1 = mgmt_root.tm.sys.connection.load()
        assert isinstance(h1, Connection)
        assert hasattr(h1, 'entries') or hasattr(h1, 'apiRawValues')
        assert h1.kind == 'tm:sys:connection:connectionstats'

        h2 = mgmt_root.tm.sys.connection.load()

        assert isinstance(h2, Connection)
        assert hasattr(h2, 'entries') or hasattr(h2, 'apiRawValues')
        assert h2.kind == 'tm:sys:connection:connectionstats'

        h1.refresh()

        assert h1.kind == h2.kind
