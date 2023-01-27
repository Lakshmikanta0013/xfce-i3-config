
###############################
#### Importing all Modules ####
###############################
import os
import subprocess
import socket

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

# from qtile_extras import widget
# from qtile_extras.widget.decorations import PowerLineDecoration

##################################
######## Autostart Apps ##########
##################################
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

#########set default
mod = "mod4"
terminal = "alacritty"
myBrowser = "firefox"
codeEditor = "code"
file = "thunar"

##########################
######    Colors   #######
##########################
colors = {    
    "bg" : '#1a1a1e',
    "bg-trans" : '#1a1a1e66',
    "bg_alt" : '#212128',
    "gray": '#565656',
    "fg" : '#eeeef4',
    "fg_alt" : '#f8f8f8',
    "red" : '#f24054',
    "green": '#80f280',
    "yellow": '#f2f280',
    "blue": '#9282f2',
    "magenta": '#f284f2',
    "cyan": '#80f2ff',
    "tela": '#30f0b2'    
}

#############################
### Defaults Keybindings ####
#############################
keys = [
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    ########### The essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn(file), desc='Thunar File Manager'),
    Key([mod], "b", lazy.spawn(myBrowser), desc='Firefox'),
    Key([mod], "c", lazy.spawn(codeEditor), desc='Visual Studio Code'),
    Key([mod, "shift"], "Return", lazy.spawn("dmenu_run -nb '#1a1e1e' -sf '#212128' -sb '#f24054' -nf '#00e5ff' -p 'Run: '"), desc='Run Dmenu Launcher'),
    Key([mod], "p", lazy.spawn("rofi -modi drun -show drun -config ~/.config/rofi/col_singlerow.rasi"), desc='Run Rofi Launcher'),
    Key(['control', 'shift'], "space", lazy.spawn("rofimoji --selector-args='-theme ~/.config/rofi/grid.rasi' --hidden-descriptions"), desc='Run RofiMoji'),
    Key([mod, "shift"], "l", lazy.spawn("betterlockscreen -l"), desc='Lock screen'),

    ############ Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    ########### Move windows
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),    
    
    ########## Grow windows.
    Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    ######################
    Key([mod], "Escape", lazy.layout.normalize(), desc="Reset all window sizes"),
    # +++++++++++++++++++++++++++++++++++++++++
    
    ########### Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "s", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"
    ),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "F11", lazy.window.toggle_fullscreen(), desc='Toggle fullscreen'),
    
    
    # Toggle between different layouts as defined below
    Key([mod], "BackSpace", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "End", lazy.shutdown(), desc="Shutdown Qtile"),
    
    ######################## Multimedia Keys
    Key ([],'XF86AudioRaiseVolume' , lazy.spawn('pamixer -i 5'), desc="Increase Volume by 5%" ),
    Key ([],'XF86AudioLowerVolume' , lazy.spawn('pamixer -d 5'), desc="Decrese Volume by 5%" ),
    Key ([],'XF86AudioMute' , lazy.spawn("pamixer -t && dunstify -h string:x-dunst-stack-tag:mute mute: $(pamixer --get-mute)!"), desc="Mute Volume"),   
]

#############################
##### workspace layout: #####
#############################
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

@hook.subscribe.client_new
def client_new(client):
    if client.name == 'Alacritty':
        client.togroup(1)
@hook.subscribe.client_new
def client_new(client):
    if client.name == 'Thunar':
        client.togroup(2)
        
        
################################
###### Layout Customizing ######
################################

layout_theme = {"border_width": 1,
                "margin": 2,
                "border_focus": colors["tela"],
                "border_normal": colors["bg"]
                }
layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Tile(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    # layout.TreeTab(
    #      font = "Cascadia Code",
    #      fontsize = 10,
    #      sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
    #      section_fontsize = 10,
    #      border_width = 2,
    #      bg_color = "1c1f24",
    #      active_bg = "c678dd",
    #      active_fg = "000000",
    #      inactive_bg = "a9a1e1",
    #      inactive_fg = "1c1f24",
    #      padding_left = 0,
    #      padding_x = 0,
    #      padding_y = 5,
    #      section_top = 10,
    #      section_bottom = 20,
    #      level_shift = 8,
    #      vspace = 3,
    #      panel_width = 200
    #      ),
    layout.Floating(**layout_theme)
]

