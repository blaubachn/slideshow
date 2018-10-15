import subprocess

class Slideshow:
    def __init__(self, directory, eog_install_type):
        self.directory = directory
        self.eog_install_type = eog_install_type

    def change_directory(self, directory):
        self.directory = directory

    def start(self):
        self.stop()
        if self.eog_install_type == 'Eye of Gnome':
            subprocess.Popen(['eog', '-s', self.directory])
        elif self.eog_install_type == 'Eye of Mate':
            subprocess.Popen(['eom', '-s', self.directory])
        elif self.eog_install_type == 'Eye of Gnome flatpak':
            subprocess.Popen(['flatpak', 'run', 'org.gnome.eog', '-s', self.directory])
        else:
            print('This type of installation is not yet supported')

    def stop(self):
        subprocess.run(['pkill', 'eog'])
        subprocess.run(['pkill', 'eom'])
