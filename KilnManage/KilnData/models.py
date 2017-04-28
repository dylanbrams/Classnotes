from django.db import models
from django.contrib.auth.models import User


class KilnUserProfile(models.Model):
    kiln_user_profile_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    temperature_display_units = models.CharField(default='C', max_length=1)

    def __str__(self):
        return str(self.kiln_user_profile_id)

    def __repr__(self):
        return 'UserProfile(user={!r}, userprofile_id={!r}))'.format(
            self.user,
            self.kiln_user_profile_id,
        )

class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.TextField()
    program_type = models.TextField()


    def __str__(self):
        return self.program_name

    def __repr__(self):
        return 'Program(name={!r}, program_type={!r})'.format(
            self.program_name,
            self.program_type,
        )

class ProgramStep(models.Model):
    programstep_id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Program, related_name='program_steps', on_delete=models.CASCADE)
    order = models.IntegerField()
    seconds = models.DecimalField(max_digits=7, decimal_places=2)
    temperature_in_c = models.DecimalField(max_digits=12, decimal_places=3)

    class Meta:
        unique_together = ('program', 'order')

    def __str__(self):
        return str(self.programstep_id) + " : part of " + self.program.program_name

    def __repr__(self):
        return 'AdminType(programstep_id={!r}, program={!r}, seconds={!r}, temperature_in_c={!r})'.format(
            self.programstep_id,
            self.program,
            self.order,
            self.seconds,
            self.temperature_in_c
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

class KilnAdminType(models.Model):
    kilnadmintype_id = models.AutoField(primary_key=True)
    kilnadmintype_name = models.TextField()

    def __str__(self):
        return self.kilnadmintype_name

    def __repr__(self):
        return 'AdminType(kilnadmintype_name={!r})'.format(
            self.kilnadmintype_name,
        )

class jt_Kiln_Admin(models.Model):
    kiln_admin_id = models.AutoField(primary_key=True)
    kiln = models.ForeignKey(Kiln, related_name='kiln_admin_id')
    user = models.ForeignKey(User, related_name='kiln_admin_id')
    kilnadmintype = models.ForeignKey(KilnAdminType, related_name='kiln_admin_id')
    def __str__(self):
        return self.kiln_admin_id

    def __repr__(self):
        return 'Kiln(kiln_admin_id={!r}, kiln={!r}, user={!r}, kilnadmintype={!r})'.format(
            self.kiln_admin_id,
            self.kiln,
            self.user,
            self.kilnadmintype
        )

class jt_Program_Admin(models.Model):
    program_admin_id = models.AutoField(primary_key=True)
    program = models.ForeignKey(Program, related_name='program_admin_id')
    user = models.ForeignKey(User, related_name='program_admin_id')
    kilnadmintype = models.ForeignKey(KilnAdminType, related_name='program_admin_id')

    def __str__(self):
        return self.program_admin_id

    def __repr__(self):
        return 'Kiln(kiln_admin_id={!r}, kiln={!r}, user={!r}, kilnadmintype={!r})'.format(
            self.program_admin_id,
            self.program,
            self.user,
            self.kilnadmintype
        )


class jt_Kiln_Program(models.Model):
    kiln_program_id = models.AutoField(primary_key=True)
    kiln = models.ForeignKey(Kiln, related_name='Kiln_program')
    user = models.ForeignKey(User, related_name='Kiln_program')
    program = models.ForeignKey(Program, related_name='Kiln_program')

    def __str__(self):
        return self.kiln_program_id

    def __repr__(self):
        return 'Kiln(kiln_program_id={!r}, kiln={!r}, user={!r}, program={!r})'.format(
            self.kiln_program_id,
            self.kiln,
            self.user,
            self.program
        )
