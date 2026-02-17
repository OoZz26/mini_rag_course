from .BaseController import BaseController
import os
from fastapi import UploadFile
from models import ResponseStatus

class ProjectController(BaseController):
        def __init__(self):
            super().__init__()
            
        def get_project_path(self, project_id: str):
            Project_dir=  os.path.join(self.file_dir, project_id)
            if not os.path.exists(Project_dir):
                os.makedirs(Project_dir)    
            return Project_dir