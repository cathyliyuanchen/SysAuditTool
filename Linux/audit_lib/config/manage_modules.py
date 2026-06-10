#!/usr/bin/env python
# -*- coding: utf-8 -*-

from audit_lib.config.soft_import_module import soft_import
# browsers
from audit_lib.softwares.browsers.firefox_browsers import firefox_browsers
from audit_lib.softwares.browsers.chromium_browsers import chromium_browsers

# mails
from audit_lib.softwares.mails.thunderbird_mails import thunderbird_mails

try:
    from audit_lib.softwares.memory.memorydump import MemoryDump
except ImportError:
    pass


def get_categories():
    category = {
        'chats': {'help': 'Chat clients supported'},
        'sysadmin': {'help': 'SCP/SSH/FTP/FTPS clients supported'},
        'databases': {'help': 'SQL clients supported'},
        'mails': {'help': 'Email clients supported'},
        'memory': {'help': 'Retrieve passwords from memory'},
        'wifi': {'help': 'Wifi'},
        'browsers': {'help': 'Web browsers supported'},
        'wallet': {'help': 'Windows credentials (credential manager, etc.)'},
        'git': {'help': 'GIT clients supported'},
        'unused': {'help': 'This modules could not be used because of broken dependence'}
    }
    return category


def get_modules_names():
    return [
        ("audit_lib.softwares.mails.clawsmail", "ClawsMail"),
        ("audit_lib.softwares.databases.dbvis", "DbVisualizer"),
        ("audit_lib.softwares.sysadmin.env_variable", "Env_variable"),
        ("audit_lib.softwares.sysadmin.apachedirectorystudio", "ApacheDirectoryStudio"),
        ("audit_lib.softwares.sysadmin.filezilla", "Filezilla"),
        ("audit_lib.softwares.sysadmin.fstab", "Fstab"),
        ("audit_lib.softwares.browsers.opera", "Opera"),
        ("audit_lib.softwares.chats.pidgin", "Pidgin"),
        ("audit_lib.softwares.chats.psi", "PSI"),
        ("audit_lib.softwares.sysadmin.shadow", "Shadow"),
        ("audit_lib.softwares.sysadmin.aws", "Aws"),
        ("audit_lib.softwares.sysadmin.docker", "Docker"),
        ("audit_lib.softwares.sysadmin.rclone", "Rclone"),
        ("audit_lib.softwares.sysadmin.ssh", "Ssh"),
        ("audit_lib.softwares.sysadmin.cli", "Cli"),
        ("audit_lib.softwares.sysadmin.gftp", "gFTP"),
        ("audit_lib.softwares.sysadmin.keepassconfig", "KeePassConfig"),
        ("audit_lib.softwares.sysadmin.grub", "Grub"),
        ("audit_lib.softwares.databases.sqldeveloper", "SQLDeveloper"),
        ("audit_lib.softwares.databases.squirrel", "Squirrel"),
        ("audit_lib.softwares.wifi.wifi", "Wifi"),
        ("audit_lib.softwares.wifi.wpa_supplicant", "Wpa_supplicant"),
        ("audit_lib.softwares.wallet.kde", "Kde"),
        ("audit_lib.softwares.wallet.libsecret", "Libsecret"),
        ("audit_lib.softwares.memory.mimipy", "Mimipy"),
        ("audit_lib.softwares.git.gitforlinux", "GitForLinux")
    ]

    # very long to execute
    # try:
    # 	module_names.append(MemoryDump())
    # except:
    # 	pass


def get_modules():
    modules = [soft_import(package_name, module_name)() for package_name, module_name in get_modules_names()]
    return modules + chromium_browsers + firefox_browsers + thunderbird_mails
