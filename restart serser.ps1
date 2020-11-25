#Kill Python servers
Get-Process |  ForEach-Object {if ($_.ProcessName -eq "python"){
    echo "Killing Python process ID number: [$($_.Id)]"
    Stop-Process -Id $_.Id
}}


#Start server
#Enter intro virtual env
& .\venv\Scripts\activate
python .\dockerDash\manage.py runserver


