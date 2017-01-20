# The script to install a custom module.
# All the default modules in portrait will also
# be added using this script, so as to ensure
# latter custom modules will work.
####
# Usage : python install_mod.py module_folder_path
from django.db import models

class module(models.Model):
    name = models.CharField(max_length=32)
    desc = models.CharField(max_length=128)

mod = module()
mod.name = str(input("Enter name of module in max. 32 chars. (Displayed in task page of app)"))
mod.desc = str(input("Enter description of module in max. 128. chars"))
mod.save()
