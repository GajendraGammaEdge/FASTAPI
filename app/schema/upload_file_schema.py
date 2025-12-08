from pydantic import  BaseModel 


class FileBase(BaseModel):
    file_name : str 
    file_path : str
    
class FileCreate(FileBase):
    user_id :int
    
class FileResponse(FileBase): 
    id: int 
    user_id :int
    
    class Config():
        orm_mode= True            