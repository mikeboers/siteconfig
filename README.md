ficonfig
========

Out-of-band configuration for Fluent Image processes.

This is generally designed to hold per-show configuration, such as credentials and settings for connecting to vendors.


Config Files
------------

By default, we look within `~offload/fidata` for `*.py` files (to execute as Python) or `*.js` files. All files found are loaded into a common namespace, and availible on the `ficonfig` package, or within the `ficonfig.config` dict.


On Uppercase
------------

Configuration keys **MUST** be uppercase. This is so that (1) there is a trivial seperation bettween variables used for control flow or intervedia values during Python execution, and (2) because they read more like constants.


API
---

From Python, all configuration is availible as attributes on the top-level `ficonfig` package, or within the `ficonfig.config` object.

From the shell, a `ficonfig` command is provided to output requested data. E.g.:

~~~bash

$ ficonfig --help
usage: ficonfig [-h] {get,list,host-string} ...

positional arguments:
  {get,list,host-string}
                        sub-command help
    get                 lookup a single key
    list                list all key-value pairs
    host-string         construct user@host:port from a base

optional arguments:
  -h, --help            show this help message and exit


$ ficonfig list
ALICE_HOST = 'alice.com'
ALICE_USERNAME = 'alice'
ALICE_PASSWORD = 'apass'
ALICE_PORT = 1234

$ ficonfig get ALICE_HOST
alice.com

$ ficonfig host-string ALICE
alice:apass@alice.com:1234

$ ficonfig host-string --no-password ALICE
alice@alice.com:1234

~~~
