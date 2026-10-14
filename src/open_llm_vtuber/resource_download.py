"""HTTP downloads for the shared learning-resource library."""

import os

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse


def create_resource_router(resource_dir: str = "demo_resources/public") -> APIRouter:
    """Create the public resource-download routes."""
    router = APIRouter(prefix="/resources", tags=["Learning resources"])

    @router.get("/download", response_class=FileResponse)
    async def download_resource(filename: str = Query(min_length=1)) -> FileResponse:
        """Return a named file from the public resource library."""
        file_path = os.path.join(resource_dir, filename)
        if not os.path.isfile(file_path):
            raise HTTPException(status_code=404, detail="Resource not found")
        return FileResponse(file_path, media_type="text/plain")

    return router
