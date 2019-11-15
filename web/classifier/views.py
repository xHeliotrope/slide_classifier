import hashlib
import io
import json

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
    def package_metadata(self, img, img_meta):
        """Get metadata for an image
        """
        img_prop = img.properties;
        img_meta["level_count"] = int(img.level_count);
        img_meta["width"]  = img.dimensions[0];
        img_meta["height"] = img.dimensions[1];
        img_meta["objective_power"] = img_prop[openslide.PROPERTY_NAME_OBJECTIVE_POWER];
        img_meta["mpp_x"] = float(img_prop[openslide.PROPERTY_NAME_MPP_X]);
        img_meta["mpp_y"] = float(img_prop[openslide.PROPERTY_NAME_MPP_Y]);
        img_meta["mpp-x"] = float(img_prop[openslide.PROPERTY_NAME_MPP_X]);
        img_meta["mpp-y"] = float(img_prop[openslide.PROPERTY_NAME_MPP_Y]);
        img_meta_prop = {}
        for p in img_prop:
            img_meta_prop[p] = img_prop[p];
        img_meta["properties"] = img_meta_prop;
        return img_meta

    def get(self, request):
        """
        """
        filename = "images/sample.svs"
        slide = openslide.OpenSlide(filename)
        metadata = self.package_metadata(slide, {})
        response = HttpResponse(json.dumps(metadata), content_type="application/json")
        return response


class SlideImageView(View):
    """Streaming slide data
    """
    def get2(self, request, x, y, offset):
        """for Tiling/sampling subsections of a slide
        """
        pass

    def get(self, request):
        """
        """
        filename = "images/sample.svs"
        slide = openslide.OpenSlide(filename)
        print('slide dimensions: ', slide.dimensions)
        my_guy = slide.read_region((1000, 1000), 0, (3000, 3000))
        response = HttpResponse(content_type="image/jpeg")
        my_guy.save(response, format='png')
        return response



class ThumbnailView(View):
    """For retrieving the thumbnail of a slide
    """

    def get_thumbnail(self, request, img_name):
        pass

    def get(self, request)
        """
        """
        return HttpResponse('hi')
