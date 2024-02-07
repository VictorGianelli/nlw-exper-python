from src.controllers.tag_creator_controller import TagCreatorController
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreatorView:

  def validate_and_create(self,http_request: HttpRequest) -> HttpResponse:
    body = http_request.body
    product_code = body['product_code']
    tag_type = 'barcode' # barcode
    if 'tag_type' in body:
      tag_type = body['tag_type'] # barcode or qrcode

    tag_creator_controller = TagCreatorController()
    formatted_response = tag_creator_controller.create(product_code, tag_type)

    return HttpResponse(status_code=200, body=formatted_response)