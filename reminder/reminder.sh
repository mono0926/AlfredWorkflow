# Run this file to create a new reminder package.
mkdir tmp
cp *.py tmp
cp info.plist tmp
cp *.png tmp
cd tmp
zip reminder.zip *
mv reminder.zip ../reminder.alfredworkflow
cd ..
rm -rf tmp