import unittest

from app.core.ioc_container import IocContainer, get_ioc_container_instance, ioc_container


class TestIocContainer(unittest.TestCase):
    def setUp(self):
        self.container = IocContainer()

    def test_register_and_resolve(self):
        service = object()
        self.container.register("my_service", service)

        self.assertIs(self.container.resolve("my_service"), service)

    def test_get_ioc_container_instance_returns_singleton(self):
        self.assertIs(get_ioc_container_instance(), ioc_container)
