you must install wayback_machine_downloader and run this before running the python3 script:

wayback_machine_downloader https://www.cheatography.com --only "/(latex)\/$/i" -c 4
wayback_machine_downloader https://www.cheatography.com --only "/(pdf)\/$/i"
wayback_machine_downloader http://www.cheatography.com --only "/\/cheat-sheets\/[a-z0-9\-_]+\/$/i" -c 4

After you're done downloading, you can sort files with the python script.

Don't forget to adjust the base directory and create the pdf, latex and html destination directory. 

