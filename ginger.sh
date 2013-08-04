cp ginger/info.plist . ginger/*.png .
zip ginger.zip ginger_driver.py ginger/*.py info.plist workflow/*.py
rm info.plist *.png
mv ginger.zip ginger.alfredworkflow