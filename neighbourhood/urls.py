from django.urls import path
from .views import HomePageView, ProfileView,BusinessListView, SearchResultsListView, PostCreateView, PostDetailView, PostUpdateView

urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('businesses/', BusinessListView.as_view(), name = 'businesses'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'), 
    path('post/new/', PostCreateView.as_view(), name='upload_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]