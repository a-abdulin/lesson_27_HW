import json

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ads.models import ADS, Categories


def home_page(request):
    responce = {
        "text": "Ok",
        "status": 200,
    }
    return JsonResponse(responce, json_dumps_params={'ensure_ascii': False})

@method_decorator(csrf_exempt, name='dispatch')
class Ads(View):
    def get(self, request):
        ads = ADS.objects.all()

        response = []
        for row in ads:
            response.append({
                "id": row.id,
                "name": row.name,
                "author": row.author,
                "price": row.price,
                "description": row.description,
                "address": row.address,
                "is_published": row.is_published
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        new_ad = json.loads(request.body)

        ad =ADS()
        ad.name = new_ad["name"]
        ad.author = new_ad["author"]
        ad.price = new_ad["price"]
        ad.description = new_ad["description"]
        ad.address = new_ad["address"]
        ad.is_published = new_ad["is_published"]

        try:
            ad.full_clean()
        except ValidationError as e:
            return JsonResponse(e.message_dict, status=422)

        ad.save()

        response = {
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
             "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        }

        return JsonResponse(response, safe=False)


class AdEntityView(View):
    def get(self, request, id):
        ad = get_object_or_404(ADS, id=id)

        response = {
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
             "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published
        }
        return JsonResponse(response, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class Cat(View):
    def get(self, request):
        cats = Categories.objects.all()

        response = []
        for row in cats:
            response.append({
                "id": row.id,
                "name": row.name,
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)
        new_cat = Categories.objects.create(**cat_data)

        response = {
            "id": new_cat.id,
            "name": new_cat.name,
        }

        return JsonResponse(response, safe=False)

class CatEntityView(View):
    def get(self, request, id):
        cat = get_object_or_404(Categories, id=id)

        response = {
            "id": cat.id,
            "name": cat.name,
        }
        return JsonResponse(response, safe=False)
