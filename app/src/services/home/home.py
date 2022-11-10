
from src.repository.get import get

def homePageService():

    return_get = get()
    return {"data": None, "message": return_get["details"], "status": True}
    
