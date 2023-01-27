#!/bin/sh

feh --bg-fill --randomize /usr/share/backgrounds/fantacy/* &
picom -b --config ~/.config/picom/picom.conf &
#pavucontrol &
blueman-applet &
nm-applet &
/usr/libexec/xfce-polkit &
numlockx on &
clipit &
xfce4-power-manager &
