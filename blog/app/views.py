from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
        template_name = "app/home.html"# Create your views here.

class PostCollectionView(TemplateView):
        template_name = "app/post_collection.html"
        
 
# nature post view
class Nature_post(TemplateView):
        template_name =  "app/post_page.html"
        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context["slug"] = self.kwargs["slug"]

                context['title'] = 'Nature at its Best'
                context['author'] = ' By Priestest'
                context['last_updated_date'] = 'Last updated on June 28th 2025'
                context['image_url'] = r'app\images\nature.jpeg'
                context['blog_content'] = 'Sed ut perspiciatis unde omnis iste natus error sit ntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem.'
                return context