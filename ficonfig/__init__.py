from .configobj import Config

config = Config.from_environ()

# Add the data and some of the API as attributes of the top-level package.
globals().update(config)
get = config.get

