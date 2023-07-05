from datetime import datetime, date
import instaloader
import config

L = instaloader.Instaloader()
L.login(config.IG_USERNAME, config.IG_PASSWORD)

profile = instaloader.Profile.from_username(L.context, config.IG_USERNAME)
followees = profile.get_followees()
posts = []
for followee in followees:
    posts.append(followee.get_posts())

SINCE = date.today()
UNTIL = date.today()

k = 0

for post in posts:
    postdate = post.date

    if postdate > UNTIL:
        continue
    elif postdate <= SINCE:
        k += 1
        if k == 50:
            break
        else:
            continue
    else:
        L.download_post(post)
        k = 0
