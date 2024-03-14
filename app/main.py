from typing import TypeVar

from fastapi import FastAPI
from fastapi_xml import XmlAppResponse, XmlRoute, add_openapi_extension, XmlBody
from pydantic import BaseModel
import patch_fastapi_xml

from views import router as api_router

T = TypeVar("T", bound=BaseModel)

app = FastAPI(title="FastAPI::XML", default_response_class=XmlAppResponse)
app.include_router(api_router)

app.router.route_class = XmlRoute

add_openapi_extension(app)


