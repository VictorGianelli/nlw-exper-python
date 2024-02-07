from typing import Dict

from src.drivers.barcode_handler import BarcodeHandler
from src.drivers.qrcode_handler import QrCodeHandler

class TagCreatorController:
    '''
        responsability for implementing business rules
    '''

    def create(self, product_code: str, tag_type: str) -> Dict:
        """ response for the create tag request"""
        if tag_type == 'qrcode':
            path = self.__create_qr(product_code)
        else:
            path = self.__create_tag(product_code)
        formatted_response =self.__format_response(path, tag_type)
        return formatted_response

    def __create_tag(self, product_code: str) -> str:
        """ create the tag using the driver BarCodeHandler """
        barcode_handler = BarcodeHandler()
        path = barcode_handler.create_barcode(product_code)
        return path

    def __create_qr(self, product_code: str) -> str:
        """ create the tag using the driver QrCodeHandler """
        qr_handler = QrCodeHandler()
        path = qr_handler.create_qrcode(product_code)
        return path

    def __format_response(self, path: str, tag_type) -> Dict:
        """ format the response into a Dict """
        return {
            "data": {
                "type": f'{tag_type} tag',
                "count": 1,
                "path": path
            }
        }