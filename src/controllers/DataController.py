from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseStatus

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

