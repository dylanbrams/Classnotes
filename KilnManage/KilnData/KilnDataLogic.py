from KilnData import models

def add_modify_kiln_data(in_dict):
    # Adds or modifies Kiln data.
    kiln_id = in_dict["kiln_id"]
    this_kiln = models.Kiln.objects.filter(kiln_id = kiln_id)
    if this_kiln != None:
        this_kiln = models.Kiln()
        this_kiln.kiln_name = in_dict["kiln_name"]
        this_kiln.save()
    else:
        this_kiln.update(kiln_name= in_dict["kiln_name"])
    return this_kiln

def add_modify_program_data(in_dict):
    # Adds or modifies Program data.
    #
    program_id = in_dict["program_id"]
    this_program = models.Program.objects.filter(program_id = program_id)
    if this_program.count() == 0:
        this_program = models.Program()
        this_program.program_name = in_dict["program_name"]
        this_program.program_type = in_dict["program_type"]
        this_program.save()
    else:
        this_program[0].program_name = in_dict["program_name"]
        this_program[0].program_type = in_dict["program_type"]
        this_program.save()
    return this_program

