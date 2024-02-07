""" qr code handling class """

import os
from datetime import datetime
import qrcode
from qrcode.image.pure import PyPNGImage

class QrCodeHandler: 
    """ qr code handling class """

    def create_qrcode(self, product_code: str) -> str:
        """ create a qr code tag, save to folder and return tag path """
        # defining a unique datetime to add to the name of the file
        dt = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        qr = qrcode.make(product_code, image_factory=PyPNGImage)
        tag_name = f'{dt}-qrcode.png'

        folder = "tags/"
        # check if the folder exists
        if os.path.isdir(folder) is False:
            # if not, create it
            os.mkdir(folder)

        # adding generated tags to the tags folder
        qr.save(folder + tag_name)

        # return path (folder + tag_name)
        return folder + tag_name