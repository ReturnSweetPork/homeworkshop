# workshop 24



```html

```
    
class HelloView(TemplateView):
    http_method_names = ['get']
    template_name = 'intro/hello.html'    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = kwargs.get('name')
        return context

