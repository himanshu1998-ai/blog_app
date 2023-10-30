from fastapi import FastAPI
import uvicorn
from blog.entrypoint.routers import blog_route, user_route

app = FastAPI()

app.include_router(blog_route.router)
app.include_router(user_route.router)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5005)
