from fastapi import  FastAPI ,Request
import logging 

async def middle_ware_process(request:Request , call_next):
        logging.info("Middleware is use")
        repsonse = await call_next(request)
        return repsonse    
