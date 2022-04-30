from ast import Add
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (Leasing_Info_Serializer, Address_Serializer, Unit_Type_Serializer,
Community_Serializer, Unit_Serializer)
from .models import Address, Community, Unit
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from django.http import HttpResponse



def SiteLoadUp(request):
    return render(request, 'index.html')



def unitJson(unit):
    # Time 1:08
    finalJson = {
            "unit" : {
                "id" : unit.id,
                "num_of_bedrooms"  			     : unit.num_of_bedrooms, 
                "num_of_bathrooms" 			     : unit.num_of_bathrooms, 
                "num_of_balcony"	 			 : unit.num_of_balcony,
                "is_available"     			     : unit.is_available,
                "is_reserved" 	 			     : unit.is_reserved,
                "unit_availability_start_date"   : unit.unit_availability_start_date,
                "unit_availability_end_date"     : unit.unit_availability_end_date,
                "unit_description" 			     : unit.unit_description,
                "living_area_sf" 				 : unit.living_area_sf,
                "unit_number" 				     : unit.unit_number,
                "unit_at_floor" 				 : unit.unit_at_floor
                }
            }
    if unit.community_id and unit.community_id.address_id:
        comunityDict =  {
                        "street_address"   : unit.community_id.address_id.street_address,
                        "city" 			   : unit.community_id.address_id.city,
                        "state" 		   : unit.community_id.address_id.state,
                        "county" 		   : unit.community_id.address_id.county,
                        "zip" 			   : unit.community_id.address_id.zip,
                        "community_name"   : unit.community_id.community_name
                    }
        finalJson['unit']['community'] = comunityDict
    if unit.leasing_info_id:
        leasingDict = {
                    "leasing_type" 				     : unit.leasing_info_id.leasing_type,
                    "is_sub_leasing_allowed"  	     : unit.leasing_info_id.is_sub_leasing_allowed,
                    "application_fee"  			     : unit.leasing_info_id.application_fee,
                    "security_deposit" 			     : unit.leasing_info_id.security_deposit, 
                    "monthly_rent_1month_lease" 	 : unit.leasing_info_id.monthly_rent_1month_lease,
                    "monthly_rent_6month_lease" 	 : unit.leasing_info_id.monthly_rent_6month_lease,
                    "monthly_rent_12month_lease" 	 : unit.leasing_info_id.monthly_rent_12month_lease,
                    "is_lease_termination_allowed"   : unit.leasing_info_id.is_lease_termination_allowed,
                    "lease_termination_cost" 		 : unit.leasing_info_id.lease_termination_cost,
                    "additional_leasing_clauses" 	 : unit.leasing_info_id.additional_leasing_clauses
                },
        finalJson['unit']['leasing_info'] = leasingDict
    if unit.unit_type_id:
        finalJson['unit']["unittype"] =  unit.unit_type_id.unit_type
    if unit.address_id:
        finalJson['unit']["street_address"] =unit.address_id.street_address
        finalJson['unit']["city"] = unit.address_id.city
        finalJson['unit']["state"] = unit.address_id.state
        finalJson['unit'][ "county"] = unit.address_id.county
        finalJson['unit']['zip'] = 	unit.address_id.zip
    return finalJson



class Unit_View(APIView):
    def get(self, request, id):
        # checks if unit exists
        if Unit.objects.filter(id=id).exists():
            unit = Unit.objects.get(id=id)
            finalJson = unitJson(unit)
            return Response(finalJson, status=status.HTTP_200_OK)
        else:
            return Response("404 not found", status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, id):
        if Unit.objects.filter(id=id).exists():
            unit = Unit.objects.get(id=id)
            unit.delete()
            return Response("Unit Deleted", status=status.HTTP_200_OK)
        else:
            return Response("404 not found", status=status.HTTP_404_NOT_FOUND)

