@echo off

echo.
echo launch RenameTool
echo.
title RenameTool
set path_orig=%CD%
set KPENV=20
cd /d %~d0%~p0
cd ../
python -m RenameTool_pkg
title Command Prompt
cd /d %path_orig%