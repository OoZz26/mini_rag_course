from enum import Enum
class ResponseStatus(Enum): 
    FILE_TYPE_NOT_SUPPORTED = "FILE_TYPE_NOT_SUPPORTED"
    
    FILE_SIZE_EXCEEDED = "File size exceeds the maximum limit"
    FILE_UPLOAD_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"
    FILE_VALID = "File is valid"
