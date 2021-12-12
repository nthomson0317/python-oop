mylist = [1,2,3]
len(mylist)
#=>3

class Book():

    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book object has been deleted")

b = Book('Python Rocks', 'Jose', 200)

print(b)
#==> Python Rocks by Jose

len(b)
#==> 200

del b#==> deletes b from memory in your computer
#==> A book object has been deleted

b
#==> name 'b' is not defined