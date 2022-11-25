from pydantic import BaseModel
from typing import List

class Blog(BaseModel):
    title : str
    body : str

    class Config():
        orm_mode = True

class User (BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):

    #we just want name amd email only no id and password

    name:str
    email:str
    blogs : List[Blog] = []

    class Config():
        orm_mode = True

class ShowBlog(BaseModel):

    #we just want title only no id and body

    title : str

    creator : ShowUser

    class Config():
        orm_mode = True