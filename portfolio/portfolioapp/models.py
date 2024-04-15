from django.db import models

# Create your models here.
class SocialMediaModel(models.Model):
    twitter=models.CharField(max_length=100)
    facebook=models.CharField(max_length=100)
    Instagram=models.CharField(max_length=100)
    skype=models.CharField(max_length=100)
    linkedin=models.CharField(max_length=100)

    def __str__(self):
        return self.twitter

class AboutModel(models.Model):
    Profile_img = models.ImageField(upload_to='media/ProfileImg')
    Name=models.CharField(max_length=100)
    Profession1=models.CharField(max_length=100)
    Profession2=models.CharField(max_length=100)
    Profession3=models.CharField(max_length=100)
    About_details=models.CharField(max_length=500)
    Profession_title1=models.CharField(max_length=100)
    Profession_title2=models.CharField(max_length=100)
    Profession_details=models.CharField(max_length=500)
    Profession_para=models.CharField(max_length=500)
    Birthday=models.CharField(max_length=100)
    Website=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    City=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Freelance_status=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name
    
class factModel(models.Model):
    Fact_para=models.CharField(max_length=500)
    Happy_clients=models.CharField(max_length=100)
    Projects=models.CharField(max_length=100)
    Hours_of_support=models.CharField(max_length=100)
    Hard_workers=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Happy_clients
    
class SkillsModel(models.Model):
    Skill_para=models.CharField(max_length=500)
    
    def __str__(self):
        return self.Skill_para
    
class SkillMatricesModel(models.Model):
    Skill_name=models.CharField(max_length=100)
    Skill_progressbar=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Skill_name
    
class ResumeModel(models.Model):
    Resume_para=models.CharField(max_length=500)
    Name=models.CharField(max_length=100)
    About=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Name  

class ResumeEducationModel(models.Model):
    Education_name=models.CharField(max_length=100)
    Education_year=models.CharField(max_length=100)
    Education_institute=models.CharField(max_length=100)
    Education_details=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Education_name
    
class ResumeProfessionalModel(models.Model):
    Professional_experience=models.CharField(max_length=100)
    Professional_experience_year=models.CharField(max_length=100)
    Professional_experience_location=models.CharField(max_length=100)
    Professional_responsibilities=models.CharField(max_length=100)

    def __str__(self):
        return self.Professional_experience

class PortfolioModel(models.Model):
    Portfolio_para=models.CharField(max_length=500)
    
    def __str__(self):
        return self.Portfolio_para
    
class ServicesModel(models.Model):
    Services_para=models.CharField(max_length=500)

    def __str__(self):
        return self.Services_para

class ServicesSectionModel(models.Model):
    Service_icon=models.CharField(max_length=100)
    Service_name=models.CharField(max_length=100)
    Service_details=models.CharField(max_length=500)
    
    def __str__(self):
        return self.Service_name
    
class TestimonialModel(models.Model):
    Testimonial_para=models.CharField(max_length=500)
    
    def __str__(self):
        return self.Testimonial_para

class ClientTestimonialModel(models.Model):
    Client_name=models.CharField(max_length=100)
    Client_img=models.ImageField(upload_to='media/ClientImg')
    Client_profession=models.CharField(max_length=100)
    Client_quote=models.CharField(max_length=500)

    def __str__(self):
        return self.Client_name

class ContactModel(models.Model):
    Contact_para=models.CharField(max_length=500)
    Contact_location=models.CharField(max_length=100)
    Contact_Email=models.CharField(max_length=100)
    Contact_Call=models.CharField(max_length=100)
    
    def __str__(self):
        return self.Contact_para