def mkdir_p(path):
    '''
    Implements ``mkdir -p``.
    '''
    import errno
    import os
    if len(path) > 0:
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST:
                pass
            else: raise

