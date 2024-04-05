from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from crown.models import Prompt, CreatePrompt
from crown.database.models import Prompt as DBPrompt


class Fetcher:

    def __init__(self):
        self.engine = create_engine("postgresql://postgres@localhost/test", echo=True)

    def fetch_prompt(self, prompt_id: int) -> Optional[Prompt]:
        try:
            with Session(self.engine) as s:
                # results = conn.execute(
                #     text("select * from prompt where prompt.id=:prompt_id"),
                #     {"prompt_id": prompt_id},
                # ).all()
                db_prompt: DBPrompt = s.get_one(DBPrompt, prompt_id)
                return Prompt.model_validate(db_prompt)
        except NoResultFound:
            return None

    def insert_prompt(self, prompt: CreatePrompt) -> int:
        with Session(self.engine) as s:
            db_prompt = DBPrompt(**prompt.dict())
            s.add(db_prompt)
            s.commit()
            return db_prompt.id
