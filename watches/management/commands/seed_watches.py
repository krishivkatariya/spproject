from django.core.management.base import BaseCommand
from django.core.files import File
from django.conf import settings
import os
from watches.models import Watch


class Command(BaseCommand):
    help = 'Seed the database with sample watches'

    def handle(self, *args, **options):
        media_dir = os.path.join(settings.MEDIA_ROOT, 'watches')
        sample_data = [
            {"name": "Rolex Submariner", "description": "Classic diver's watch from Rolex.", "price": "12999.00", "image": "i1.png"},
            {"name": "Tissot Le Locle", "description": "Elegant Swiss automatic dress watch.", "price": "549.00", "image": "i2.png"},
            {"name": "Titoni Airmaster", "description": "Reliable Swiss-made everyday watch.", "price": "799.00", "image": "i3.png"},
            {"name": "Omega Seamaster", "description": "Iconic professional diver's watch by Omega.", "price": "4999.00", "image": "i4.png"},
            {"name": "Seiko Prospex", "description": "Durable and accurate sports watch from Seiko.", "price": "399.00", "image": "i5.png"},
            {"name": "Casio G-Shock", "description": "Rugged shock-resistant digital watch.", "price": "129.00", "image": "i6.png"},
            {"name": "Tag Heuer Carrera", "description": "Sporty chronograph with racing heritage.", "price": "2599.00", "image": "i7.png"},
            {"name": "Citizen Eco-Drive", "description": "Solar-powered watch with elegant design.", "price": "299.00", "image": "i8.png"},
            {"name": "Fossil Grant", "description": "Affordable automatic-styled chronograph.", "price": "149.00", "image": "i1.png"},
            {"name": "Patek Philippe Calatrava", "description": "Timeless high-end dress watch.", "price": "24999.00", "image": "i2.png"},
            {"name": "Hublot Big Bang", "description": "Bold modern luxury sports watch.", "price": "11999.00", "image": "i3.png"},
            {"name": "Longines Master Collection", "description": "Classic Swiss watch with refined details.", "price": "1899.00", "image": "i4.png"},
            {"name": "Bulova Classic", "description": "Reliable and well-priced dress watch.", "price": "249.00", "image": "i5.png"},
            {"name": "Cartier Tank", "description": "Iconic rectangular luxury watch.", "price": "6999.00", "image": "i6.png"},
            {"name": "Timex Marlin", "description": "Vintage-inspired mechanical watch at an accessible price.", "price": "199.00", "image": "i7.png"},
        ]

        created = 0
        for item in sample_data:
            if Watch.objects.filter(name=item['name']).exists():
                self.stdout.write(self.style.WARNING(f"Watch '{item['name']}' already exists. Skipping."))
                continue
            watch = Watch(name=item['name'], description=item['description'], price=item['price'])
            image_path = os.path.join(media_dir, item['image'])
            if os.path.exists(image_path):
                with open(image_path, 'rb') as f:
                    django_file = File(f)
                    watch.image.save(item['image'], django_file, save=False)
            else:
                self.stdout.write(self.style.WARNING(f"Image '{item['image']}' not found in MEDIA_ROOT/watches. Skipping image."))
            watch.save()
            created += 1
            self.stdout.write(self.style.SUCCESS(f"Created watch: {watch.name}"))

        self.stdout.write(self.style.SUCCESS(f"Seeding complete. {created} watches created."))
