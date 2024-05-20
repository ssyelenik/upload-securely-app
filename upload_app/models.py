# upload_app/models.py
from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='images/')
    transformed_image = models.URLField(blank=True, null=True)

# Example of parameterized query (data insertion)
@classmethod
def create_photo(cls, image_path):
    photo = cls(image=image_path) # Creating a new Photo instance with parameterized data
    photo.save() # Saving the instance to the database
    return photo

# Example of data validation (ensuring image size doesn't exceed a certain limit)
def save(self, *args, **kwargs):
    # Check if the image file size is within a specific limit (e.g., 10MB)
    if self.image.size > 10 * 1024 * 1024: # 10MB limit
        raise ValueError("Image size exceeds the maximum allowed limit.")
    super().save(*args, **kwargs) # Call the parent class's save method to save the object to the database
