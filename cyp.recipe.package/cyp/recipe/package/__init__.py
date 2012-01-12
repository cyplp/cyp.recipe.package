# -*- coding: utf-8 -*-
"""Recipe package"""
import platform
import subprocess

linuxInstaller = {'debian' : '/usr/bin/aptitude',
                  'LinuxMint' : '/usr/bin/aptitude',
                  'Ubuntu' : '/usr/bin/aptitude',
                  'Fedora' : '/usr/bin/yum'}

defaultInstallerOptions = {'/usr/bin/aptitude' : ['install'],
                           '/usr/bin/apt-get' : ['install'],
                           '/usr/bin/yum' : ['install'],
                           }
linuxUninstaller = {'debian' : '/usr/bin/aptitude',
                  'LinuxMint' : '/usr/bin/aptitude',
                  'Ubuntu' : '/usr/bin/aptitude',
                  'Fedora' : '/usr/bin/yum'}

defaultUninstallerOptions = {'/usr/bin/aptitude' : ['remove'],
                           '/usr/bin/apt-get' : ['remove'],
                           '/usr/bin/yum' : ['remove'],
                           }

class Recipe(object):
    """zc.buildout recipe"""

    def __init__(self, buildout, name, options):
        self.buildout, self.name, self.options = buildout, name, options

    def install(self):
        """Installer"""
        # XXX Implement recipe functionality here

        sudo = self._getSudo()

        installer = self._getInstaller()
        installOptions = self._getInstallOptions()
        packages = self.options['packages'].split()

        args = []

        if sudo:
            args.extend(['sudo'])

        args.extend([installer])
        args.extend(installOptions)
        args.extend(packages)
        print args
        subprocess.call(args,
                        stdin=subprocess.PIPE,
                        stderr=subprocess.STDOUT,
                        shell=True)
        # Return files that were created by the recipe. The buildout
        # will remove all returned files upon reinstall.
        return tuple()

    def update(self):
        """Updater"""
        pass

    def _getInstaller(self):
        """
        Return the string path to the installer
        """
        if "installer" in self.options:
            return self.options["installer"]

        if platform.system() == 'Linux':
            return linuxInstaller[platform.linux_distribution()[0]]
        # TODO other os and distribution.

    def _getUninstaller(self):
        """
        Return the string path to the uninstaller
        """
        if "uninstaller" in self.options:
            return self.options["uninstaller"]

        if platform.system() == 'Linux':
            return linuxInstaller[platform.linux_distribution()[0]]
        # TODO other os and distribution.

    def _getInstallOptions(self):
        """
        Return install options.
        """
        if 'install_options' in self.options:
            return self.options['install_options'].split()

        if self._getInstaller() in defaultInstallerOptions:
            return defaultInstallerOptions[self._getInstaller()]
        else:
            raise zc.buildout.UserError('Unkwnonw installer.')

    def _getUninstallOptions(self):
        """
        Return uninstall options.
        """
        if 'uninstall_options' in self.options:
            return self.options['uninstall_options'].split()

        if self._getUninstaller() in defaultUninstallerOptions:
            return defaultUninstallerOptions[self._getInstaller()]
        else:
            raise zc.buildout.UserError('Unkwnonw uninstaller.')

    def uninstall(self):
        """
        Uninstall if needed.
        """
        if 'uninstall' not in self.options:
            return

        if self.options['uninstall'].lower() != 'true':
            return

        sudo = self._getSudo()

    def _getSudo(self):
        """
        Return if sudo is needed.
        """
        sudo = False

        if 'sudo' in self.options:
            if self.options['sudo'].lower() == 'true':
                sudo = True

        return sudo