class Community_View(APIView):
    def put(self, request, id):
        if 'community' in request.data and Community.objects.filter(id=id).exists():
            community = Community.objects.get(id=id)
            #if partial not true object being serialized requires all required fields
            # where null = true in model field not required
            serializer = Community_Serializer(community ,data=request.data['community'], partial=True)
            if serializer.is_valid():
                print("is valid")
                serializer.save()
                return Response('valid data')
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)

class Unit_Type_View(APIView):
    pass

class Leasing_Info_View(APIView):
    pass

class UnitList(APIView):
    def get(self, request):
        parameters = request.GET
        if ('offset' in parameters and 'limit' in parameters 
            and parameters['offset'].isnumeric() and parameters['limit'].isnumeric()):
            offset = int(parameters['offset'])
            limit = int(parameters['limit'])
            limit = offset + limit

            unitLists = Unit.objects.all()[offset:limit]
            units = []
            for unit in unitLists:
                tempJson = unitJson(unit)
                units.append(tempJson['unit'])
            finalJson ={
                "unitlisting" : {
                    "units" : units,
                    "count" : Unit.objects.all().count()
                }
            }
            
            return Response(finalJson, status=status.HTTP_200_OK)
        else:
            unitLists = Unit.objects.all()
            units = []
            for unit in unitLists:
                tempJson = unitJson(unit)
                units.append(tempJson['unit'])
            finalJson ={
                "unitlisting" : {
                    "units" : units,
                    "count" : Unit.objects.all().count()
                }
            }

            finalJson = {
                "units" : units
            }
            print("unit listing check..")
            return Response(finalJson, status=status.HTTP_200_OK)

class AddressList(APIView):
    def get(self, request):
        parameters = request.GET
        print(parameters)
        if ('offset' in parameters and 'limit' in parameters 
            and parameters['offset'].isnumeric() and parameters['limit'].isnumeric()):
            offset = int(parameters['offset'])
            limit = int(parameters['limit'])
            limit = offset + limit
            addresses = [{
                "id"                : address.id,
                "street_address" 	: address.street_address,
			    "city"			    : address.city,
			    "state" 	 		: address.state,
				"county"  		    : address.county,
				"zip"  			    : address.zip
                } for address in Address.objects.all()[offset:limit]
            ]
            finalJson  = {
                "AddressObject" : {
                    "addresses" : addresses,
                    "count"     :  Address.objects.all().count()
                }
            }
            return Response(finalJson)
        else:
            return Response("404", status=status.HTTP_404_NOT_FOUND)

class Address_View(APIView):
    def get(self, request, id):
        # address will check if objects with said parameters exist
        address = Address.objects.filter(id=id)
        if Address.objects.filter(id=id).exists():
            address = Address.objects.get(id=id)
            data = model_to_dict(address)
            return Response(data)
        else:
            return Response("404", status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, id):
        if 'address' in request.data and Address.objects.filter(id=id).exists():
            address = Address.objects.get(id=id)
            #if partial not true object being serialized requires all required fields
            # where null = true in model field not required
            serializer = Address_Serializer(address ,data=request.data['address'], partial=True)
            if serializer.is_valid():
                print("is valid")
                serializer.save()
                return Response('valid data')
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)

class Post_Leasing_Info_View(APIView):
    def post(self, request):
        if "leasing_info" in request.data:
            leasingSerializer = Leasing_Info_Serializer(data=request.data["leasing_info"])
            if leasingSerializer.is_valid():
                leasingSerializer.save()
                print("serializer valid")
                return Response("valid data", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)

class Post_Address_View(APIView):
    # def get(self, request):
    #     nums = request.GET
    #     return Response(nums)
    # --------------------------
    # Get DONT USE BELOW!!
    # response = requests.get("http://localhost:8000/unitmanagement/address/?id=2")
    # print(response.content)
    # print(response.status_code)
    #----------------------------

    def post(self, request):
        if 'address' in request.data:
            serializer = Address_Serializer(data=request.data['address'])
            if serializer.is_valid():
                print("is valid")
                serializer.save()
                return Response('valid data')
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)


