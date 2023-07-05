from instalooter.looters import ProfileLooter
import datetime
import dateutil.relativedelta
import config

looter = ProfileLooter("daquan", videos_only=True,
                       template="{id}-{username}-{width}-{height}")
looter.login(config.IG_USERNAME, config.IG_PASSWORD)

today = datetime.date.today()
thismonth = today.month

looter.download('./Memes', media_count=50, timeframe=thismonth)
