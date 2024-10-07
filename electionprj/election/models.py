from django.db import models

class Voter(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    national_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    voted = models.BooleanField(default=False)


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    voted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    party = models.CharField(max_length=50)


class Admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class County(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Constituency(models.Model):
    name = models.CharField(max_length=100)
    county = models.ForeignKey(County, related_name="constituencies", on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}, {self.county.name}'


class Ward(models.Model):
    name = models.CharField(max_length=100)
    constituency = models.ForeignKey(Constituency, related_name="wards", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.constituency.name}'

class PollingStation(models.Model):
    name = models.CharField(max_length=100)
    ward = models.ForeignKey(Ward, related_name="polling_stations", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.ward.name}'
