from fastapi import FastAPI

from reportsapi.routes import router

app = FastAPI(title="Reports API")
app.include_router(router)
