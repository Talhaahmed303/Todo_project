from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

# GET + POST
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

# UPDATE + DELETE
@api_view(['PUT', 'DELETE'])
def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif request.method == 'DELETE':
        todo.delete()
        return Response({"message": "Deleted"})