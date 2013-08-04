cp ginger/info.plist .
cp ginger/*.png .
zip ginger.zip ginger_driver.py ginger/*.py info.plist *.png workflow/*.py
rm info.plist *.png
mv ginger.zip ginger.alfredworkflow