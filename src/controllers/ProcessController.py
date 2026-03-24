from .BaseController import BaseController
from  .ProjectController import ProjectController
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from models import ProcessingEnums

import os


class ProcessController(BaseController):
    def __init__(self, project_id: str):
        super().__init__()
        self.project_id = project_id
        self.project_path = ProjectController().get_project_path(project_id=project_id)
    def get_file_extention(self, file_id: str):
        return os.path.splitext(file_id)[-1]

    def get_file_loader(self, file_id: str):
        file_extention = self.get_file_extention(file_id)

        file_path = os.path.join(self.project_path, file_id)
        if file_extention == ProcessingEnums.TXT.value:
            return TextLoader(file_path , "utf-8")
        elif file_extention == ProcessingEnums.PDF.value:
            return PyPDFLoader(file_path)
        else:
            raise ValueError("File extension not supported")

    def get_file_content(self, file_id: str):
        loader = self.get_file_loader(file_id)
        return loader.load()
    
    def process_file_content(self,file_content: list ,file_id: str, chunk_size: int, chunk_overlap: int):
        # content = self.get_file_content(file_id)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
         chunk_overlap=chunk_overlap,length_function=len,add_start_index=True)

        file_content_text = [rec.page_content for rec in file_content]

        file_content_metadata = [rec.metadata for rec in file_content]

        chunks = text_splitter.create_documents(texts=file_content_text,metadatas=file_content_metadata)
        
        return chunks


        
