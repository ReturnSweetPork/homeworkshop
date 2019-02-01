# workshop 20



```html
class Question(models.Model):
    title = models.CharField(max_length = 100)
    content = models.CharField(max_length = 100)
    votes = models.IntergerField
```







{% for choice in question.choice_set.all %}

<li>{{choice.content}}:{{choice.votes}}표</li>

{% endfor %}