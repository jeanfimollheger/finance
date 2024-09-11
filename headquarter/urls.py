from django.contrib import admin
from django.urls import path
from budget.views import all_stuffs, all_categories, all_subcategories, all_periods, signup, FluxListView, FluxDetailView, FluxCreateView, FluxUpdateView, FluxDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_stuffs, name="all_stuffs"),
    path('all_categories', all_categories, name="all_categories"),
    path('all_subcategories', all_subcategories, name="all_subcategories"),
    path('all_periods', all_periods, name="all_periods"),
    path('user/signup', signup, name='signup'),


    path('flux/list/', FluxListView.as_view(), name="flux-list"),
    path('flux/<int:pk>/',FluxDetailView.as_view(), name="flux-detail"),
    path('flux/create/', FluxCreateView.as_view(), name ="flux-create"),
    path('flux/<int:pk>/update/', FluxUpdateView.as_view(), name ="flux-update"),
    path('flux/<int:pk>/delete/', FluxDeleteView.as_view(), name ="flux-delete"),
    ]
