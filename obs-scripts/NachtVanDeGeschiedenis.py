#!/usr/bin/env python3

"""
Dit script wordt vanuit OBS gedraaid.
"""
import obspython as obs
from datetime import datetime

##
# Script properties
##
def script_description():
    return '''<center><h2>Nacht van de Geschiedenis</h2></center>
    <p>
    Configureer OBS voor de Nacht van de Geschiedenis (CC Nova Wetteren).
    </p>
    '''


def script_defaults(settings):
    obs.obs_data_set_default_string(settings, "editie", '{0}'.format(datetime.now().year))
    obs.obs_data_set_default_int(settings, "scenes", 0)
    obs.obs_data_set_default_string(settings, "bronnen", '/home/pieter/NVDG/{0}/bronnen'.format(datetime.now().year))


def script_properties():
    props = obs.obs_properties_create()
    obs.obs_properties_add_text(props, "editie", "Editie", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_int(props, "scenes", "Aantal scènes", 0, 999, 1)
    obs.obs_properties_add_path(props, "bronnen", "Map met alle bronbestanden (afbeeldingen)", obs.OBS_PATH_DIRECTORY, '', None)
    return props


def script_update(settings):
    global editie, scenes, bronnen
    editie = obs.obs_data_get_string(settings, 'editie')
    scenes = obs.obs_data_get_int(settings, 'scenes')
    bronnen = obs.obs_data_get_string(settings, 'bronnen')
