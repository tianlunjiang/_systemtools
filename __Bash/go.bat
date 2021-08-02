@echo off
set KP_SHOW=%1
set KP_SHOT=%2
set KP_SCENE=%KP_SHOT:~0,3%
set KP_SHOWDIR=k:/PROJECTS/Personal/%KP_SHOW%/
set KP_SHOTDIR=k:/PROJECTS/Personal/%KP_SHOW%/%KP_SHOT%/
set KP_SHELL=CMD
set KP_MAYADIR=%KP_SHOTDIR%workbench/maya/
set OCIO=K:/PROJECTS/_VFXtemplet/ocio-config/aces_1.0.3/config.ocio
set MAYA_PLUG_IN_PATH=D:/Dropbox/REPOSITORIES/_MayaStudio/

set argC=0
for %%x in (%*) do Set /A argC+=1

if %argC% == 2 (

    if exist %KP_SHOWDIR% (
        if exist %KP_SHOTDIR% (

            cls
            k:
            cd %KP_SHOTDIR%
            echo == GO TO SHOT =========
            echo Show:   %KP_SHOW%
            echo Scene:  %KP_SCENE%
            echo Shot:   %KP_SHOT%
            echo Dir:    %KP_SHOTDIR%
            echo =======================
            REM dir /ad /b
            ls
            echo =======================
            echo - cdshot:      shot dir
            echo - cdshow:      show dir
            echo - cdnuke:      nuke workbench dir
            echo - cdmaya:      maya workbench dir
            echo - cdblender:   blender workbench dir
            echo - cdlgt:       lighting renders dir
            echo - cddailies:   dailies dir
            echo - cddelivery:  delivery renders dir
            title %KP_SHOW%:%KP_SCENE%:%KP_SHOT%

            doskey cdshot=cd "%KP_SHOTDIR%"
            doskey cdshow=cd "%KP_SHOWDIR%"
            doskey cdnuke=cd "%KP_SHOTDIR%workbench/nuke/"
            doskey cdmaya=cd "%KP_SHOTDIR%workbench/maya/scenes/"
            doskey cdblender=cd "%KP_SHOTDIR%workbench/blender/"
            doskey cdlgt=cd "%KP_SHOTDIR%assets/lighting/"
            doskey cddailies=cd "%KP_SHOWDIR%_dailies/"
            doskey cddelivery=cd "%KP_SHOWDIR%_delivery/"
            REM doskey ls=dir /a /b /od

        ) else (
            echo.
            echo %KP_SHOT% does not exist
        )
    ) else (
        echo.
        echo %KP_SHOW% does not exist
    )

) else (
    echo insufficient arguments
    echo "go <show_codename> <shot_name>"
)
