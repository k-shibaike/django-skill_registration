from django import forms
from django.core.exceptions import ValidationError
from hashlib import sha256
from .models import Product, Skill

import time

def image(self):
    image = self.cleaned_data.get('image')
    if image:
        # 1. 画像ファイルの拡張子を確認
        allowed_extensions = ['jpg','jpeg','png']
        file_extension = image.name.lower().split('.')[-1]
        print("file_extension",file_extension)
        if not any(file_extension.endswith(ext) for ext in allowed_extensions):
            raise ValidationError("JPEGまたはPNGフォーマットの画像ファイルをアップロードしてください。")

        # 2. ファイル名をハッシュ化
        time_int = int(time.time())
        hashed_filename = sha256(image.name.encode()).hexdigest()[:10] # ファイル名をハッシュ化して10文字までにする
        image.name = f"{hashed_filename}{str(time_int)}.{file_extension}"

    return image

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "image"]

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # 1. 画像ファイルの拡張子を確認
            allowed_extensions = ['jpg','jpeg','png']
            file_extension = image.name.lower().split('.')[-1]
            print("file_extension",file_extension)
            if not any(file_extension.endswith(ext) for ext in allowed_extensions):
                raise ValidationError("JPEGまたはPNGフォーマットの画像ファイルをアップロードしてください。")

            # 2. ファイル名をハッシュ化
            time_int = int(time.time())
            hashed_filename = sha256(image.name.encode()).hexdigest()[:10] # ファイル名をハッシュ化して10文字までにする
            image.name = f"{hashed_filename}{str(time_int)}.{file_extension}"

        return image


class SkillForm(ProductForm):
    class Meta:
        model = Skill
        fields = ["name", "image"]

        # def clean_image(self):
        #   image = self.cleaned_data.get('image')
        #   if image:
        #       # 1. 画像ファイルの拡張子を確認
        #       allowed_extensions = ['jpg','jpeg','png']
        #       file_extension = image.name.lower().split('.')[-1]
        #       print("file_extension",file_extension)
        #       if not any(file_extension.endswith(ext) for ext in allowed_extensions):
        #           raise ValidationError("JPEGまたはPNGフォーマットの画像ファイルをアップロードしてください。")

        #       # 2. ファイル名をハッシュ化
        #       time_int = int(time.time())
        #       hashed_filename = sha256(image.name.encode()).hexdigest()[:10] # ファイル名をハッシュ化して10文字までにする
        #       image.name = f"{hashed_filename}{str(time_int)}.{file_extension}"

        #   return image
