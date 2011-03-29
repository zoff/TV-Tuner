#!/bin/bash

link=$HOME/.data/data.txt
zatto=$HOME/.data/zatto.txt

if [[ ! -f "$link" || "$(( $(date +"%s") - $(stat -c "%Y" "$link") ))" -gt "600" ]]; then
rm $HOME/.data/data.txt
    curl "http://nst-team.freehostia.com/data.txt"  > $link
fi

cat "$link" | grep "ra2" | cut -d" " -f3 > $zatto
read file < $zatto
rtmpdump -v -r "$file" -W "http://zattoo.com/static/player.swf?" | vlc -
rm $zatto
exit 0
