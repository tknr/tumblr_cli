import pytumblr2
import yaml

with open('config/config.yml', 'r') as filehandle:
    config = yaml.safe_load(filehandle)

print(config)

client = pytumblr2.TumblrRestClient(
    config['consumer_key'],
    config['consumer_secret'],
    config['oauth_token'],
    config['oauth_secret']
)

print(client.info())

