from django.shortcuts import render, Http404
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

def badges(request, badge_name):
    # Example badge data - you can replace this with database data
    badge_info = {
        '16a56d3b-b93d-4414-a52b-c7d00c2c1718': {'title': 'Mohit Patel', 'description': 'Top contributor'},
        '17a56d3b-b92d-4454-a52b-c7d00c2c1719': {'title': 'Goli Sai Shiva', 'description': 'Regular contributor'},
        'bronze': {'title': 'Bronze Badge', 'description': 'New contributor'}
    }
    
    if badge_name not in badge_info:
        raise Http404("Badge not found")
        
    context = {
        'badge': badge_info[badge_name],
        'badge_name': badge_name
    }
    return render(request, 'posts/badges.html', context)
