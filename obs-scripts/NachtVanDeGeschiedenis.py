#!/usr/bin/env python3

"""
Dit script wordt vanuit OBS gedraaid.
"""
import obspython as obs
from datetime import datetime
import os

##
# Script properties
##
def script_description():
    return '''<center><h2>Nacht van de Geschiedenis</h2></center>
    <p>
    Configureer OBS voor de Nacht van de Geschiedenis (CC Nova Wetteren).
    Bronbestanden moeten geordend zijn per scène.
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
    obs.obs_properties_add_button(props, 'button', 'Aanmaken scenes', script_NachtVanDeGeschiedenis)
    return props


def script_update(settings):
    global EDITIE, SCENES, BRONNEN
    EDITIE = obs.obs_data_get_string(settings, 'editie')
    SCENES = obs.obs_data_get_int(settings, 'scenes')
    BRONNEN = obs.obs_data_get_string(settings, 'bronnen')

def script_unload():
    pass


global ACCEPTED_FILE_EXT
ACCEPTED_FILE_EXT = ('.bmp', '.tga', '.png', '.jpeg', '.jpg', '.gif')


##
# Main script
##
def script_NachtVanDeGeschiedenis():
    """
    Maak x aantal scènes aan.
    Ga naar een map met daarin alle scènes met alle bronbestanden per scène.
    Maak een bron per scène (scene_$scenenummer_bron_$bronnummer)
    """


def nvdg_add_sources_to_scene(scene_number):
    """
    Voeg een set bronnen toe aan een scène.
    We verwachten die in
    $bronnen/$scene_number/
    """
    scene_path = os.path.join(
        BRONNEN,
        '{0}'.format(scene_number)
    )
