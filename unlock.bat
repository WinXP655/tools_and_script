@ECHO OFF
color 0f
title Folder Lock
if EXIST "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" goto UNLOCK
if NOT EXIST Private goto MDLOCKER
:CONFIRM
echo Are you sure you want to lock the folder(Y/N)
set/p "cho=>"
if %cho%==Y goto LOCK
if %cho%==y goto LOCK
if %cho%==n goto END
if %cho%==N goto END
echo Invalid choice.
goto CONFIRM

:LOCK
ren Private "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
attrib +h +s +r "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
echo Folder locked
pause
goto End

:UNLOCK
title Folder Locked
echo Folder state: Locked
echo You need a password to unlock folder
set/p "pass=>"
if NOT %pass%== password goto FAIL
attrib -h -s -r "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}"
ren "Control Panel.{21EC2020-3AEA-1069-A2DD-08002B30309D}" Private
echo Folder Unlocked successfully
pause
goto End

:FAIL
echo Invalid password
pause
goto end

:MDLOCKER
md Privte
echo Folder created successfully
pause
goto End

:End
