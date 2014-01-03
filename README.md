ficonfig
========

Out-of-band configuration for Fluent Image processes.

This is generally designed to hold per-show configuration, such as credentials and settings for connecting to vendors.


Config Files
------------

By default, we look within `~offload/fidata` for `*.py` files (to execute as Python) or `*.js` files. All files found are loaded into a common namespace, and availible on the `ficonfig` package, or within the `ficonfig.config` dict.

Environment variables with a `FICONFIG_` prefix will be pulled in as well.


On Uppercase
------------

Configuration keys **MUST** be uppercase. This is so that (1) there is a trivial seperation bettween variables used for control flow or intermediate values during Python execution, and (2) because they read more like constants.


API
---

From Python, all configuration is availible as attributes on the top-level `ficonfig` package, or within the `ficonfig.config` object.

From the shell, a `ficonfig` command is provided to output requested data. E.g.:

~~~bash


$ ficonfig --list
ALICE_HOST = 'alice.com'
ALICE_USERNAME = 'alice'
ALICE_PASSWORD = 'apass'
ALICE_PORT = 1234

$ ficonfig ALICE_HOST
alice.com

# Keys are case and symbol insensitive from the shell:
$ ficonfig alice.host
alice.com

$ ficonfig --basic-auth ALICE
alice:apass

$ ficonfig --host-string ALICE
alice:apass@alice.com:1234

$ ficonfig --host-string --no-password ALICE
alice@alice.com:1234

~~~
