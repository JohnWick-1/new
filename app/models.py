from django.db import models

# Create your models here.


class RawDateManager(models.Manager):
    def get_query_set(self):
        return super(RawDateManager, self).get_query_set().raw('''
                    SELECT * FROM student WHERE dob >= "2019-08-13" AND
                                                      dob <= '2020-01-09''')


class FtrByFNameManager(models.Manager):
    def get_query_set(self):
        return super(FtrByFNameManager, self).get_query_set().filter(first_name='john')


class OrdByMarksManager(models.Manager):
    def get_query_set(self):
        return super(OrdByMarksManager, self).get_query_set().order_by('marks')


class Student(models.Model):
    print('inside Student model')

    first_name = models.CharField(max_length=33)
    last_name = models.CharField(max_length=33)
    marks = models.IntegerField()
    DOB = models.DateField()
    objs = models.Manager()
    ord_fn = FtrByFNameManager()
    ord_dt = RawDateManager()
    ord_mk = OrdByMarksManager()

    class Meta:
        db_table = 'student'



class Student2(models.Model):
    print('inside Student2 model')

    first_name = models.CharField(max_length=33)
    last_name = models.CharField(max_length=33)
    marks = models.IntegerField()
    DOB = models.DateField()

    class Meta:
        db_table = 'student2'

