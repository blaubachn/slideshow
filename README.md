# Eye of Gnome/Mate Remote

This application uses Eye of Gnome or Eye of Mate and CherryPy to start, update or stop a slideshow of pictures. The main use for it is being able to have a computer that is scanning a synced folder of some kind to be able to change what is being rotated through.

# Setup

## Installing Eye of Gnome or Eye of Mate (eog/eom)

If Eye of Gnome isn't already installed, here are a few options for installation.  
You will need to know which method was used to install Eye of Gnome/Mate.
**Note: Eye of Mate was included, because Eye of Gnome displays the menu bar in slideshow mode in Lubuntu which I am planning on using this for.**

### Eye of Gnome installation

```
# Installation of Eye of Gnome
sudo apt install eog # Install on Debian/Ubuntu/...
sudo yum install eog # Install on Fedora/RHEL/...
eog                  # test

# Installation of Eye of Gnome using snap
# Set up [snapd](https://docs.snapcraft.io/t/installing-snapd/6735)
sudo snap install eog # install on any distro that supports snaps
eog                   # test

# Installation of Eye of Gnome using flatpak
# Set up [flatpak and flathub](https://flathub.org/home)
flatpak install flathub org.gnome.eog # install
flatpak run org.gnome.eog             # test
```

### Eye of Mate installation

```
sudo apt install eom # Install on Debian/Ubuntu/...
sudo yum install eom # Install on Fedora/RHEL/...
eom                  # test
```

## Installing Python and project dependencies

```
# Install on Debian/Ubuntu/...
sudo apt install python3 
sudo apt install python3-pip

# Install on Fedora/RHEL/...
sudo yum install python3 
sudo yum install python3-pip
```

## Installing project and dependencies

```
git clone https://github.com/blaubachn/eye_of_gnome_remote.git
cd eye_of_gnome_remote
python3 -m pip install cherrypy
python3 run.py
```

# License

[MIT](https://github.com/blaubachn/eye_of_gnome_remote/blob/master/LICENSE.md)
