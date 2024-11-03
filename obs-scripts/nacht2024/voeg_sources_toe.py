import obspython as obs
import os.path
import os


class SourcesForNacht2024:
    """
    image_source
    ffmpeg_source
    """

    amount_of_scenes = 106
    path_with_source_files = '/home/pieter/Cheops/Gedeelde documenten/Documenten/2.7 Projecten/2.7.3 Nacht van de geschiedenis/2024/Scenes'
    source_folder_for_scene_format_string = 'dia_{0}'

    def generate_scenes(self):
        """
        Generate scenes for 106 dia's
        https://docs.obsproject.com/reference-scenes
        https://github.com/Jwolter0/OBS-Studio-Python-Scripting-Cheatsheet-obspython-Examples-of-API/blob/6d6396f2da410bc29f9665dbc40a21fc390aaa57/src/source_add.py
        """
        for scene_number in range(self.amount_of_scenes, 0, -1):
            # Perform a reverse run to make sure the scenes appear in order
            scene_name = '{0}_Scène {0}'.format(scene_number)
            scene = obs.obs_scene_create(scene_name)
            self.add_sources_to_scene(scene, scene_number, scene_name)
    
    def add_sources_to_scene(self, scene, scene_number, scene_name):
        """
        Add all sources in the folder to the scene
        """
        path_with_sources = os.path.join(
            self.path_with_source_files,
            self.source_folder_for_scene_format_string.format(scene_number)
        )
        for filename in os.listdir(path_with_sources):
            abs_path = os.path.join(path_with_sources, filename)
            if os.path.isfile(abs_path):
                # Ugly hack
                # The following image formats are supported: .bmp, .tga, .png, .jpeg, .jpg, and .gif. (https://obsproject.com/kb/image-sources)
                if os.path.splitext(abs_path)[1].lower() in ('.bmp', '.tga', '.png', '.jpeg', '.jpg', '.gif'):
                    obs.obs_scene_add(scene, self.make_image_source(scene_name, abs_path))
                else:
                    obs.obs_scene_add(scene, self.make_media_source(scene_name, abs_path))

    
    def make_media_source(self, scene_name, path):
        """
        Make a media source
        https://docs.obsproject.com/reference-sources#general-source-functions
        """
        settings = obs.obs_data_create()
        path = os.path.abspath(path)

        source_name = '{0}_{1}'.format(scene_name, os.path.basename(path))

        obs.obs_data_set_string(
            settings,
            'local_file',
            path
        )
        return obs.obs_source_create('ffmpeg_source', source_name, settings, None)
    
    def make_image_source(self, scene_name, path):
        """
        Make an image source
        https://docs.obsproject.com/reference-sources#general-source-functions
        """
        settings = obs.obs_data_create()
        path = os.path.abspath(path)

        source_name = '{0}_{1}'.format(scene_name, os.path.basename(path))

        obs.obs_data_set_string(
            settings,
            'file',
            path
        )
        return obs.obs_source_create('image_source', source_name, settings, None)



eg = SourcesForNacht2024()


def add_pressed(props, prop):
    eg.generate_scenes()


def script_description():
    return "Generate the scenes for the 2024 Nacht van de geschiedenis"


def script_properties():  # ui
    props = obs.obs_properties_create()
    obs.obs_properties_add_button(props, "button", "Generate scenes", add_pressed)
    return props
