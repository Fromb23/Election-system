import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'electionprj.settings')  # Adjust to your project name
django.setup()

from election.models import County, Constituency, Ward, PollingStation

def polulate_data():
    nairobi = County.objects.create(name="Nairobi")
    kajiado = County.objects.create(name="Kajiado")

    # Nairobi Constituency
    kibra = Constituency.objects.create(name="Kibra", county=nairobi)

    # Kibra wards
    lindi = Wards.objects.create(name="Lindi", constituency=kibra)
    makina = wards.objects.create(name="Makina", constituency=kibra)
    highrise = Wards.objects.create(name="Highrise", constituency=kibra)

    # Polling stations for Lindi 
    PollingStation.objects.create(name="Lindi Primary", ward=lindi)
    PollingStation.objects.create(name="Lindi Mosque", ward=lindi)
    PollingStation.objects.create(name="ODM Center", ward=lindi)
    PollingStation.objects.create(name="Mashimoni Primary", ward=lindi)

    # Polling Station for Makina
    PollingStation.objects.create(name="Makina Mosque", ward=makina)
    PollingStation.objects.create(name="Makina Primary", ward=makina)
    PollingStation.objects.create(name="Kibra High", ward=makina)
    PollingStation.objects.create(name="Kibra DC", ward=makina)
    PollingStation.objects.create(name="Karanja Mosque", ward=makina)

    # PollingStation for Highrise
    

    print("Data polulated for Nairobi kibra constituency")


if __name__ == "__main__":
    polulate_data()

