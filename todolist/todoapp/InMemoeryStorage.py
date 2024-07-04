import os
import json

class TodoModel:
    """description:Todo model is used to to store todo list data in in memory file
    """

    def __init__(self):
        self.path_of_file = 'todos.json' # Path where we store the data for the to-do list
        self.todos = []        # Initialing empty list to store`todos` items
        self.index_id = 1      # Initialing the `id` value for auto-increment field(read-only)
        self.reterive_data_form_file() # loads data from the file

    def list(self): 
        """ return all elements available in todo list"""
        return self.todos 

    def create(self, data): 
        """ DESCRIPTION: Add new elements to todo list
            ARGS :  data(dict) --contains new todo element data with fields tittle: required,
                                                                          description:optional,
                                                                          completed:default(false)
           Returns (dict): added auto assigns id (auto-incremented) to data dict
        """
        # assigns new id to todo element
        data['id'] = self.index_id  

        # adds the new todo element to the todos list
        self.todos.append(data)

        # Incrementing the index value by one for next todo
        self.index_id += 1

        # storing newly updated todo list , index value
        self.save()
        return data

    def get_by_id(self, todo_id): 
        """ Desc: Reterive the todo element by its id
         args: id of todo for reterival
         returns: if found single todo item otherwise returns None"""
        
        # searchs in todos list of dict for specified id 
        return next((todo for todo in self.todos if todo['id'] == todo_id), None)
    

    def update(self, todo_id, data):  
        """Desc: Updates single todo element of specitfied `id`  
        args: todo_id(pk:int) retrive the todo items if found
              data(dict): data contains field and its values to update previously eixting data
        returns: updated todo element data if specified id matched otherwise returns None
        """
        # find the todo item with specified `id`
        todo = self.get_by_id(todo_id)
        
        # todo if found
        if todo:
            # update the todo item with new data
            todo.update(data)
            
            # svae the updated list with todo in storage
            self.save()
        # returns the updated todo element if found other None
        return todo

    def delete(self, todo_id):
        """Desc: Updates single todo element of specitfied `id`  
        args: todo_id(pk:int) retrive the todo items if found
        returns: updated todo element data if specified id matched otherwise returns None
        """
        # find the todo item with specified `id`
        todo = self.get_by_id(todo_id)
        
        # todo if found
        if todo:
            # removes the matched todo element from todos list 
            self.todos.remove(todo)
            
            # svae the updated list with todo in storage
            self.save()
            
            # Indicated the deletion is successfull
            return True
        
        # Indicated the deletion is unsuccessfull
        return False

    def save(self): 
        """write current values of todo list and index  into the file."""
        with open(self.path_of_file, 'w') as f:
            json.dump({'todos': self.todos, 'index_id': self.index_id}, f)

    def reterive_data_form_file(self): 
        """Read json data current values of todo list and index  from the file."""
        if os.path.exists(self.path_of_file):
            with open(self.path_of_file, 'r') as f:
                data = json.load(f)
                self.todos = data['todos']
                self.index_id = data['index_id']