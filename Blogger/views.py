from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404

from Blogger.models import BlogModel, ImageModel
from Blogger.forms import ImageForm, BlogForm

from django.contrib.auth.decorators import login_required



@login_required
def create_blog_and_image(request):
    form_blog = BlogForm()
    form_image = ImageForm()
    message = ''
    if request.method=="POST":
        form_blog = BlogForm(request.POST)
        form_image=ImageForm(request.POST, request.FILES)
        if all((form_blog.is_valid(), form_image.is_valid())):
            form_image_instance = form_image.save(commit=False)
            form_image_instance .uploader = request.user
            form_image_instance .save()
            form_blog_instance = form_blog.save(commit=False)
            form_blog_instance.blog_creator = request.user
            form_blog_instance.blog_image = form_image_instance 
            form_blog_instance.save()
            message = 'blog and image created succefully'
            return redirect('get_blogs_images')
        else:
            message = 'verify data !'
    return render(request, 'Blogger/blog_and_image_created.html', context={'form_blog':form_blog,'form_image':form_image,'message':message})
        

@login_required  
def get_blogs_images(request):
    images = ImageModel.objects.all()
    blogs = BlogModel.objects.all()
    return render(request, 'Blogger/get_blogs_images.html', context={'images':images,'blogs':blogs})

@login_required
def get_my_blogs_and_images(request):
    blogs_images_list = get_list_or_404(BlogModel, blog_creator=request.user)
    return render(request, 'Blogger/blogs_images_with_criteria.html', context={'blogs_images_list':blogs_images_list})
    

@login_required
def modify_blog_image(request, id):
    blog_instance = get_object_or_404(BlogModel, id=id)
    image_instance = get_object_or_404(ImageModel, id=id)
    form_blog_instance = BlogForm(instance=blog_instance)
    form_image_instance=ImageForm(instance=image_instance)
    if request.method=="POST":
        form_blog_instance = BlogForm(request.POST, instance=blog_instance)
        form_image_instance=ImageForm(request.POST, request.FILES, instance=image_instance)
        if all((form_blog_instance.is_valid(), form_image_instance.is_valid())):
            form_image_instance.save(commit=False)
            form_image_instance.uploader=request.user
            form_image_instance.save()
            form_blog_instance.save(commit=False)
            #form_blog_instance.blog_image = form_image_instance #look at this
            blog_instance.blog_image = image_instance
            form_blog_instance.blog_creator = request.user
            form_blog_instance.save()
            return redirect('get_my_blogs_and_images')
    return render(request, 'Blogger/blog_image_modified.html', context={'form_blog_instance':form_blog_instance, 'form_image_instance':form_image_instance})

@login_required        
def delete_blog_image(request, id):
    blog_instance=get_object_or_404(BlogModel, id=id)
    blog_instance.delete()
    return redirect('home')