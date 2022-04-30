from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import (Leasing_Info_View, Address_View, Unit_Type_View, Community_View, Unit_View,
Post_Leasing_Info_View, Post_Address_View, Post_Unit_Type_View, Post_Community_View,  Post_Unit_View,
AddressList, UnitList, Example, SiteLoadUp)

# the as_view() turns class into functioning function
urlpatterns = [
    
    path('leasing_info/<int:id>/',Leasing_Info_View.as_view(),name='Example'),
    path('address/<int:id>/', Address_View.as_view(), name='Address'),
    path('unit_type/<int:id>/', Unit_Type_View.as_view(), name="Unit_Type"),
    path('community/<int:id>/', Community_View.as_view(), name="community"),
    path('unit/<int:id>/', Unit_View.as_view(), name = "Unit"),

    #post requests
    path('leasing_info/',Post_Leasing_Info_View.as_view(),name='PostExample'),
    path('address/', Post_Address_View.as_view(), name='PostAddress'),
    path('unit_type/', Post_Unit_Type_View.as_view(), name="PostUnit_Type"),
    path('community/', Post_Community_View.as_view(), name="Postcommunity"),
    path('unit/', Post_Unit_View.as_view(), name = "PostUnit"),

    #listings
    path("addresslisting/", AddressList.as_view(), name="addressList"),
    path('unitlisting/', UnitList.as_view(), name ="UnitListing" ),

    #examples
    path('example/', Example.as_view(), name="Example"),
    
    path('', SiteLoadUp, name="SiteLoadUp"),


]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
