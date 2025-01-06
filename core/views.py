from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Project, Category
from .mail_script import send_email
from .models import Category, Software
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect



def home(request):
    categories = Category.objects.all()
    web_scrapping_category = Category.objects.get(name = "Web Scraping")
    automation_category = Category.objects.get(name = "Automation")
    full_stack_development_category = Category.objects.get(name = "Full Stack Development")
    frontend_category = Category.objects.get(name = "Frontend")
    backend_category = Category.objects.get(name = "Backend")
    scripting_category = Category.objects.get(name="Scripting")
    web_scrapping_project = Project.objects.filter(category=web_scrapping_category)
    automation_project = Project.objects.filter(category=automation_category)
    full_stack_development_project= Project.objects.filter(category=full_stack_development_category)
    frontend_project = Project.objects.filter(category=frontend_category)
    backend_project = Project.objects.filter(category=backend_category)
    scripting_project = Project.objects.filter(category=scripting_category)
    projects = Project.objects.all()
    context = {
        'categories': categories,
        "total_projects": projects.count(),
        "backend_count": backend_project.count(),
        "full_stack_count": full_stack_development_project.count(),
        "frontend_count": frontend_project.count(),
        "automation_count": automation_project.count(),
        "web_scraping_count": web_scrapping_project.count(),
        "scripting_count": scripting_project.count(),
        "projects" : projects,
        "backend": backend_project,
        "full_Stack": full_stack_development_project,
        "frontend": frontend_project,
        "automation": automation_project,
        "web_scraping": web_scrapping_project,
        "scripting": scripting_project,
    }
    
    return render(request,'index.html', context)


