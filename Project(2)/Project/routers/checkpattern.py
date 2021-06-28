from typing import Dict
from fastapi import APIRouter , HTTPException , Depends , Query
from typefunction import typefunction

router = APIRouter(
    tags=["checkFormat"],
    responses={404: {"message": "Not found"}}
)

@router.post("/checkFormat" , status_code = 200)
async def checkFormat(txt:str,mode:int):
    typefn = typefunction()
    if mode == 1:
        result =  typefn.checkBOOK(txt)
    elif mode == 2:
        result =  typefn.checkARTICLE(txt)
    elif mode == 3:
        result =  typefn.checkJOURNAL(txt)
    elif mode == 4:
        result =  typefn.checkTHESES(txt)
    elif mode == 5:
        result =  typefn.checkELECTRONICS(txt)
    elif mode == 6:
        result =  typefn.checkWIKI(txt)
    elif mode == 7:
        result =  typefn.checkPERIODICAL(txt)
    return result
    
  

    


    