echo "There is a change!"
echo "Going to changed directory"
cd /home/farm
echo "Printing working directory"
pwd
echo "restart application"
systemctl restart farm
echo "You're up to date and application is restarted"