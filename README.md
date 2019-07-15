# Slideshow

## Purpose

This is a very customized project written to sit on top of either the Eye of Gnome or Eye of Mate slideshow feature. It stores a file directory and starts or stops a slideshow of the pictures at that location via a Cherry Py web server. While the project was originally targeted only towards Eye of GNOME, Eye of MATE was included because Eye of GNOME displays the menu bar in slideshow mode in Lubuntu which I am using this for. You may want to try out both just to see if you have any issues with either one.

## Setup

1. Install either [Eye of GNOME](https://wiki.gnome.org/Apps/EyeOfGnome/) or [Eye of MATE](https://mate-desktop.org/#eye-of-mate) using the chart below
2. Install [git](https://git-scm.com/downloads), [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/)
3. Check out this repository and dependencies using the following commands in your terminal:

```
git clone https://github.com/blaubachn/slideshow.git
cd slideshow
python3 -m pip install --upgrade -r requirements.txt
python3 src/run.py [--skipconfig]
# The --skipconfig parameter starts up the server without displaying the configuration menu
```

### Eye of Gnome/Eye of Mate Installation
| Platform | Install Eye of GNOME | Install Eye of MATE |
| --- | --- | --- |
| Debian/Ubuntu/... | sudo apt install eog | sudo apt install eom |
| Fedora | sudo dnf install eog | sudo dnf install eom |
| Arch/Manjaro/... | sudo pacman -S eog | sudo pacman -S eom  |
| snap - [setup](https://docs.snapcraft.io/t/installing-snapd/6735) | sudo snap install eog | Not Available (Yet...) |
| flatpak and flathub - [setup](https://flatpak.org/setup/) | flatpak install flathub org.gnome.eog | Not Available (Yet...) |

## Dependencies

* [Python](https://www.python.org/)
* [CherryPy](https://cherrypy.org/)
* [Eye of MATE](https://mate-desktop.org/#eye-of-mate)
* [Eye of GNOME](https://wiki.gnome.org/Apps/EyeOfGnome/)

## Contributors

* [Nathan Blaubach](https://github.com/blaubachn)

## License

[MIT](https://github.com/blaubachn/slideshow/blob/master/LICENSE)
