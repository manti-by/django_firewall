class DjangoFirewallMiddleware:
    def __init__(self, get_response):
        """One-time configuration and initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """
        Code to be executed for each request before.

        the view (and later middleware) are called.
        :param request: Http request object.
        :return:
        """
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
