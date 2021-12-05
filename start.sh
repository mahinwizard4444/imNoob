if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/jinspalakkattu/UFS_Adv_Filter_Bot_v3.git /UFSBotz
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /UFSBotz
fi
cd /UFSBotz
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py