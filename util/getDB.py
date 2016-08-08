# -*- coding: utf-8 -*-
__author__ = 'Shang'

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class dbutil:
    def __init__(self):
        engine = create_engine('mysql://root:@localhost:3306/rong360')
        DBSession = sessionmaker(bind = engine)
        self.session = DBSession()

    def get_session(self):
        return self.session