###################################
######## Floating Windows #########
###################################
# @hook.subscribe.client_new
# def floating_dialogs(window):
#     dialog = window.window.get_wm_name() == 'Blueman-manager'
#     if dialog:
#         window.floating = True

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

###################################
##### DEFAULT WIDGET SETTINGS #####
###################################
widget_defaults = dict(
    font="Cascadia Code",
    fontsize=12,
    padding=5,
    background = colors["bg-trans"]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(            
            [
                widget.CurrentLayoutIcon(
                    custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                    foreground = colors["bg"],
                    background = colors["tela"],
                    padding = 0,
                    scale = 0.7
                ),
                widget.CurrentLayout(
                    foreground = colors["bg"],
                    background = colors["tela"],
                    padding = 5
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                    foreground = colors["bg"],
                    background = colors["tela"]
                ),
                widget.GroupBox(
                    hide_unused = True,
                    highlight_method='block',
                    this_current_screen_border = colors["tela"],
                    this_screen_border = colors["red"],
                    block_highlight_text_color = colors["bg"],
                    foreground = colors["tela"],                    
                    fontsize = 14,
                    urgent_border = colors["red"],                    
                    urgent_text = colors["bg"],
                    borderwidth = 0,
                    padding_x = 10,
                ),
                widget.Prompt(
                       prompt = prompt,
                       font = "Cascadia Code",
                       padding = 10,
                       foreground = colors["bg"],
                       background = colors["red"]
                       ),
                widget.TextBox(
                    "❱",
                    foreground = colors["tela"] , 
                    name="icon"
                ),
                widget.WindowName(
                    max_chars = 60,
                    foreground = colors["tela"],
                    padding_x = 10,
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 8,
                       background = colors["red"],
                       foreground = colors["bg"],
                ),
                widget.TextBox(
                       text = " ",
                       width=22,
                       background = colors["red"],
                       foreground = colors["bg"],
                       padding = 0,
                       fontsize = 30
                       ),
                widget.CPU(
                    background = colors["red"],
                    foreground = colors["bg"],
                    format = '{load_percent}%',
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors["bg"],
                       background = colors["red"]
                ),
                widget.Net(
                    background = colors["magenta"],
                    foreground = colors["bg"],
                    format='↓↑{down}',
                    prefix='k'
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       background = colors["green"],
                       foreground = colors["bg"],
                ),
                widget.TextBox(
                       text = "",
                       width=22,
                       background = colors["green"],
                       foreground = colors["bg"],
                       padding = 0,
                       fontsize = 18
                       ),
                widget.Battery(
                    padding = 3,
                    background = colors["green"],
                    foreground = colors["bg"],
                    low_background = colors["red"],
                    low_foreground = colors["bg"],
                    charge_char = '⚡',
                    discharge_char = '',
                    empty_char = '',
                    full_char = '',
                    low_percentage = 0.2,
                    format ='{char} {percent:2.0%}',
                    update_interval = 5,    
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       background = colors["yellow"],
                       foreground = colors["bg"],
                ),
                widget.TextBox(
                       text = "",
                       width = 22,
                       foreground = colors["bg"],
                       background = colors["yellow"],
                       padding = 0,
                       fontsize = 30
                       ),
                widget.Volume(
                    background = colors["yellow"],
                    foreground = colors["bg"],
                ),
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       background = colors["yellow"],
                       foreground = colors["bg"],
                ),
                widget.Systray(
                    background = colors["bg-trans"],
                       padding = 5                        
                ),
                widget.Clock(
                    foreground = colors["bg"],
                    background = colors["magenta"],
                    format = "%A, %b %d - %H:%M "
                ),
            ],
            24,            
            background = colors["bg-trans"],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
