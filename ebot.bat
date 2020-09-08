pushd %~dp0
set script_dir=%CD%
popd
python script_dir/pyfiles/ebot.py
