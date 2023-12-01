class SingletonMeta(type):
    """Singleton meta class

    If any class set this class as metaclass, it will be restricted to one-instance class.
    """

    __instance = None

    def __call__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance
