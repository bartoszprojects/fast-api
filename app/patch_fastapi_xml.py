from xml.etree.ElementTree import ParseError

from pydantic_core._pydantic_core import ValidationError
from typing import Any
from typing import Dict
from typing import Optional

from fastapi._compat import ModelField
from starlette.requests import Request

from fastapi_xml.decoder import XmlDecoder, BodyDecodeError
from fastapi_xml.response import XmlResponse


# To work with FASTAPI & PYDANTIC & XML - I am using fastapi_xml library
# ... but this library converts XML to DataClass. Then it not works with Pydantic Schemas. To avoid keeping
# DataClasses and Pydantic Schemas together - I reworked fastapi_xml.decode method to make XML -> PYDANTIC SCHEMA

def xml_decode(request: Request, model_field: ModelField, body: bytes) -> Optional[Dict[str, Any]]:
    # here I am changing the original fastapi_xml lib method that works with DataClasses to my pydanticSchema from endpoints
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
