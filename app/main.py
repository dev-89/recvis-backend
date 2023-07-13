from fastapi import FastAPI
from routers import (
    analysis,
    collected_documents,
    detailed_analysis,
    discipline_weightset,
    document,
    folder,
    user,
    user_info,
)

app = FastAPI()

app.include_router(analysis.router)
app.include_router(collected_documents.router)
app.include_router(detailed_analysis.router)
app.include_router(discipline_weightset.router)
app.include_router(document.router)
app.include_router(folder.router)
app.include_router(user.router)
app.include_router(user_info.router)
