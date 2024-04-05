from pydantic import BaseModel, Field


class CreatePrompt(BaseModel):
    title: str = Field(required=True, max_length=256)
    text: str = Field(required=True, max_length=4096)


class Prompt(CreatePrompt):
    model_config = {"from_attributes": True}
    id: int = Field()
