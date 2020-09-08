pip3 install -r requirements.txt
chmod +x pyfiles/*
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
$DIR/pyfiles/ebot.py

