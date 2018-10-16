import sys
from os.path import join, dirname, realpath
from config_gui import Configuration_Manager
from server_should_run import ServerShouldRun
from slideshow import Slideshow
from remote import Remote

if __name__ == '__main__':
    configuration_manager = Configuration_Manager(join(dirname(realpath(__file__)), 'config.ini'))
    skipconfig = len(sys.argv) > 1 and sys.argv[1] == '--skipconfig'
    server_should_run = ServerShouldRun(skipconfig)

    if not skipconfig:
        from config_gui import ConfigurationManagerGui
        settings_gui = ConfigurationManagerGui(configuration_manager, server_should_run)
        settings_gui.run()

    if server_should_run.ask():
        settings = configuration_manager.get_config()
        slideshow = Slideshow(settings['directory'], settings['install'])
        remote = Remote(slideshow)
        remote.run()
        
    print('Process terminated successfully')