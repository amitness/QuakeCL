git clone http://github.com/studenton/QuakeCL.git --quiet
cp QuakeCL/earthquake.py /bin/earthquake
chmod a+x /bin/earthquake
echo "Installation complete."
echo "Type earthquake to start using it."
sudo rm -rf QuakeCL