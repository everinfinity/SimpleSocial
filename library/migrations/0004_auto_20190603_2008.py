# Generated by Django 2.2.1 on 2019-06-03 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_libraryitem_authored_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryitem',
            name='audience',
            field=models.CharField(choices=[('hs_and_older', 'HS and older'), ('intergenerational', 'Intergenerational'), ('grades_k-5', 'Grades K-5'), ('grades_6-10', 'Grades 6-10')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='libraryitem',
            name='genre',
            field=models.CharField(choices=[('biography', 'Biography'), ('commentary', 'Commentary'), ('documentary', 'Documentary'), ('epistle', 'Epistle'), ('exposition', 'Exposition'), ('fiction', 'Fiction'), ('history', 'History'), ('humor', 'Humor'), ('keynote_talk', 'Keynote Talk'), ('lesson_plan', 'Lesson Plan'), ('memorial_minute', 'Memorial Minute'), ('narrative', 'Narrative'), ('poetry', 'Poetry'), ('prayer', 'Prayer'), ('reference', 'Reference')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='libraryitem',
            name='medium',
            field=models.CharField(choices=[('audio', 'Audio production'), ('blog', 'Blog'), ('drawing_painting', 'Drawing/Painting'), ('photograph', 'Photograph'), ('print', 'Print document'), ('video', 'Video production'), ('website', 'Website')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='libraryitem',
            name='time_period',
            field=models.CharField(choices=[('timeless', 'Timeless'), ('1400s', '1400s'), ('1500s', '1500s'), ('1600s', '1600s'), ('1700s', '1700s'), ('1800s', '1800s'), ('1900s', '1900s'), ('2000s', '2000s')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='libraryitem',
            name='topic',
            field=models.CharField(choices=[('community', 'Community'), ('equality', 'Equality'), ('good_order_in_quaker_meetings', 'Good Order in Quaker Meetings'), ('integrity', 'Integrity'), ('the_light', 'The Light'), ('peace', 'Peace'), ('simplicity', 'Simplicity'), ('stewardship', 'Stewardship'), ('quaker_camps', 'Quaker Camps'), ('quaker_culture', 'Quaker Culture'), ('quaker_public_policy_organizations', 'Quaker Public Policy Organizations'), ('quaker_publishers', 'Quaker Publishers'), ('quaker_retreat_centers', 'Quaker Retreat Centers'), ('quaker_schools', 'Quaker Schools'), ('quaker_service_organizations', 'Quaker Service Organizations')], max_length=255, null=True),
        ),
    ]
