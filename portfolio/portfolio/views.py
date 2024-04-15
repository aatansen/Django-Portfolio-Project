from django.shortcuts import redirect,render
from portfolioapp.models import SocialMediaModel,AboutModel,factModel,SkillsModel,SkillMatricesModel,ResumeModel,ResumeEducationModel,ResumeProfessionalModel,PortfolioModel,ServicesModel,ServicesSectionModel,TestimonialModel,ClientTestimonialModel,ContactModel

def portfolio(request):
    socialmedia = SocialMediaModel.objects.get()
    about = AboutModel.objects.get()
    fact = factModel.objects.get()
    skills = SkillsModel.objects.get()
    skills_matrices = SkillMatricesModel.objects.all()
    resume = ResumeModel.objects.get()
    resume_edu = ResumeEducationModel.objects.all()
    resume_pro = ResumeProfessionalModel.objects.all()
    portfolio_des = PortfolioModel.objects.get()
    services_des = ServicesModel.objects.get()
    services_section = ServicesSectionModel.objects.all()
    testimonial_des = TestimonialModel.objects.get()
    client_testimonial = ClientTestimonialModel.objects.all()
    contact = ContactModel.objects.get()
    myDict={
        'socialmedia':socialmedia,
        'about':about,
        'fact':fact,
        'skills':skills,
        'skills_matrices':skills_matrices,
        'resume':resume,
        'resume_edu':resume_edu,
        'resume_pro':resume_pro,
        'portfolio_des':portfolio_des,
        'services_des':services_des,
        'services_section':services_section,
        'testimonial_des':testimonial_des,
        'client_testimonial':client_testimonial,
        'contact':contact,
        
    }
    return render(request,'index.html',myDict)