# Run this file to create a new ginger package.
mkdir -p tmp/ginger
cp *.py tmp/ginger
cp info.plist tmp
cp *.png tmp
cp -R ../workflow tmp
cp ../ginger_driver.py tmp
cd tmp
zip ginger.zip * */*.py
mv ginger.zip ../ginger.alfredworkflow
cd ..
rm -rf tmp