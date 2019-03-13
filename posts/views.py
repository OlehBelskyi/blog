from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import posts
from .serializers import *
from .models import Post


@api_view(['GET', 'POST', 'PUT'])
@permission_classes([IsAuthenticated, ])
def user_post(request):

    if request.method == "GET":
        try:
            post = Post.objects.get(title=request.GET.get('title'))
            data = {
                "Title": post.title,
                "Content": post.content,
                "Author": post.author,
                "Likes": post.likes,
                "Unlikes": post.unlikes,
                "date": post.date
            }
            return Response(data, status=status.HTTP_200_OK)
        except posts.models.Post.DoesNotExist:
            data = "Post does not exist"
            return Response(data, status=status.HTTP_404_NOT_FOUND)

    if request.method == "POST":
        post = request.data
        post['user_id'] = request.user.id
        post['author'] = request.user.first_name + ' ' + request.user.last_name
        serializer = PostSerializer(data=post)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            data = "Please post correct data"
            return Response(data, status=status.HTTP_409_CONFLICT)

    if request.method == "PUT":

        post = Post.objects.get(title=request.data['title'])

        if request.data['like'] == 'Like':
            post.likes += 1
            post.save()
            data = "Successful like adding"
        else:
            post.unlikes += 1
            post.save()
            data = "Successful unlike adding"

        return Response(data, status=status.HTTP_200_OK)
