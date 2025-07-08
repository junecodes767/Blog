from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import date

posts = [
        {
             "slug": "hike-in-the-mountains",
             "image": "mountain.jpg",
             "author":"Priestest",
             "date": date(2025,7,8),
             "title":"Mountain Hiking",
             "excerpt":"There is nothing like when you're hiking in the mountain",
             "content": """
             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
             tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
             quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
             Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
             nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
             deserunt mollit anim id est laborum
             
             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
             tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
             quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
             Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
             nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
             deserunt mollit anim id est laborum
             """
        },
        {
             "slug": "nature-is-amazing",
             "image": "nature.jpeg",
             "author":"Priestest",
             "date": date(2025,7,8),
             "title":"Nature is amazing",
             "excerpt":"There is nothing like when you're walking through nature",
             "content": """
             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
             tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
             quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
             Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
             nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
             deserunt mollit anim id est laborum
             
             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
             tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
             quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
             Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
             nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
             deserunt mollit anim id est laborum
             """
        },
        {
             "slug": "code-is-fun",
             "image": "code.jpeg",
             "author":"Priestest",
             "date": date(2025,7,8),
             "title":"my new obesession: Coding",
             "excerpt":"Learning to use Django in my coding is fun",
             "content": """
             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
             tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
             quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
             Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
             nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
             deserunt mollit anim id est laborum
             
             Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
             tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
             quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
             Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
             nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
             deserunt mollit anim id est laborum
             """
        }
]

def get_date(posts):
        return posts["date"]

def HomeView(request):
        sorted_posts =  sorted(posts,key=get_date)
        latest_post = sorted_posts[-3:]
        return render(request,"app/home.html",context={"posts":latest_post})
        
def PostCollectionView(request):
        return render(request,"app/post_collection.html",context={"posts":posts})
        
 
# nature post view
def post_detail(request,slug):
        identified_post = next(post for post in posts if post["slug"] == slug )
        return render(request,"app/post_page.html",{"posts":identified_post})