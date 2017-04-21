from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    userprofile_id = models.AutoField(primary_key=True)
    temperature_display_units = models.CharField(default='C', max_length=1)

    def __str__(self):
        return str(self.userprofile_id)

    def __repr__(self):
        return 'UserProfile(user={!r}, userprofile_id={!r}))'.format(
            self.user,
            self.userprofile_id,
        )

class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.TextField()
    program_type = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Program(name={!r}, program_type={!r})'.format(
            self.name,
            self.program_type,
        )

class Kiln(models.Model):
    kiln_id = models.AutoField(primary_key=True)
    kiln_name = models.TextField()

    def __str__(self):
        return self.kiln_name

    def __repr__(self):
        return 'Kiln(kiln_name={!r})'.format(
            self.kiln_name,
        )

class AdminType(models.Model):
    admintype_id = models.AutoField(primary_key=True)
    admintype_name = models.TextField()



class ProgramStep(models.Model):
    programstep_id = models.AutoField(primary_key=True)
    program_id = models.ForeignKey(Program)
    seconds = models.IntegerField()
    temperature_in_c = models.DecimalField(max_digits=5, decimal_places=2)

class jt_Kiln_Admin:
    kiln_admin_id = models.AutoField(primary_key=True)
    kiln_id = models.ForeignKey(Kiln)
    userprofile_id = models.ForeignKey(UserProfile)
    admintype_id = models.ForeignKey(AdminType)
    def __str__(self):
        return self.kiln_admin_id

    def __repr__(self):
        return 'Kiln(kiln_admin_id={!r}, kiln_id={!r}, kiln_user_id={!r})'.format(
            self.kiln_admin_id,
            self.kiln_id,
            self.user_id,
            self.admin_type
        )

class jt_Kiln_Program:
    kiln_program_id = models.AutoField(primary_key=True)
    kiln_id = models.ForeignKey(Kiln)
    userprofile_id = models.ForeignKey(UserProfile)
    program_id = models.ForeignKey(Program)

