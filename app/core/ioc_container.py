class IocContainer:
    def __init__(self):
        self._instance_pool = {}

    def register(self, name, instance):
        if name in self._instance_pool:
            raise ValueError("This service is already registered")

        self._instance_pool[name] = instance

    def resolve(self, name):
        if name not in self._instance_pool:
            raise ValueError("This service is not registered.")

        return self._instance_pool[name]


ioc_container = IocContainer()


def get_ioc_container_instance():
    return ioc_container
