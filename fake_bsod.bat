@echo off
taskkill /f /im explorer.exe
taskkill /f /im taskmgr.exe
color 17
mode con: lines=30 cols=80
echo A problem has been detected and Windows has been shut down to prevent damage
echo to your computer.
echo.
echo DRIVER_IRQL_NOT_LESS_OR_EQUAL
echo.
echo If this is the first time you've seen this stop error screen.
echo restart your computer. If this screen appears again, follow
echo these steps:
echo.
echo Check to make sure any new hardware or software is properly installed.
echo If this is a new installation, ask your hardware or software manufacturer
echo for any windows updates you might need.
echo.
echo If problems continue, disable or remove any newly installed hardware
echo or software. Disable BIOS memory options such as caching or shadowing.
echo If you need to use safe mode to remove or disable components, restart
echo your computer, press F8 to select Advanced Startup Options, and then
echo select Safe Mode.
echo.
echo Technical information:
echo.
echo *** STOP: 0x00000000D1 (0x00000000C, 0x000000002, 0x000000000, 0xF86B5A89)
echo *** null.sys - Address F86B5A89 base at F86B5000, DateStamp 3dd991eb
echo.
echo Beginning dump of physical memory
echo Physical memory dump complete.
echo Contact your system administrator or technical support group for further
echo assistance.
:a
goto a