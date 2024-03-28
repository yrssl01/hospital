import datetime

from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

from .models import Appointment, Notification, Doctor, Patient

@receiver(post_save, sender=Appointment)
def notify_on_new_appointment(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            sender=instance.patient.user,
            recipient=instance.schedule.doctor.user,
            message=f"Новая встреча запланирована на {instance.schedule.timestamp_start}.",
            notification_type=Notification.VISIT_CREATED
        )

@receiver(pre_save, sender=Appointment)
def notify_on_cancelled_appointment(sender, instance, **kwargs):
    if instance.status == Appointment.CANCELLED:
        Notification.objects.create(
            sender=instance.patient.user,
            recipient=instance.schedule.doctor.user,
            message=f"Встреча отменена.",
            notification_type=Notification.VISIT_CANCELLED
        )

@receiver(pre_delete, sender=Doctor)
def notify_on_doctor_delete(sender, instance, **kwargs):
    upcoming_appointments_users_id = Appointment.objects.filter(
        schedule__timestamp_start__gte=datetime.datetime.now(),
        schedule__doctor=instance
    ).values_list('patient__user_id', flat=True)
    for user_id in upcoming_appointments_users_id:
        Notification.objects.create(
            sender=instance.user,
            recipient_id=user_id,
            message=f"Врач {instance.full_name} удален, все связанные встречи и расписания также удалены.",
            notification_type=Notification.OTHER
        )


@receiver(pre_delete, sender=Patient)
def delete_related_appointments(sender, instance, **kwargs):
    related_appointments = Appointment.objects.filter(patient=instance)
    for appointment in related_appointments:
        Notification.objects.create(
            sender=instance.user,
            recipient=appointment.schedule.doctor.user,
            message=f"Пациент {instance.full_name} удален, связанная встреча также удалена.",
            notification_type=Notification.OTHER
        )
