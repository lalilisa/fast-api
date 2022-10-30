from typing import List, Union

from pydantic import BaseModel

#DTO
class CreateAccountDto(BaseModel):
    username: str
    password:str


class AudioGenerated(BaseModel):
    hashcode: str
    inputText: str
    audioNameOutput: str
    length: int
    words: int
    outputPathAudio:str 


class idAudioGenerated(BaseModel):
    id:int