class Post_Unit_Type_View(APIView):
    def post(self, request):
        if 'unit_type' in request.data:
            serializer = Unit_Type_Serializer(data=request.data['unit_type'])
            if serializer.is_valid():
                print("is valid")
                serializer.save()
                return Response('valid data')
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)


class Post_Community_View(APIView):
    def post(self, request):
        if "community" in request.data:
            serializer = Community_Serializer(data=request.data["community"])
            if serializer.is_valid():
                print("is valid")
                serializer.save()
                return Response('valid data')
            else:
                return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)

class Post_Unit_View(APIView):
    def post(self, request):
      
        communityObject = None
        addressObject = None
        leasingObject = None
        if 'unit' in request.data:
            fullData = request.data['unit']
        else:
            return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
        # print(request.data)
        #request.data takes json object and converts it to dictionary for us to use
        if "community" in request.data['unit']:
            communityData = request.data['unit']["community"]
            communityName = communityData.pop('community_name')
            addressSerializer = Address_Serializer(data=communityData)
            if addressSerializer.is_valid():
                communityAddressObject = addressSerializer.save()
            else:
                return Response("invalid data", status=status.HTTP_400_BAD_REQUEST)
            communityData = {
                "address_id" : communityAddressObject.id,
                "community_name": communityName
            }
            communitySerializer = Community_Serializer(data=communityData)
            if communitySerializer.is_valid():
                communityObject = communitySerializer.save()
        if "leasing_info" in request.data['unit']:
            # print("yep leasing exists")
            leasingData = request.data['unit']['leasing_info']
            leasingSerializer = Leasing_Info_Serializer(data=leasingData)
            if leasingSerializer.is_valid():
                leasingObject = leasingSerializer.save()
        if ('street_address' in fullData and
            'city' in fullData and
            'state' in fullData and 
            'county' in fullData and 
            'zip' in fullData):
            addressData = {
                'street_address' : fullData['street_address'],
                'city' :fullData['city'],
                'state':fullData['state'],
                'county' :fullData['county'],
                'zip' : fullData['zip']
            }
            addressSerializer = Address_Serializer(data=addressData)
            if addressSerializer.is_valid():
                addressObject = addressSerializer.save()
        if "unit_type" in fullData:
            unitData = {
                'unit_type': fullData['unit_type'] 
            }
            unitTypeSerializer = Unit_Type_Serializer(data=unitData)
            if unitTypeSerializer.is_valid():
                print("yep unit type valid")
                unitTypeObject = unitTypeSerializer.save()
        
        unitData = {
            "num_of_bedrooms" : fullData["num_of_bedrooms"],
            "num_of_bathrooms" : fullData["num_of_bathrooms"],
            "num_of_balcony" :  fullData["num_of_balcony"],
            "is_available" : fullData["is_available"],
            "is_reserved" : fullData["is_reserved"],
            "unit_availability_start_date" :fullData["unit_availability_start_date"],
            "unit_availability_end_date" : fullData["unit_availability_end_date"],
            "unit_description" : fullData["unit_description"],
            "living_area_sf" : fullData["living_area_sf"],
            "unit_number" : fullData["unit_number"],
            "unit_at_floor" : fullData["unit_at_floor"],
        }
        unitSerialier = Unit_Serializer(data=unitData)
        if unitSerialier.is_valid():
            print('valid unit!')
            unitSerialier.save()
        else:
            print("invalid unit")
            return Response(unitSerialier.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response("hello there from unit")

class Example(APIView):
    def get(self, request):
        print(request.data)
        print('why though...')
        unit = Unit.objects.get(id=1)
        print("address:", unit.address_id.street_address)
        return Response("I am a get request",status=status.HTTP_202_ACCEPTED)


    def post(self, request):
        print("data:", request.data)
        print('why though...')

        return Response("good good")