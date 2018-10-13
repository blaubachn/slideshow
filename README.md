# Eye of Gnome Remote

This application uses Eye of Gnome and CherryPy to stop, update or stop a slideshow of pictures. The main use for it is being able to have a computer that is scanning a synced folder of some kind to be able to change what is being rotated through.

# Setup

## Installing Eye of Gnome (eog)

If Eye of Gnome isn't already installed, here are a few options for installation.  
You will need to know which method was used to install Eye of Gnome.

### standard installation

```
sudo apt install eog # Install on Debian/Ubuntu/...
sudo yum install eog # Install on Fedora/RHEL/...
eog                  # test
```

### snapcraft.io installation

```
sudo snap install eog # install
snap run eog          # test
```

### standard installation

```
flatpak install flathub org.gnome.eog # install
flatpak run org.gnome.eog             # test
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
