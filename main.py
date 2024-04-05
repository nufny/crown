from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from crown.fetcher import Fetcher
from crown.models import CreatePrompt, Prompt


def gen_app():
    app = FastAPI()
    app.fetcher: Fetcher = Fetcher()

    favicon_path = "favicon.ico"

    @app.get("/favicon.ico", include_in_schema=False)
    async def favicon():
        return FileResponse(favicon_path)

    @app.get("/prompt/{prompt_id}")
    async def get_prompt(prompt_id) -> Prompt:
        prompt = app.fetcher.fetch_prompt(prompt_id)
        if prompt is None:
            raise HTTPException(status_code=404, detail="Prompt not found")
        return prompt

    @app.post("/prompt/new")
    async def create_prompt(prompt: CreatePrompt):
        return app.fetcher.insert_prompt(prompt)

    return app
