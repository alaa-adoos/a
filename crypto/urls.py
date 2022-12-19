from django.urls import path
from .views import CryptoListView,CryptoDetailView,PostListView,PostDetailView

urlpatterns = [
      path('', CryptoListView.as_view(), name='crypto_list'),
      path('<int:pk>/', CryptoDetailView.as_view(), name='crypto_detail'),
      path('post/', PostListView.as_view(), name='post_list'),
      path('<int:pk>/post/', PostDetailView.as_view(), name='post_detail'),
#     path('<int:pk>/delete/', DeleteView.as_view(), name='_delete'),
]