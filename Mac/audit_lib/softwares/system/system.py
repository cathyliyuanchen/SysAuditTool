# -*- coding: utf-8 -*- 
# !/usr/bin/python

from audit_lib.config.module_info import ModuleInfo
from audit_lib.config.constant import constant


class System(ModuleInfo):
    def __init__(self):
        ModuleInfo.__init__(self, 'system', 'system')

    def run(self):
        pwd_found = []
        pwd_found += constant.keychains_pwd
        pwd_found += constant.system_pwd

        return pwd_found
