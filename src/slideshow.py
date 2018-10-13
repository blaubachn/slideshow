import subprocess

class Slideshow:
    def __init__(self, directory, eog_install_type):
        self.directory = directory
        self.eog_install_type = eog_install_type

    def change_directory(self, directory):
        self.directory = directory

    def start(self):
        if self.eog_install_type == 'standard/snap':
            subprocess.Popen(['eog', '-s', self.directory])
        elif self.eog_install_type == 'flatpak':
            subprocess.Popen(['flatpak', 'run', 'org.gnome.eog', '-s', self.directory])
        else:
            print('Error: Eye of Gnome is not installed')

    def stop(self):
        subprocess.run(['pkill', 'eog'])

    def update(self):
        self.stop()
        self.start()
