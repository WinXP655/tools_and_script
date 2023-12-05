@echo off
if exist log.txt (
	echo Renaming log.txt
	ren log.txt log%random%.old
)
setlocal enabledelayedexpansion
echo PC Tester
echo Log will be saved as: %cd%\log.txt
echo Level choice
echo.
echo 5 laps - Poor
echo 10 laps - Low
echo 50 laps - Moderate
echo 75 laps - Harder
echo 100 laps - More Harder
echo 150 laps - Hard
echo 500 laps - More Hard
echo 1000 laps - Insane
echo 5000 laps - More Insane
echo 10000 laps - Cool. This is recommended maximum
echo You can enter also a custom laps
echo.
:m
set /p lap=Enter number of repeats(laps): 
if not defined lap (
    echo Laps cannot be blank.
    goto m
)
REM Check if input is a number
echo %lap%|findstr /R /C:"^[1-9][0-9]*$">nul
if %errorlevel% neq 0 (
    echo Please enter a valid number.
    goto m
)
if %lap% leq 0 (
    echo Number must be greater than 0.
    goto m
)

REM Ask for confirmation
set /p confirm=Are you sure to start test with %lap% laps? (Y/N)
if /I "%confirm%" NEQ "Y" (
    echo Test cancelled.
    goto m
)

REM Start the timer
for /f "tokens=1-4 delims=:.," %%a in ("%time%") do (
   set /A "start=(((%%a*60)+1%%b %% 100)*6000+1%%c %% 100*100+1%%d %% 100)/100"
)

:a
for /L %%i in (1,1,%lap%) do (
    set "randomString="
    for /L %%j in (1,1,50) do (
        set /a "rand=(!random!%%10)"
        set "randomString=!randomString!!rand!"
    )
    echo !randomString! >> log_randnum.txt
    echo Lap: %%i/%lap% - completed! >> log.txt
    echo Lap %%i of %lap% completed.
)

REM End the timer
for /f "tokens=1-4 delims=:.," %%a in ("%time%") do (
   set /A "end=(((%%a*60)+1%%b %% 100)*6000+1%%c %% 100*100+1%%d %% 100)/100"
)

REM Calculate the elapsed time
set /A elapsed=(end-start)*10

echo Test completed in %elapsed% ms. >> log.txt
echo Test completed in %elapsed% milliseconds. Press any key to run again or close this window to exit.
pause>nul
goto a
