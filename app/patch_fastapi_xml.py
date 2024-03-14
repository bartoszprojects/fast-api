from xml.etree.ElementTree import ParseError

from pydantic_core._pydantic_core import ValidationError
from typing import Any
from typing import Dict
from typing import Optional

from fastapi._compat import ModelField
from starlette.requests import Request

from fastapi_xml.decoder import XmlDecoder, BodyDecodeError
from fastapi_xml.response import XmlResponse

from starlette.exceptions import HTTPException as StarletteHTTPException

# to dostaje body (Device) i wrzuca do modedlu pydantica. normalnie nie dziala basexmlmodel bo fastapi-xml obsluguje tylko dataklasy a nie obsluguuje pydantica

def xml_decode(request: Request, model_field: ModelField, body: bytes) -> Optional[Dict[str, Any]]:
    clazz = model_field.type_

    try:
        result: object = clazz.from_xml(body)
    except ValidationError as e:
        raise BodyDecodeError(str(e)) from e
    except ParseError as e:
        raise BodyDecodeError(str(e)) from e
    else:
        return result


def xml_encode(slf, content: Any) -> bytes:
    return content.to_xml()


XmlDecoder.decode = xml_decode
XmlResponse.render = xml_encode
