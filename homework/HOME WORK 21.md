# homework 21

1. 

```php+HTML
 {% for comment in question.comment_set.all %}
	<h3>{{comment.content}}<h3>
    {% endfor %}
```

```html
questions/{{question.id}}/comments/create


```

