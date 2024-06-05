from abc import ABC, abstractmethod

class Document(ABC):
    
    def open(self):
        pass
    
    def read(self):
        pass
  
    def save(self):
        pass

class WordDocument(Document):
    def __init__(self, filename, filesize, content):
        self.filename = filename
        self.filesize = filesize
        self.content = content
    
    def open(self):
        print("Opening Word document", self.filename)
    
    def read(self):
        print("Reading Word document content", self.content)
    
    def save(self):
        print("Saving Word document", self.filename)

class PDFDocument(Document):
    def __init__(self, filename, filesize, content):
        self.filename = filename
        self.filesize = filesize
        self.content = content
    
    def open(self):
        print("Opening PDF document", self.filename)
    
    def read(self):
        print("Reading PDF document content", self.content)
    
    def save(self):
        print("Saving PDF document", self.filename)

class ExcelDocument(Document):
    def __init__(self, filename, filesize, content):
        self.filename = filename
        self.filesize = filesize
        self.content = content
    
    def open(self):
        print("Opening Excel document", self.filename)
    
    def read(self):
        print("Reading Excel document content", self.content)
    
    def save(self):
        print("Saving Excel document:", self.filename)

class DocumentFactory:
   
    def create_document(doc_type, filename, filesize, content):
        if doc_type == "Word":
            return WordDocument(filename, filesize, content)

        elif doc_type == "PDF":
            return PDFDocument(filename, filesize, content)

        elif doc_type == "Excel":
            return ExcelDocument(filename, filesize, content)

        else:
            raise ValueError("Invalid document ")

if __name__ == "__main__":
    
    word_doc = DocumentFactory.create_document("Word", "cheat.docx", 2048, "This is a word document.")
    pdf_doc = DocumentFactory.create_document("PDF", "word.pdf", 9969, "This is a PDF document.")
    excel_doc = DocumentFactory.create_document("Excel", "aim.excel", 2004, "This is an excel document.")
    
    word_doc.open()
    word_doc.read()
    word_doc.save()
    
    pdf_doc.open()
    pdf_doc.read()
    pdf_doc.save()
    
    excel_doc.open()
    excel_doc.read()
    excel_doc.save()
