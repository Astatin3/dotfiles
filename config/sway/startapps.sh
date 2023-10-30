dbus-update-activation-environment --systemd DISPLAY WAYLAND_DISPLAY SWAYSOCK & 
pkill -f waybar &
pkill -f swaybg &
python3 ~/.config/sway/neofetch.py &
waybar &
