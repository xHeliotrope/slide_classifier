import hashlib
import io

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
import openslide
from openslide import deepzoom


class HomeView(View):
    """Render order confirmation data and associated tools.
    """

    template_name = "index.html"

    def get(self, request, word=None):
        hashable = "Hellow Werld"
        if word:
            hashable = word
        unique_hash = hashlib.md5(hashable.encode("utf-8")).hexdigest()
        ctx = {
            "stuff": [
                {"name": "Hellow", "value": "Werld"},
                {"name": "hashed hellow werld", "value": unique_hash},
            ]
        }
        return render(request, self.template_name, ctx)


def compute_hash(name):
    """Compute the MD5 hash of a file, returned as a hexstring
    # lifted from (https://github.com/SBU-BMI/quip_slide_metadata/blob/master/image_metadata.py)
    """
    hash_md5 = hashlib.md5()
    # curious if this will work on large files
    with open(name, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


class SlideView(View):
    """Get data about a particular slide
    """

    template_name = "slide.html"

    DEEPZOOM_SLIDE = None
    DEEPZOOM_FORMAT = "jpeg"
    DEEPZOOM_TILE_SIZE = 254
    DEEPZOOM_OVERLAP = 1
    DEEPZOOM_LIMIT_BOUNDS = True
    DEEPZOOM_TILE_QUALITY = 75
    SLIDE_NAME = "slide"

    def get(self, request, word=None):
        filename = "images/sample.svs"
        slide_hash = compute_hash(filename)
        try:
            img = openslide.OpenSlide(filename)
        except openslide.OpenSlideUnsupportedFormatError as exc:
            print(exc)
        except openslide.OpenSlideError as exc:
            print(exc)
        except Exception as exc:
            print(exc)

        img_type = type(img)
        context = {
            "slide_hash": slide_hash,
            "slide_img": img,
            "slide_type": img_type,
        }
        return render(request, self.template_name, context)


class SlideDataView(View):
    """Streaming slide data
    """

    def get(self, request):
        """
        """
        filename = "images/sample.svs"
        slide = openslide.OpenSlide(filename)
        #zoomies = deepzoom.DeepZoomGenerator(slide)
        buff = io.BytesIO()
        slide.save(buff, 'jpeg', 75)

        response = HttpResponse(buff.get_value(), content_type="image/jpeg")
        # slide.save(response, "JPEG")
        return response


class SlideImageView(View):
    """Streaming slide data
    """

    def get(self, request):
        """
        """
        filename = "images/sample.svs"
        slide = openslide.OpenSlide(filename)
        #zoomies = deepzoom.DeepZoomGenerator(slide)
        buff = io.BytesIO()
        slide.save(buff, 'jpeg', 75)

        response = HttpResponse(buff.get_value(), content_type="image/jpeg")
        # slide.save(response, "JPEG")
        return response
