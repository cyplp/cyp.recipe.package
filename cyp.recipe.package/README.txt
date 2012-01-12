.. contents::

Introduction
============

`cyp.recipe.package` is a buildout recipe for installing package from distribution.

Currently `cyp.recipe.package` supports :
 * debian,
 * linux mint,
 * ubuntu.

How to use it
=============

Here a buildout.cfg example :

::

 [buildout]
 parts =
         nginx
 [nginx]
 recipe = cyp.recipe.package
 packages =
         nginx
 sudo = true

Options
=======

`cyp.recipe.package` has several options:

 * packages (required): a list of the needed to install package,
 * sudo (optional): True if sudo is needed (False by default),
 * installer (optional) : if another installer than the default installer is wanted,
 * uninstaller (optional) : if another uninstaller than the default uninstaller is wanted,
 * installer_options  (optional) : list of wanted options,
 * uninstaller_options  (optional) : list of wanted options,
 * uninstall (optional) : True if buildout uninstall must uninstall package.

