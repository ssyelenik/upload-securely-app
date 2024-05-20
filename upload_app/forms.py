# django_app/forms.py
from django import forms
from .models import Photo
import cloudinary.uploader
from cloudinary import CloudinaryImage

class PhotoForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Photo
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].widget = forms.FileInput(attrs={'accept': 'image/*'})

    def save(self, commit=True):
        instance = super(PhotoForm, self).save(commit=False)
        image = self.cleaned_data.get('image')
        if image:
            # Upload image to Cloudinary with transformation
            result = cloudinary.uploader.upload(image, moderation = "perception_point|aws_rek")
            if result['moderation'][0].get('status') != 'approved':
                return None
            instance.image = result['secure_url']
            transformed_url = CloudinaryImage(result['public_id']).build_url(quality='auto', width=600, height=00, crop='pad', background='gen_fill:ignore-foreground_true')
            instance.transformed_image = transformed_url
            instance.save()
        return instance