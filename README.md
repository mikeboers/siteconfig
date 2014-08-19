siteconfig
==========

Out-of-band configuration for Python processes.

This is generally designed to hold per-venv configuration, such as credentials and settings for connecting to servers.


Config Files
------------

By default, we look within `$SITECONFIG` for `*.py` files (to execute as Python) or `*.js` files. All files found are loaded into a common namespace, and availible on the `siteconfig` package, or within the `siteconfig.config` dict.

Environment variables with a `SITECONFIG_` prefix will be pulled in as well.


On Uppercase
------------

Configuration keys **MUST** be uppercase. This is so that (1) there is a trivial seperation bettween variables used for control flow or intermediate values during Python execution, and (2) because they read more like constants.


API
---

From Python, all configuration is availible as attributes on the top-level `siteconfig` package, or within the `siteconfig.config` object.

From the shell, a `siteconfig` command is provided to output requested data. E.g.:

~~~bash


$ siteconfig --list
ALICE_HOST = 'alice.com'
ALICE_USERNAME = 'alice'
ALICE_PASSWORD = 'apass'
ALICE_PORT = 1234

$ siteconfig ALICE_HOST
alice.com

# Keys are case and symbol insensitive from the shell:
$ siteconfig alice.host
alice.com

$ siteconfig --basic-auth ALICE
alice:apass

$ siteconfig --host-string ALICE
alice:apass@alice.com:1234

$ siteconfig --host-string --no-password ALICE
alice@alice.com:1234

~~~
