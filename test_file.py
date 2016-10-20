class SingletonMeta(type):
    def __init__(cls, name, bases, dict):
        super(SingletonMeta, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(self, *args, **kw):
        if self.instance is None:
            self.instance = super(SingletonMeta, self).__call__(*args, **kw)
        return self.instance

    def __getattr__(cls, name):
        return getattr(cls(), name)

class Foo(object):
    __metaclass__ = SingletonMeta

    def __init__(self,name):
        print 'RUN RUN RUN RUN'
        self.name = name
        self.call = None
