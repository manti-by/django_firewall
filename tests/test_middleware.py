from django_firewall.middleware import DjangoFirewallMiddleware
from requests import Request


class TestMiddleware:
    def setup_method(self):
        self.request = Request()

    def test_middleware_init(self):
        middleware = DjangoFirewallMiddleware(lambda x: x)
        response = middleware(self.request)
        assert response is not None
