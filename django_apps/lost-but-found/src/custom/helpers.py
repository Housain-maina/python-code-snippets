import os
import uuid


def make_image_file_path(instance, filename):
    """Generate file path for new profile image"""
    ext = filename.split(".")[-1]
    filename = (
        f"{instance.user.first_name}_{instance.user.last_name}-{uuid.uuid4()}.{ext}"
    )
    return os.path.join("uploads/profile/", filename)