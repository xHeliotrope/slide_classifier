import hashlib
import io
import json
import os
import subprocess

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


class ListSlidesView(View):
    """For the List Files
    """
    def get(self, request):
        images = [img for img in os.listdir('/app/images') if img.endswith('svs')]
        return HttpResponse(json.dumps(images), content_type="application/json")

class SlideThumbnail(View):
    """For gettting the Slide thumbnail
    """
    def get(self, request, image_name):
        """
        """
        filename = f'images/{image_name}'
        # get the slide object
        try:
            img = openslide.OpenSlide(filename)
        except openslide.OpenSlideUnsupportedFormatError as exc:
            print(exc)
        except openslide.OpenSlideError as exc:
            print(exc)
        except Exception as exc:
            print(exc)

        thumbnail = img.get_thumbnail((150, 150))
        response = HttpResponse(content_type="image/jpeg")
        thumbnail.save(response, format='png')
        return response

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
        filename = "images/C3L-00452-41.svs"
        try:
            img = openslide.OpenSlide(filename)
        except openslide.OpenSlideUnsupportedFormatError as exc:
            print(exc)
        except openslide.OpenSlideError as exc:
            print(exc)
        except Exception as exc:
            print(exc)

        context = {
            "levels": 3,
            "slide_img": img,
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
        filename = "images/C3L-00452-41.svs"
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
        filename = "images/C3L-00452-41.svs"
        slide = openslide.OpenSlide(filename)
        default_subsection = slide.read_region((1000, 1000), 0, (3000, 3000))
        response = HttpResponse(content_type="image/jpeg")
        default_subsection.save(response, format='png')
        return response


class SlideSubsectionView(View):
    """For retrieving a subsection of a slide
    """
    def get(self, request, anchor_x, anchor_y, size_x, size_y, level):
        """GET a subsection
        """
        filename = "images/C3L-00452-41.svs"
        slide = openslide.OpenSlide(filename)
        subsection = slide.read_region((anchor_x, anchor_y), level, (size_x, size_y))
        response = HttpResponse(content_type="image/jpeg")
        subsection.save(response, format='png')
        return response


