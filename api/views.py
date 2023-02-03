from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import GlyphUnion, Weapon
from .serializers import GlyphUnionSerializer, WeaponSerializer

# Create your views here.


class WeaponView(APIView):
    def get(self, request):
        weapons = Weapon.objects.all()
        serializer = WeaponSerializer(weapons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WeaponDetailView(APIView):
    def get_object(self, name):
        try:
            return Weapon.objects.get(name=name)
        except Weapon.DoesNotExist:
            try:
                return Weapon.objects.get(alias=name)
            except:
                return None

    def get(self, request, name):
        weapon = self.get_object(name)

        if weapon:
            serializer = WeaponSerializer(weapon)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response({"message":"Weapon not found"},status.HTTP_404_NOT_FOUND)


class GlyphUnionView(APIView):
    weapon_list = [
        "Rapier",
        "Sword",
        "Hammer",
        "Sickle",
        "Axe",
        "Lance",
        "Knife",
        "Arrow",
    ]

    def get_weapon(self, name):
        try:
            return Weapon.objects.get(name=name)
        except Weapon.DoesNotExist:
            try:
                return Weapon.objects.get(alias=name)
            except:
                return None

    def get(self, request):
        if request.GET.get("back"):
            if (str(request.GET["back"]).lower().__contains__("dominus")):
                try:
                    slot1 = self.get_weapon(request.GET["slot1"])
                    slot2 = self.get_weapon(request.GET["slot2"])
                    if slot1 == None or slot2 == None:
                        return Response(
                            {"message": "Invalid Combination"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                    union = GlyphUnion.objects.get(slot1=slot1.name, slot2=slot2.name,back="Dominus Agony")
                    serializer = GlyphUnionSerializer(union)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except:
                    try:
                        slot1 = self.get_weapon(request.GET["slot2"])
                        slot2 = self.get_weapon(request.GET["slot1"])
                        
                        if slot1 == None or slot2 == None:
                            return Response(
                                {"message": "Invalid Combination"},
                                status=status.HTTP_400_BAD_REQUEST,
                            )
                        union = GlyphUnion.objects.get(slot1=slot1.name, slot2=slot2.name,back="Dominus Agony")
                        serializer = GlyphUnionSerializer(union)
                        return Response(serializer.data, status=status.HTTP_200_OK)
                    except:
                        return Response(
                            {"message": "Invalid Combination. Pulsus."},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

        if request.GET:
            try:
                slot1 = self.get_weapon(request.GET["slot1"])
                slot2 = self.get_weapon(request.GET["slot2"])
                if slot1 == None or slot2 == None:
                    return Response(
                        {"message": "Invalid Combination. Pulsus."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                union = GlyphUnion.objects.get(slot1=slot1.type, slot2=slot2.type)
                serializer = GlyphUnionSerializer(union)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except:
                try:
                    slot1 = self.get_weapon(request.GET["slot2"])
                    slot2 = self.get_weapon(request.GET["slot1"])
                    union = GlyphUnion.objects.get(slot1=slot1.type, slot2=slot2.type)
                    serializer = GlyphUnionSerializer(union)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except:
                    try:
                        if self.get_weapon(request.GET["slot1"]).type in self.weapon_list:
                            slot1= "Weapon"
                        else:
                            slot1 = self.get_weapon(request.GET["slot1"]).type
                        
                        if self.get_weapon(request.GET["slot2"]).type in self.weapon_list:
                            slot2= "Weapon"
                        else:
                            slot2 = self.get_weapon(request.GET["slot2"]).type

                        union = GlyphUnion.objects.get(slot1=slot1, slot2=slot2)
                        serializer = GlyphUnionSerializer(union)
                        return Response(serializer.data, status=status.HTTP_200_OK)



                    except:

                        try:
                            if self.get_weapon(request.GET["slot2"]).type in self.weapon_list:
                                slot1= "Weapon"
                            else:
                                slot1 = self.get_weapon(request.GET["slot2"]).type
                            
                            if self.get_weapon(request.GET["slot1"]).type in self.weapon_list:
                                slot2= "Weapon"
                            else:
                                slot2 = self.get_weapon(request.GET["slot1"]).type

                            union = GlyphUnion.objects.get(slot1=slot1, slot2=slot2)
                            serializer = GlyphUnionSerializer(union)
                            return Response(serializer.data, status=status.HTTP_200_OK)
                        except:
                            return Response({"message": "Invalid Combination. Pulsus."}, status=status.HTTP_400_BAD_REQUEST)
                    
                   
        else:
            union = GlyphUnion.objects.all()
            serializer = GlyphUnionSerializer(union, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)


class GlyphUnionDetailView(APIView):
    def get_object(self, name):
        try:
            return GlyphUnion.objects.get(name=name)
        except GlyphUnion.DoesNotExist:
            try:
                return GlyphUnion.objects.get(alias=name)
            except:
                return None

    def get(self, request, name):
        union = self.get_object(name)

        if union:
            serializer = GlyphUnionSerializer(union)
            return Response(serializer.data, status.HTTP_200_OK)
        else:
            return Response(
                {"Message": "Glyph Union Not Found"}, status.HTTP_404_NOT_FOUND
            )
