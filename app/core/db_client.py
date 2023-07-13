from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from app.core.config import settings
from app import models


async def init_db():
    print("Connecting to Mongo database")
    client: AsyncIOMotorClient = AsyncIOMotorClient(settings.MONGODB_URL)
    dbname: str = settings.sample_storage_db_service_name
    await init_beanie(
        database=client[dbname],
        document_models=[
            models.collected_documents.CollectedDocuments,
            models.collected_documents.CollectedDocumentOrder,
            models.discipline_weightset.ResearchDisciplineWeightSet,
            models.document.UserDocument,
            models.folder.Folder,
            models.user.User,
            models.weightset.WeightSet,
        ],
    )
