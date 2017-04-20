from django.db import models

def add_modify_kiln_data(in_dict):
    #
    kiln_id = in_dict["kiln_id"]
    this_kiln = models.Kiln.objects.filter(kiln_id = kiln_id)
    if this_kiln is None:
        this_kiln = models.Kiln()
        this_kiln.name = in_dict["kiln_name"]
    else:
        this_kiln.name = in_dict["kiln_name"]
    return False
