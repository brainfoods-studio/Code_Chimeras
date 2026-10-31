from fastapi import FastAPI

from reportsapi.routers import inventory, refunds, sales

app = FastAPI(title="Reports API")
app.include_router(sales.router)
app.include_router(refunds.router)
app.include_router(inventory.router)
