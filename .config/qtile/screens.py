from libqtile.config import Screen
from libqtile import qtile, bar, widget
from var import terminal


##########################
######    Colors   #######
##########################
from colors import colors, backgroundColor, foregroundColor, workspaceColor

###################################
##### DEFAULT WIDGET SETTINGS #####
###################################
widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=12,
    padding=5,
    background = backgroundColor,
)
extension_defaults = widget_defaults.copy()

top_bar = [
       widget.CurrentLayoutIcon(
           background = backgroundColor,
           scale = 0.7
       ),
       widget.GroupBox(
           hide_unused = True,
           highlight_method='block',
           highlight_color = [backgroundColor, workspaceColor],
           this_current_screen_border = workspaceColor,
           block_highlight_text_color = foregroundColor,
           foreground = workspaceColor,                    
           fontsize = 14,
           urgent_border = colors[9],                    
           urgent_text = foregroundColor,
           borderwidth = 0,
           padding_x = 10,
       ),
       widget.Sep(
              linewidth = 0,
              padding = 8,
              background = backgroundColor,
       ),
       widget.TextBox(
              text = "",
              width=20,
              background = backgroundColor,
              foreground = colors[4],
              padding = 0,
              margin = -5,
              fontsize = 20
              ),
       widget.TextBox(
           "❱",
           foreground = foregroundColor , 
           background = colors[4],
           name="icon"
       ),
       widget.WindowName(
           max_chars = 60,
           foreground = foregroundColor,
           padding_x = 10,
           background = colors[4]
       ),
       widget.Sep(
              linewidth = 0,
              padding = 8,
              background = backgroundColor,
       ),
       widget.TextBox(
              text = "",
              width=20,
              background = backgroundColor,
              foreground = colors[4],
              padding = 0,
              margin = -5,
              fontsize = 20
              ), 
       widget.Sep(
              linewidth = 0,
              padding = 8,
              background = colors[9],
       ),               
       widget.TextBox(
              text = " ",
              width=22,
              background = colors[9],
              foreground = foregroundColor,
              padding = 0,
              fontsize = 30,
              mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
              ),
       widget.CPU(
           background = colors[9],
           foreground = foregroundColor,
           format = '{load_percent}%',
           mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
       ),
       widget.Sep(
              linewidth = 0,
              padding = 6,
              foreground = foregroundColor,
              background = colors[9]
       ),
       widget.Net(
           background = colors[7],
           foreground = foregroundColor,
           format='↓↑{down}',
           prefix='k'
       ),
       widget.Sep(
              linewidth = 0,
              padding = 6,
              background = colors[5],
              foreground = foregroundColor,
       ),
       widget.TextBox(
              text = "",
              width=22,
              background = colors[5],
              foreground = foregroundColor,
              padding = 0,
              fontsize = 16
              ),
       widget.Battery(
           padding = 3,
           background = colors[5],
           foreground = foregroundColor,
           low_background = colors[9],
           low_foreground = foregroundColor,
           charge_char = '⚡',
           discharge_char = '',
           empty_char = '',
           full_char = '',
           low_percentage = 0.2,
           format ='{char} {percent:2.0%}',
           update_interval = 5,    
       ), widget.Sep(
              linewidth = 0,
              padding = 6,
              background = colors[5],
              foreground = foregroundColor,
       ),

       widget.Sep(
              linewidth = 0,
              padding = 6,
              background = colors[6],
              foreground = foregroundColor,
       ),
       widget.TextBox(
              text = "",
              width=22,
              background = colors[6],
              foreground = foregroundColor,
              padding = 0,
              fontsize = 30,
              mouse_callbacks = {
               'Button4': lambda: qtile.cmd_spawn('brightnessctl set +5%'),'Button5': lambda: qtile.cmd_spawn('brightnessctl set 5%-')
               },
              ),
       widget.Backlight(
           background = colors[6],
           foreground = foregroundColor,
           backlight_name = "intel_backlight",
           # brightness_file = '/sys/class/backlight/intel_backlight/brightness',
           # max_brightness_file = '/sys/class/backlight/intel_backlight/max_brightness',
           format = '{percent:2.0%}',
           mouse_callbacks = {
               'Button4': lambda: qtile.cmd_spawn('brightnessctl set +5%'),'Button5': lambda: qtile.cmd_spawn('brightnessctl set 5%-')
           },
       ),
       widget.Sep(
              linewidth = 0,
              padding = 6,
              background = colors[10],
              foreground = foregroundColor,
       ),
       widget.TextBox(
              text = "",
              width = 22,
              foreground = foregroundColor,
              background = colors[10],
              padding = 0,
              fontsize = 30
              ),
       widget.Volume(
           background = colors[10],
           foreground = foregroundColor,
       ),
       widget.Sep(
              linewidth = 0,
              padding = 6,
              background = colors[10],
              foreground = foregroundColor,
       ),
       widget.Systray(
           background = colors[1],
              padding = 5                        
       ), widget.Sep(
              linewidth = 0,
              padding = 6,
              background = colors[1],
       ),
       widget.Sep(
              linewidth = 0,
              padding = 6,
              background = colors[7],
              foreground = foregroundColor,
       ),
       widget.Clock(
           foreground = foregroundColor,
           background = colors[7],
           format = "%I:%M %p "
       ),
       widget.TextBox(
       	text = "⏻",
         width = 30,
         foreground = foregroundColor,
         background = '#ff5555',
         padding = 10,
         fontsize = 22,
         mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("/home/lakshmi/.config/qtile/scripts/powermenu")},    
       ),
       widget.Sep(
              linewidth = 0,
              padding = 6,
              background = '#ff5555',
       ),
]

screens = [
    Screen(
        top=bar.Bar( top_bar,24,),
    ),
]
