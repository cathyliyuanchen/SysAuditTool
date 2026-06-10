from audit_lib.config.module_info import ModuleInfo
from audit_lib.softwares.browsers.mozilla import Mozilla
import os

class Thunderbird(Mozilla):

    def __init__(self):
        self.path = u"~/Library/Thunderbird"
        ModuleInfo.__init__(self, 'Thunderbird', 'mails')
