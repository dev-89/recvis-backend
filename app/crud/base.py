from typing import TypeVar

from beanie import Document
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase:
    def __init__(self, model: Document) -> None:
        self.model = model

    async def get(self, id: any) -> Document:
        doc = await self.model.get(id)
        if doc is None:
            raise HTTPException(
                status_code=404, detail="Could not find document in database!"
            )
        return doc

    async def get_multi(
        self, *, skip: int = 0, limit: int = 100
    ) -> list[Document] | None:
        pass

    async def create(self, *, obj_in: CreateSchemaType) -> Document:
        obj_in_data = jsonable_encoder(obj_in)
        new_instance = self.model(**obj_in_data)
        await new_instance.insert()
        return new_instance

    async def update(
        self, *, db_obj: Document, obj_in: UpdateSchemaType | dict[str, any]
    ) -> None:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        await db_obj.set(update_data)

    async def remove(self, id: any) -> Document | None:
        doc = await self.model.get(id)
        await doc.delete()
        return doc