def about_page(request):
    return render(request, 'about.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if name and email and phone and subject and message:
            send_email(name, email, phone, subject, message)
        
    return render(request, 'contact.html')


def portfolio(request):
    web_scrapping_category = Category.objects.get(name = "Web Scraping")
    automation_category = Category.objects.get(name = "Automation")
    full_stack_development_category = Category.objects.get(name = "Full Stack Development")
    frontend_category = Category.objects.get(name = "Frontend")
    backend_category = Category.objects.get(name = "Backend")
    scripting_category = Category.objects.get(name="Scripting")
    others_category = Category.objects.get(name = "Other")
    web_scrapping_project = Project.objects.filter(category=web_scrapping_category)
    automation_project = Project.objects.filter(category=automation_category)
    full_stack_development_project= Project.objects.filter(category=full_stack_development_category)
    frontend_project = Project.objects.filter(category=frontend_category)
    backend_project = Project.objects.filter(category=backend_category)
    scripting_project = Project.objects.filter(category=scripting_category)

    

    projects = Project.objects.all()


    context = {
        "projects" : projects,
        "backend": backend_project,
        "full_Stack": full_stack_development_project,
        "frontend": frontend_project,
        "automation": automation_project,
        "web_scraping": web_scrapping_project,
        "scripting": scripting_project,
        "total_projects": projects.count(),
        "backend_count": backend_project.count(),
        "full_stack_count": full_stack_development_project.count(),
        "frontend_count": frontend_project.count(),
        "automation_count": automation_project.count(),
        "web_scraping_count": web_scrapping_project.count(),
        "scripting_count": scripting_project.count(),


    }
    return render(request, 'portfolio2.html', context )


def project_details(request, pk):
    try:
        project = Project.objects.get(pk=pk)
        
        # Split the description by words
        words = project.description.split()
        
        # Divide the words equally
        halfway = len(words) // 2
        project.overview_part1 = ' '.join(words[:halfway])
        project.overview_part2 = ' '.join(words[halfway:])
        # Join words back into two separate parts
        project.description_part1 = ' '.join(words[:halfway])
        project.description_part2 = ' '.join(words[halfway:])
        
        context = {
            'project': project,
        }
    except Project.DoesNotExist:
        # Handle the case where the project does not exist
        context = {
            'error': 'Project not found'
        }

    return render(request, 'single_portfolio.html', context)

def resume_link(request):
    pass

def categorysdata(request):
    data = []
    
    # Fetch all categories
    categories = Category.objects.all()
    
    for category in categories:
        # For each category, get the related projects and their count
        category_projects = Project.objects.filter(category=category)
        category_projects_count = category_projects.count()
        
        # Add the category data to the list
        data.append({
            "category": category.name,  # Replace with actual field name
            "projects": list(category_projects.values()),  # Convert QuerySet to list of dicts
            "count": category_projects_count,
        })
    
    # Return JSON response with the full data
    return JsonResponse(data={"categories": data})
       
def services(request):
    web_scrapping_category = Category.objects.get(name = "Web Scraping")
    automation_category = Category.objects.get(name = "Automation")
    full_stack_development_category = Category.objects.get(name = "Full Stack Development")
    frontend_category = Category.objects.get(name = "Frontend")
    backend_category = Category.objects.get(name = "Backend")
    scripting_category = Category.objects.get(name="Scripting")
    others_category = Category.objects.get(name = "Other")
    web_scrapping_project = Project.objects.filter(category=web_scrapping_category)
    automation_project = Project.objects.filter(category=automation_category)
    full_stack_development_project= Project.objects.filter(category=full_stack_development_category)
    frontend_project = Project.objects.filter(category=frontend_category)
    backend_project = Project.objects.filter(category=backend_category)
    scripting_project = Project.objects.filter(category=scripting_category)
    projects = Project.objects.all()


    context = {
        "projects" : projects,
        "backend": backend_project,
        "full_Stack": full_stack_development_project,
        "frontend": frontend_project,
        "automation": automation_project,
        "web_scraping": web_scrapping_project,
        "scripting": scripting_project,
        "total_projects": projects.count(),
        "backend_count": backend_project.count(),
        "full_stack_count": full_stack_development_project.count(),
        "frontend_count": frontend_project.count(),
        "automation_count": automation_project.count(),
        "web_scraping_count": web_scrapping_project.count(),
        "scripting_count": scripting_project.count(),


    }

    return render(request, 'services2.html', context)


def blog(request):
    return render(request, 'blog.html')



# def project_upload(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         image = request.FILES.get('image')
#         category_id = request.POST.get('category')
#         software_ids = request.POST.getlist('software')
#         overview = request.POST.get('overview')

#         try:
#             category = Category.objects.get(id=category_id)
#             software_list = Software.objects.filter(id__in=software_ids)
#             project = Project.objects.create(
#                 title=title,
#                 description=description,
#                 image=image,
#                 category=category,
#                 overview=overview
#             )
#             project.software.set(software_list)
#             project.save()
#             messages.success(request, "Project uploaded successfully!")
#             return redirect('project_upload')  # Redirect to the same page or another view
#         except Exception as e:
#             messages.error(request, f"Error: {e}")

#     categories = Category.objects.all()
#     software_list = Software.objects.all()
#     return render(request, 'project_upload.html', {
#         'categories': categories,
#         'software_list': software_list
#     })



def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image1')
        category_id = request.POST.get('category')
        software_ids = request.POST.getlist('software')
        overview = request.POST.get('overview')

        try:
            category = Category.objects.get(id=category_id)
            software_list = Software.objects.filter(id__in=software_ids)

            project.title = title
            project.description = description
            if image:
                project.image = image
            project.category = category
            project.software.set(software_list)
            project.overview = overview
            project.save()
            
            messages.success(request, "Project updated successfully!")
            return redirect('project_details', pk=project.pk)  # Redirect to project details
        except Exception as e:
            messages.error(request, f"Error: {e}")

    categories = Category.objects.all()
    software_list = Software.objects.all()
    return render(request, 'edit_project.html', {
        'project': project,
        'categories': categories,
        'software_list': software_list
    })