import uuid
import base64
import imghdr
from django.utils.translation import gettext_lazy as _
from django.core.files.base import ContentFile
from rest_framework import serializers
# class Base64ImageField(serializers.ImageField):
#     def from_native(self, data):
#         if isinstance(data, basestring) and data.startswith('data:image'):
#             # base64 encoded image - decode
#             format, imgstr = data.split(';base64,')  # format ~= data:image/X,
#             ext = format.split('/')[-1]  # guess file extension

#             data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

#         return super(Base64ImageField, self).from_native(data)


ALLOWED_IMAGE_TYPES = (
    "jpeg",
    "jpg",
    "png",
    "gif"
)


class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, base64_data):
        # Check if this is a base64 string
        if not base64_data:
            return None

        if isinstance(base64_data, str) and base64_data.startswith('data:image'):
            # Check if the base64 string is in the "data:" format
            if 'data:' in base64_data and ';base64,' in base64_data:
                # Break out the header from the base64 content
                header, base64_data = base64_data.split(';base64,')
                
            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(base64_data)
            except TypeError:
                raise serializers.ValidationError(_("Please upload a valid image."))
            # Generate file name:
            file_name = str(uuid.uuid4())[:12]  # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)
            if file_extension not in ALLOWED_IMAGE_TYPES:
                raise serializers.ValidationError(_("The type of the image couldn't been determined."))
            complete_file_name = file_name + "." + file_extension
            data = ContentFile(decoded_file, name=complete_file_name)
            return super(Base64ImageField, self).to_internal_value(data)
        raise serializers.ValidationError('This is not an base64 string')

    def to_representation(self, value):
        # Return url including domain name.
        return value.name

    def get_file_extension(self, filename, decoded_file):
        extension = imghdr.what(filename, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension
        return extension
