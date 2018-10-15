import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from config import Configuration_Manager

about_text = '''Welcome to the Eye of Gnome Remote!

Photo Directory: The remote will diplay a slideshow of the photos in this folder (excluding photos in it's subfolders)
Installation Type: flatpak commands have an extra prefix, so select the method you used for installation
If Eye of Gnome was pre-installed on the system, the correct installation type is likely the standard/snap option.

Once the Save and Start button is pressed, the web service will start on this machine. You will not be able to change
the settings unless the web service is stopped. This can be done using ctrl+c in the terminal window running this app'''

class ConfigurationManagerGui(Gtk.Window):
    def __init__(self, configuration_manager, server_should_run):
        self.configuration_manager = configuration_manager
        self.server_should_run = server_should_run
        current_configuration = self.configuration_manager.get_config()

        Gtk.Window.__init__(self, title="Eye of Gnome Remote")
        grid = Gtk.Grid()
        self.add(grid)

        spacing = 30
        self.set_border_width(spacing)
        grid.set_column_spacing(spacing)
        grid.set_row_spacing(spacing)

        #------------------------------------------------------------------------------
        # About Label
        #------------------------------------------------------------------------------
        self.about_label = Gtk.Label(about_text)

        #------------------------------------------------------------------------------
        # Directory Label
        #------------------------------------------------------------------------------
        self.directory_label = Gtk.Label("Photo Directory")

        #------------------------------------------------------------------------------
        # Directory Entry
        #------------------------------------------------------------------------------
        self.directory_entry = Gtk.Entry()
        self.directory_entry.set_text(current_configuration['directory'])
        self.directory_entry.set_width_chars(80)

        #------------------------------------------------------------------------------
        # Directory Button
        #------------------------------------------------------------------------------
        self.directory_button = Gtk.Button("Choose...")
        self.directory_button.connect("clicked", self.on_directory_button_clicked)

        #------------------------------------------------------------------------------
        # Installation Label
        #------------------------------------------------------------------------------
        self.installation_label = Gtk.Label("Installation Type")

        #------------------------------------------------------------------------------
        # Installation Combo
        #------------------------------------------------------------------------------
        installation_store = Gtk.ListStore(str)
        installation_types = configuration_manager.get_installation_types()
        for installation_type in installation_types:
            installation_store.append([installation_type])
        
        self.installation_combo = Gtk.ComboBox.new_with_model(installation_store)
        
        renderer_text = Gtk.CellRendererText()
        self.installation_combo.pack_start(renderer_text, True)
        self.installation_combo.add_attribute(renderer_text, "text", 0)

        self.installation_combo.set_active(installation_types.index(current_configuration['install']))

        #------------------------------------------------------------------------------
        # Save Button
        #------------------------------------------------------------------------------
        self.save_button = Gtk.Button("Save")
        self.save_button.connect("clicked", self.on_save_button_clicked)

        #------------------------------------------------------------------------------
        # Cancel Button
        #------------------------------------------------------------------------------
        self.cancel_button = Gtk.Button("Cancel")
        self.cancel_button.connect("clicked", self.on_cancel_button_clicked)

        #------------------------------------------------------------------------------
        # Save and Continue Button
        #------------------------------------------------------------------------------
        self.save_and_start_button = Gtk.Button("Save and Continue")
        self.save_and_start_button.connect("clicked", self.on_save_and_start_button_clicked)

        #------------------------------------------------------------------------------
        # Layout
        #------------------------------------------------------------------------------
        grid.attach(self.about_label,              0,0,3,1)
        
        grid.attach(self.directory_label,          0,1,1,1)
        grid.attach(self.directory_entry,          1,1,1,1)
        grid.attach(self.directory_button,         2,1,1,1)

        grid.attach(self.installation_label,       0,2,1,1)
        grid.attach(self.installation_combo,       1,2,1,1)
        grid.attach(self.save_button,              2,2,1,1)

        grid.attach(self.cancel_button,            0,3,1,1)
        grid.attach(self.save_and_start_button,    2,3,1,1)

    def run(self):
        self.connect("destroy", Gtk.main_quit)
        self.show_all()
        Gtk.main()

    def on_directory_button_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
            "Please choose a folder", 
            self, 
            Gtk.FileChooserAction.SELECT_FOLDER, 
            (
                Gtk.STOCK_CANCEL, 
                Gtk.ResponseType.CANCEL, 
                "Select", 
                Gtk.ResponseType.OK
            )
        )
        dialog.set_default_size(800, 400)
        if dialog.run() == Gtk.ResponseType.OK:
            self.directory_entry.set_text(dialog.get_filename())
        dialog.destroy()

    def on_save_button_clicked(self, button):
        active_iter = self.installation_combo.get_active_iter()
        self.configuration_manager.set_config(
            self.directory_entry.get_text(),
            self.installation_combo.get_model()[active_iter][0]
        )

    def on_cancel_button_clicked(self, button):
        self.destroy()

    def on_save_and_start_button_clicked(self, button):
        active_iter = self.installation_combo.get_active_iter()
        self.configuration_manager.set_config(
            self.directory_entry.get_text(),
            self.installation_combo.get_model()[active_iter][0]
        )
        self.server_should_run.allow()
        self.destroy()
    