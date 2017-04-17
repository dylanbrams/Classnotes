from django.db import models

class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    name = models.TextField()
    program_type = models.TextField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Program(name={!r}, program_type={!r})'.format(
            self.name,
            self.program_type
        )

class Kiln(models.Model):
    kiln_id = models.AutoField(primary_key=True)
    kiln_name = models.TextField()

    def __str__(self):
        return self.kiln_name

    def __repr__(self):
        return 'Kiln(kiln_name={!r})'.format(
            self.kiln_name
        )
