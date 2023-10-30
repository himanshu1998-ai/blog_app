from fastapi import FastAPI
import uvicorn
from ui.entrypoint.routers import ui_router
from fastapi.staticfiles import StaticFiles
import os
app = FastAPI()
CONFIG_PATH = os.path.abspath(os.path.dirname(__file__))

STATIC_PATH = os.path.abspath(os.path.join(CONFIG_PATH, "./static"))

app.include_router(ui_router.router)
app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5006)
