class SingletonB:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


class Singleton:
    instance = None
    singleton_b = None

    def __new__(cls, singleton_b: SingletonB):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.singleton_b = singleton_b
        return cls.instance
