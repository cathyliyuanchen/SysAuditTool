# Browsers
from audit_lib.config.soft_import_module import soft_import
from audit_lib.softwares.browsers.chromium_browsers import chromium_browsers
from audit_lib.softwares.browsers.firefox_browsers import firefox_browsers

# mails
from audit_lib.softwares.mails.thunderbird_mails import thunderbird_mails


def get_modules_names():
    return [
        ("audit_lib.softwares.browsers.ie", "IE"),
        ("audit_lib.softwares.browsers.ucbrowser", "UCBrowser"),
# Chats
        ("audit_lib.softwares.chats.pidgin", "Pidgin"),
        ("audit_lib.softwares.chats.psi", "PSI"),
        ("audit_lib.softwares.chats.skype", "Skype"),
# Databases
        ("audit_lib.softwares.databases.dbvis", "Dbvisualizer"),
        ("audit_lib.softwares.databases.postgresql", "PostgreSQL"),
        ("audit_lib.softwares.databases.robomongo", "Robomongo"),
        ("audit_lib.softwares.databases.sqldeveloper", "SQLDeveloper"),
        ("audit_lib.softwares.databases.squirrel", "Squirrel"),
# Games
        ("audit_lib.softwares.games.galconfusion", "GalconFusion"),
        ("audit_lib.softwares.games.kalypsomedia", "KalypsoMedia"),
        ("audit_lib.softwares.games.roguestale", "RoguesTale"),
        ("audit_lib.softwares.games.turba", "Turba"),
# Git
        ("audit_lib.softwares.git.gitforwindows", "GitForWindows"),
# Mails
        ("audit_lib.softwares.mails.outlook", "Outlook"),
# Maven
        ("audit_lib.softwares.maven.mavenrepositories", "MavenRepositories"),
# Memory
        ("audit_lib.softwares.memory.keepass", "Keepass"),
        ("audit_lib.softwares.memory.memorydump", "MemoryDump"),
        ("audit_lib.softwares.memory.onepassword", "OnePassword"),
# Multimedia
        ("audit_lib.softwares.multimedia.eyecon", "EyeCON"),
# Php
        ("audit_lib.softwares.php.composer", "Composer"),
# Svn
        ("audit_lib.softwares.svn.tortoise", "Tortoise"),
# Sysadmin
        ("audit_lib.softwares.sysadmin.apachedirectorystudio", "ApacheDirectoryStudio"),
        ("audit_lib.softwares.sysadmin.coreftp", "CoreFTP"),
        ("audit_lib.softwares.sysadmin.cyberduck", "Cyberduck"),
        ("audit_lib.softwares.sysadmin.filezilla", "Filezilla"),
        ("audit_lib.softwares.sysadmin.filezillaserver", "FilezillaServer"),
        ("audit_lib.softwares.sysadmin.ftpnavigator", "FtpNavigator"),
        ("audit_lib.softwares.sysadmin.opensshforwindows", "OpenSSHForWindows"),
        ("audit_lib.softwares.sysadmin.openvpn", "OpenVPN"),
        ("audit_lib.softwares.sysadmin.iiscentralcertp", "IISCentralCertP"),
        ("audit_lib.softwares.sysadmin.keepassconfig", "KeePassConfig"),
        ("audit_lib.softwares.sysadmin.iisapppool", "IISAppPool"),
        ("audit_lib.softwares.sysadmin.puttycm", "Puttycm"),
        ("audit_lib.softwares.sysadmin.rclone", "Rclone"),
        ("audit_lib.softwares.sysadmin.rdpmanager", "RDPManager"),
        ("audit_lib.softwares.sysadmin.unattended", "Unattended"),
        ("audit_lib.softwares.sysadmin.vnc", "Vnc"),
        ("audit_lib.softwares.sysadmin.winscp", "WinSCP"),
        ("audit_lib.softwares.sysadmin.wsl", "Wsl"),
        ("audit_lib.softwares.sysadmin.mRemoteNG", "mRemoteNG"),
# Wifi
        ("audit_lib.softwares.wifi.wifi", "Wifi"),
# Windows
        ("audit_lib.softwares.windows.autologon", "Autologon"),
        ("audit_lib.softwares.windows.cachedump", "Cachedump"),
        ("audit_lib.softwares.windows.credman", "Credman"),
        ("audit_lib.softwares.windows.credfiles", "CredFiles"),
        ("audit_lib.softwares.windows.hashdump", "Hashdump"),
        ("audit_lib.softwares.windows.ppypykatz", "Pypykatz"),
        ("audit_lib.softwares.windows.lsa_secrets", "LSASecrets"),
        ("audit_lib.softwares.windows.vault", "Vault"),
        ("audit_lib.softwares.windows.vaultfiles", "VaultFiles"),
        ("audit_lib.softwares.windows.windows", "WindowsPassword")
    ]


def get_categories():
    category = {
        'browsers': {'help': 'Web browsers supported'},
        'chats': {'help': 'Chat clients supported'},
        'databases': {'help': 'SQL/NoSQL clients supported'},
        'games': {'help': 'Games etc.'},
        'git': {'help': 'GIT clients supported'},
        'mails': {'help': 'Email clients supported'},
        'maven': {'help': 'Maven java build tool'},
        'memory': {'help': 'Retrieve passwords from memory'},
        'multimedia': {'help': 'Multimedia applications, etc'},
        'php': {'help': 'PHP build tool'},
        'svn': {'help': 'SVN clients supported'},
        'sysadmin': {'help': 'SCP/SSH/FTP/FTPS clients supported'},
        'windows': {'help': 'Windows credentials (credential manager, etc.)'},
        'wifi': {'help': 'Wifi'},
        'unused': {'help': 'This modules could not be used because of broken dependence'}
    }
    return category




def get_modules():
    modules = [soft_import(package_name, module_name)() for package_name, module_name in get_modules_names()]
    return modules + chromium_browsers + firefox_browsers + thunderbird_mails
