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

from sqlalchemy import Column, String, Float, Sequence, ForeignKey
from sqlalchemy.orm import relationship

from deeptracy_core.dal.database import Base

TABLE_ID = Sequence('table_id_seq', start=1)


class ScanVulnerability(Base):
    """SQLAlchemy ScanVulnerability model"""
    __tablename__ = 'scan_vulnerability'

    id = Column(String, TABLE_ID, primary_key=True, server_default=TABLE_ID.next_value())
    scan_id = Column(String, ForeignKey('scan.id'), nullable=False)
    lang = Column(String, nullable=False)
    cpe = Column(String, nullable=False)
    max_score = Column(Float, default=0)
    scan_dep_id = Column(String, ForeignKey('scan_dep.id'), nullable=False)

    scan = relationship('Scan', lazy='subquery')
    scan_dep = relationship('ScanDep', lazy='subquery')

    def to_dict(self):
        return {
            'id': self.id,
            'scan_id': self.scan_id,
            'lang': self.lang,
            'cpe': self.cpe,
            'max_score': self.max_score,
            'scan_dep_id': self.scan_dep_id
        }
