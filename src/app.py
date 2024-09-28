import pytumblr2
import yaml
import argparse

parser = argparse.ArgumentParser(description='tumblr cli')
parser.add_argument('-v', '--verbose',action='store_true')
args = parser.parse_args()

with open('config/config.yml', 'r') as filehandle:
    config = yaml.safe_load(filehandle)
if args.verbose:
    print(config)

client = pytumblr2.TumblrRestClient(
    config['consumer_key'],
    config['consumer_secret'],
    config['oauth_token'],
    config['oauth_secret']
)
if args.verbose:
    print(client.info())

