# DONT CHANGE THESE CODES⚠️⚠️
if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Jeolpaul2/evamaria /evamaria
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /evamaria
fi
cd /evamaria
pip3 install -U -r requirements.txt
echo "BOT IS STARTING"
python3 botz.py
