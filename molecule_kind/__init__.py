try:
    import pkg_resources

    __version__ = pkg_resources.get_distribution('molecule-kind').version
except Exception:  # pragma: no cover
    __version__ = 'unknown'
