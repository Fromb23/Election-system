import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electionprj.settings')  # Adjust to your project name
django.setup()

from election.models import County, Constituency, Ward, PollingStation

def polulate_data():
    nairobi, created = County.objects.get_or_create(name="Nairobi")
    kajiado, created = County.objects.get_or_create(name="Kajiado")

    # Nairobi Constituency
    kibra, created = Constituency.objects.get_or_create(name="Kibra", county=nairobi)

    # Kibra wards
    lindi, created = Ward.objects.get_or_create(name="Lindi", constituency=kibra)
    makina, created = Ward.objects.get_or_create(name="Makina", constituency=kibra)
    highrise, created = Ward.objects.get_or_create(name="Highrise", constituency=kibra)

    # Polling stations for Lindi 
    PollingStation.objects.get_or_create(name="Lindi Primary", ward=lindi)
    PollingStation.objects.get_or_create(name="Lindi Mosque", ward=lindi)
    PollingStation.objects.get_or_create(name="ODM Center", ward=lindi)
    PollingStation.objects.get_or_create(name="Mashimoni Primary", ward=lindi)

    # Polling Station for Makina
    PollingStation.objects.get_or_create(name="Makina Mosque", ward=makina)
    PollingStation.objects.get_or_create(name="Makina Primary", ward=makina)
    PollingStation.objects.get_or_create(name="Kibra High", ward=makina)
    PollingStation.objects.get_or_create(name="Kibra DC", ward=makina)
    PollingStation.objects.get_or_create(name="Karanja Mosque", ward=makina)

    # PollingStation for Highrise
    

    print("Data polulated for Nairobi kibra constituency")


if __name__ == "__main__":
    polulate_data()

