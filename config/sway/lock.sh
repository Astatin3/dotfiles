screenshotloc=/tmp/screensaver.png
sscommand="btop"
terminal="foot"

lockscreensaverdelay=30
termopendelay=0.2

curworkspace=$(swaymsg -pt get_workspaces | grep -o -P '(?<=Workspace\s).*(?=\s\(focused\))')
brightness=$(brightnessctl g)

function start {
  #Create screenshot and blur
  grim $screenshotloc
  convert $screenshotloc -filter Gaussian -blur 0x8 $screenshotloc

  #Open screensaver program for quick-change
  swaymsg workspace "screensaver"
  sleep 0.1
  swaymsg exec $terminal $sscommand &
  sleep "$termopendelay"
  swaymsg fullscreen toggle
}

function stop {
  swaymsg workspace $curworkspace
  pkill -fn $sscommand
  rm $screenshotloc
}

function doscreensaver {
  swayidle timeout 1 "" resume "pkill -n swayidle"
  dolock
}

function dolock {
  pkill swaylock
  swaymsg exec "swaylock -i $screenshotloc && pkill -n swayidle" &
  swayidle timeout "$lockscreensaverdelay" "pkill -n swayidle"
  if [[ "$(pidof 'swaylock')" != "" ]]; then
    pkill swaylock
    doscreensaver
  fi
}

if [[ $1 == "lock" ]]; then
  start
  dolock
  stop
elif [[ $1 == "ss" ]]; then
  start
  doscreensaver
  stop
else
  echo "invalid command, try 'ss' or 'lock'"
fi
