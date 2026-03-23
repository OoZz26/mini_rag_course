import os
from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseStatus
import re

class DataController(BaseController):
        def __init__(self):
            super().__init__()
            
        def validate_file(self, file : UploadFile):
            # Validate file type
            if file.content_type not in self.app_settings.FILE_ALLOWED_EXTENSIONS:
                return False, ResponseStatus.FILE_TYPE_NOT_SUPPORTED.value
            
            # Validate file size
            max_size_bytes = self.app_settings.MAX_FILE_SIZE_MB * 1024 * 1024
            if file.size > max_size_bytes:
                return False, ResponseStatus.FILE_SIZE_EXCEEDED.value
            
            return True, ResponseStatus.FILE_VALID.value
        
        
        def generate_unique_filepath(self, original_filename: str, project_id: str):
          random_key = self.generate_random_string()
          project_path = ProjectController().get_project_path(project_id=project_id)
          
          clean_filename = self.get_clean_file_name(original_filename)
          
          unique_filepath = os.path.join(project_path, random_key + "_" + clean_filename)
          
          while os.path.exists(unique_filepath):
              random_key = self.generate_random_string()
              unique_filepath = os.path.join(project_path, random_key + "_" + clean_filename)
          return unique_filepath , random_key + "_" + clean_filename
          
          
          
          

        def get_clean_file_name(self, filename: str):
            # Remove special characters and spaces from the filename
            clean_name = re.sub(r'[^\w.]', '', filename.strip())
            clean_name = clean_name.replace(" ", "_")  # Replace spaces with underscores
            return clean_name
        
        
        
 