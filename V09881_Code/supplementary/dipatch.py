class View:
    http_method_names = [u'get', u'post', u'put', u'patch', u'delete', u'head',
                         u'options', u'trace']

    '''
        View.as_view()
    '''
    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(),
                              self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
