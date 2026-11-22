Greta Schmedes portfolio

Open the greta-portfolio folder in Visual Studio Code (File > Open Folder).
To preview: right-click site/index.html and choose "Open with Live Server" (install the Live Server extension), or just open it in a browser.

site/            the finished website (keep the img folder next to the html files)
                 index.html = main page with the slide-in panels
                 case-*.html and medal-holder.html = one page per project (5 projects)
source/build.py  texts of the four generated case studies (Broke Blocker, Health Journal, Frisian Link, Scissors Replicate)
source/engine.js interactive parts shared by the case studies
To change case-study text: edit source/build.py, then run  python3 build.py  inside source/  (rewrites the case-*.html files in site/).
Small edits can also be made directly in the html files. medal-holder.html is your original file, edit it directly.
