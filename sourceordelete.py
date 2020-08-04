import praw
from datetime import datetime, timedelta, timezone
import os
import requests, requests.auth
import re
from src.classes.baseclass import RedditBaseClass
from src.database.database import Posts, Database
from src.classes.logger import Logger
import time, static
import pytz



# Create table to store a backup of all posts

class SourceorDelete_Bot(RedditBaseClass):

    def __init__(self):
        super().__init__()
        self.user_agent = "PC:FeedbackTrackerBot:V1.5 by ScoopJr"
        print('Starting up...', self.user_agent)
        self.reddit = praw.Reddit(client_id=self.client,
                                  client_secret=self.secret,
                                  password=self.password,
                                  user_agent=self.user_agent,
                                  username=self.user)

        self.td = pytz.timezone("America/Los_Angeles")
        self.unixnow = None
        self.db = Database()
        self.log = Logger()
        self.logger = self.log.logger

    def get_token(self):
        """ Retrieves token for Reddit API."""
        client_auth = requests.auth.HTTPBasicAuth(self.client, self.secret)
        post_data = {'grant_type': 'password', 'username': self.user, 'password': self.password}
        headers = {'User-Agent': self.user_agent}
        response = requests.Session()
        response2 = response.post(self.token_url, auth=client_auth, data=post_data, headers=headers)
        self.token = response2.json()['access_token']
        self.t_type = response2.json()['token_type']



    def get_or_create(self, model, **kwargs):
        instance = self.db.session.query(model).filter_by(**kwargs).first()
        if instance:
            return instance
        else:
            instance = model(**kwargs)
            self.db.session.add(instance)
            self.db.session.commit()

    def get_or_add_posts(self, model, **kwargs):
        instance = self.db.session.query(model).filter_by(**kwargs).first()
        if instance:
            print(instance)
            return True
        else:
            try:
                instance = model(**kwargs)
                self.db.session.add(instance)
                self.db.session.commit()
                return False
            except Exception as e:
                print(e)



    def get_utc_days_ago(self, days):
        if days == 0:
            return self.unixnow
        past_date = datetime.now(tz=self.td) - timedelta(days)
        return datetime.timestamp(past_date)


    def get_date_from_utc(self, utc_timestamp):
        monthYearDate = datetime.utcfromtimestamp(int(utc_timestamp)).strftime('%B %Y')
        # post_time = datetime.strptime(post_time, '%Y-%B')
        return monthYearDate

    def compare_two_dates(self):
        posts = []
        post_query = self.db.session.query(Posts).order_by(Posts.date_check.desc()).all()
        for entry in post_query:
            print(self.td.localize(entry.date_check) < self.td.localize(datetime.now()))
            if ((self.td.localize(entry.date_check) < self.td.localize(datetime.now())) and not entry.is_replied):
                posts.append(entry.comment_id)

        return posts

    def reply_to_ready_post(self, comments):

        for com in comments:
            user = self.db.session.query(Posts).filter_by(comment_id=com).first()
            comment = self.reddit.comment(com)
            comment.refresh()
            should_delete = True
            for item in comment.replies:
                print(item)
            for subcomment in comment.replies:
                print(subcomment.author.name, user.author, subcomment.author.name.lower() == user.author.lower())
                if subcomment.author.name.lower() == user.author.lower():
                    msg = subcomment.body
                    reply = f"* Comment by {subcomment.author.name}:\n > {msg}"
                    comment.edit(reply)
                    db_post = self.db.session.query(Posts).filter_by(comment_id=com).first()
                    db_post.is_replied = True
                    self.db.session.commit()
                    should_delete = False
            if should_delete:
                db_post = self.db.session.query(Posts).filter_by(comment_id=com).first()
                db_post.is_replied = True
                self.db.session.commit()
                comment.submission.mod.remove(mod_note=self.removal_note)
                comment.submission.mod.send_removal_message(self.removal_note)


    def main(self):
        subreddit = self.reddit.subreddit(self.subreddit)
        while True:
            for post in subreddit.stream.submissions(pause_after=-1):
                if post is None:
                    break
                print(post.title)
                if post.selftext == "[removed]":
                    continue
                if post.link_flair_text is None:
                    continue
                elif post.link_flair_text in self.flair:
                    time = datetime.fromtimestamp(post.created_utc)
                    print(time)
                    db_post = self.db.session.query(Posts).filter_by(id=post.id).first()
                    if db_post:
                        continue
                    else:
                        for comment in post.comments:
                            if comment.author.name.lower() == self.user.lower() and comment.stickied:
                                time = datetime.fromtimestamp(post.created_utc, tz=self.td) + timedelta(
                                    minutes=self.wait_timer)
                                self.get_or_create(Posts, id=post.id, author=post.author.name.lower(), date_check=time,
                                                   comment_id=comment.id)
                                continue
                        print(f'Going through the subreddit: {post.id}: {post.title} by {post.author.name}')
                        reply_template = f"Hey {post.author.name}! Please reply to this comment with your source. I will check this post for a source in exactly {self.wait_timer} minutes.  Unable to provide a source means post will be removed."
                        my_comment = post.reply(reply_template)
                        my_comment.mod.distinguish(sticky=True)
                        time = datetime.fromtimestamp(post.created_utc, tz=self.td) + timedelta(minutes=self.wait_timer)
                        self.get_or_create(Posts, id=post.id, author=post.author.name.lower(), date_check=time,
                                           comment_id=my_comment.id)
            comments = self.compare_two_dates()
            print(comments)
            if comments:
                self.reply_to_ready_post(comments=comments)
            else:
                time.sleep(120)





if __name__ == '__main__':
    bot = SourceorDelete_Bot()
    bot.main()

