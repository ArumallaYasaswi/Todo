from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import  BasicAuthentication 
from rest_framework.permissions import IsAuthenticated

from .InMemoeryStorage import TodoModel
from .serializers import TodoSerializer


class TODOLISTCREATE(APIView):

    """
    DESC: used to LIST, CREATE a todo item.
    """
    authentication_classes = [ BasicAuthentication] # type of authecation used
    permission_classes = [IsAuthenticated] # thype of permission given to access api

    def get(self, request, format=None):
        """ Handles the get request to list all the elements in todos list """
        
        # calling the list method to reterive all items of Todos list using TODOMODEL(), which manages the storage of the Todos list.
        todo=TodoModel().list()
        todoserializer= TodoSerializer(todo, many=True)
        return Response(todoserializer.data)
    
    def post(self, request):
        """Handles the post request to add new elements in todos list """
        
        # verifying `id` field not passed in requested data as `id` field as its is auto-generated field
        if "id" not in request.data:  
            
            # serializing requested data
            serializer=TodoSerializer(data=request.data)
            
            # vaild the request if valid then created new todo item
            if serializer.is_valid(): 
                
                # calling the create method to add a new item to todos list using TODOMODEL(), which manages the storage of the Todos list.
                todo = TodoModel().create(serializer.validated_data)
                
                # returns created details of todo data, and status record successfully created 
                return Response(todo, status=status.HTTP_201_CREATED)
            
            # handling field validation errors in provided todo details    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # handling `id` validation error in  provied todo details
        return Response([{"id":"'ID field cannot be provided'"}], status= status.HTTP_400_BAD_REQUEST)


class TodoGETUpdateDeleteBYIDView(APIView):
    """DESC: used to GET, Update, Delete a todo item."""
    authentication_classes = [ BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        """Reterives to do elemntby matched id
        args (pk:int): `id`of the todo element
        returns: 
                Todo item found return todo item(dict)
                otherwise raises Http404"""
        
        # calling the get_by_id method to retirve items of matched specified id from todos list using TODOMODEL(), 
        # which manages the storage of the Todos list.
        todo = TodoModel().get_by_id(int(pk))
        if todo is None:
            from django.http import Http404
            raise Http404("Todo not found")
        return todo        

    def get(self, request, pk):
        """Handles get request for single todo element"""
        
        # reterives the todo item using spectifed id  details
        todo = self.get_object(pk)
    
        # serializing requested data
        serializer = TodoSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk):
        """Handles put request for single todo element to update details of the todo item"""
        
        # reterives the todo item using spectifed id  details
        todo = self.get_object(pk)

        # verifying `id` field not passed in requested data as `id`(read-only) field cannot be updated
        if "id" in request.data:

            # serializing requested data
            serializer = TodoSerializer(data=request.data)
            if serializer.is_valid():
                
                # calling the update method to update a specific item to todos list using TODOMODEL(), which manages the storage of the Todos list.
                updated_todo = TodoModel().update(todo['id'], serializer.validated_data)
                return Response(updated_todo)
            
            # handling field validation errors in provided todo details    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # handling `id` validation error in  provied todo details
        return Response([{"id":"'ID field cannot be updated.'"}], status= status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        """Handles delete request for single todo element """
        
        # reterives the todo item using spectifed id  details
        todo = self.get_object(pk)

        # calling the delete method to delete a specific item to todos list using TODOMODEL(), which manages the storage of the Todos list.
        if TodoModel().delete(todo['id']): #It returns True if item is deleted otherwise False

            # shows handles the 204 response after deletion of todo item  
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        # handles the 404 if the todo item not matches 
        return Response(status=status.HTTP_404_NOT_FOUND)
