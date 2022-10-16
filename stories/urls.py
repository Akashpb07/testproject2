from django.urls import path
from stories import views

urlpatterns = [
    path('story/<pk>/', views.StoryDetailView.as_view(), name='story-detail'),
    # path('blog_detail/<str:slug>', views.blog_detail, name="blog_detail"),
    # path('contact_us/', views.contactUs.as_view(), name="contact_us"),
    #{% url 'UpdateBlogView' blog.id %}
    # path('create_new_blog/', views.CreateBlog.as_view(), name="create-blog"),
    #
    # path('update_blog/<int:pk>/', views.UpdateBlogView.as_view(), name="UpdateBlogView"),
    #
    # path('delete_blog/<int:pk>/', views.DeleteBlogView.as_view(), name="DeleteBlogView")
]

