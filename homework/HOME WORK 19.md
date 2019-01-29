# HOMEWORK 19

1. csrf 토큰/수정,삭제,등록

2. ```python
   title = request.POST.get('title')
   
   ```

3. ```python
       <form action="/posts/{{post.id}}/update/" method="post">
           {% csrf_token %}
           <input type="text" name="title" value="{{post.title}}"/>
           <input type="text" name="content" value="{{post.content}}"/>
           <input type="submit" value="Submit" />
       </form>
   ```

4. 