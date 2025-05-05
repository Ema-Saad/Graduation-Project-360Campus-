from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0007_classroom_teaching_assistants'),  
    ]

    operations = [
        migrations.AddField(
            model_name='eventregistration',
            name='person',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='event_registrations',
                to='main.person'
            ),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='eventregistration',
            unique_together={('event', 'person')},
        ),
        migrations.RemoveField(
            model_name='eventregistration',
            name='student',
        ),
    ]