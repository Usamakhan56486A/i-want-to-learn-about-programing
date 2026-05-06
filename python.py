class Document:
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def update(self):
        print(f"Document '{self.title}' updated!")

class Mk:
    def __init__(self):
        self.documents = []
    
    def add_documents(self, doc):
        self.documents.append(doc)

    def do_get(self, idx):        
        return self.documents[idx]

# Example usage
mk = Mk()
doc1 = Document("Usama", "My Book")
mk.add_documents(doc1)

print(mk.do_get(0))   # Output: My Book
# mk.do_get(0).update()       # Output: Document 'My Book' updated!
