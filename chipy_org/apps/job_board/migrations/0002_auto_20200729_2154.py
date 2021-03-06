# Generated by Django 2.2.12 on 2020-07-29 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='how_to_apply',
            field=models.CharField(default='hello', help_text='2500 Character Limit', max_length=2500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobpost',
            name='job_type',
            field=models.CharField(choices=[('FT', 'Full-Time'), ('PT', 'Part-Time'), ('CO', 'Contract to Hire Full-Time'), ('PI', 'Paid Internship'), ('PA', 'Paid Apprenticeship')], default='FT', max_length=2),
        ),
        migrations.AddField(
            model_name='jobpost',
            name='location',
            field=models.CharField(choices=[('CH', 'Chicago'), ('CT', 'Chicago and Temporarily Remote'), ('CR', 'Chicago and Remote'), ('RO', 'Remote Only')], default='CH', help_text='ChiPy is a locally based group. The job position must not move the candidate out from Chicago. Working remotely or commuting is acceptable.', max_length=2),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='is_sponsor',
            field=models.BooleanField(default=False, verbose_name='Is this posting from a recruiting agency?'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='status',
            field=models.CharField(choices=[('SU', 'Submitted'), ('AP', 'Approved'), ('RE', 'Rejected')], default='SU', max_length=2),
        ),
    ]
