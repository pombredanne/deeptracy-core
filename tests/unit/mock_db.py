# Copyright 2017 BBVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class MockFilter:
    _ret_val = None

    def __init__(self, model):
        self._model = model

    def limit(self, limit):
        return self._ret_val[:limit]


class MockAll:
    _ret_val = None

    def __init__(self, model):
        self._model = model

    def count(self):
        return len(self._ret_val)


class MockQuery:
    _ret_val = None
    filter = MockFilter

    def __init__(self, model):
        self._model = model

    def all(self):
        return [self._ret_val]

    def get(self, id):
        return self._ret_val

    def update(self, condition):
        return self.condition

    def count(self):
        return len(self._ret_val)


class MockSession:
    query = MockQuery

    def close(self):
        pass

    def add(self, object):
        pass


class MockDeeptracyDBEngine:

    engine = None
    Base = None
    Session = MockSession
    created_session = None
