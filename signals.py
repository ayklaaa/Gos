# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from .models import Buyer, Profile  # Импортируем наши модели
#
#
# @receiver(post_save, sender=Buyer)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
#
# @receiver(post_save, sender=Buyer)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
