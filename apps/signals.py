from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.models import Student
from apps.serializers import StudentModelSerializer


@receiver(post_save, sender=Student)
def student_change_rank(sender, **kwargs):
    channel_layer = get_channel_layer()
    print(10)
    student_leader_board = list(Student.objects.all().order_by('-rank','name').values('rank' , 'name' , 'id'))
    serializer = StudentModelSerializer(student_leader_board, many=True)
    async_to_sync(channel_layer.group_send)(
        "leader_bord_group",
        {
            "type": "leaderboard_update",
            "data": serializer.data
        }
    )
