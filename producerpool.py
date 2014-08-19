from multiprocessing.pool import Pool as BasePool


def callback_intercept(args):
    func, args, callback = args
    result = func(args)
    callback(result)
    return result


class Pool(BasePool):
    
    def __init__(self, *args, **kwargs):
        BasePool.__init__(self, *args, **kwargs)
        return

    def map_async(self, func, iterable, chunksize=None, callback=None,
                  error_callback=None, all_callback=None):
        wrapped_iterable = ((func, args, all_callback) for args in iterable)
        return BasePool.map_async(self, callback_intercept, wrapped_iterable,
                                  chunksize, callback, error_callback)
