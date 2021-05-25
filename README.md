# TwitterFollows.py
A script to find mutual follows meeting certain criteria on twitter.
The purpose of this script is to compare two or more twitter profiles and see
if they have any mutual follows in common. Additionally you can put a criteria
for the mutual follower's followers count. So you can find as an example
all people that both CryptoCobain and Path follow that have less than 10,000 followers
These accounts may be under the radar traders, what you do with the information
is up to you.

To use this script you need the following installed or set up:
Python 3

Python Requests Library

Access to the twitter API  library

You view the [SETUP.md](./SETUP.md) file for how to set the project up.

Once you have set the project up the very thing you have to do to it is run the
following command in a terminal window or set it up as an enviornment variable in the 
IDE you are using

`export 'BEARER_TOKEN'=<bearer token value>`

This will allow you access the twitter api using your key.

With all of this set up you can run the program with the following commands

Python3 Influencer.py <filter> <number> <name1> <name1>

The arguments for the program are as follows:

Filter - What to filter the mutual followers by
         Options -
            "follower_count_lt" - Follower Count Less Than
            "follower_count_gt" - Follow Count Greater Than
  
Number - Input for the filter criteria (follower count greater than or less if you are filtering on follower count)

<name1> - Twitter handle of the first person you want to compare against followed by
any number of other twitter handles.

Once ran the program will go through all API calls and output a list of twitter handles
that met the criteria.

Example Input
```
Python3 Influencer.py follower_count_lt 350 EtheriaChan PunOkoBuffett
```

This query will ask for the Mutual Follows between EtheriaChan and PunOkoBuffett
that have less than 350 followers each.

Example Output
```
['@noidtwo', '@Cannibal420']
```

These are the two mutual follows that met this criteria.

You can also use this script (though a bit inefficiently) to find analyze a single person's follow list.
Keep in mind that there is the limit of 900 on the twitter API so this can't be used on big accounts
In the below example I am checking my own account for people with follower count less than 100

Input
```
python3 Influencer.py follower_count_lt 100 PunOkoBuffett
```
Output
```
['@0xdazai', '@0xBasedVoid', '@OscarKevinXR']
```

## Twitter API Limitations
The twitter API standard plan has the following limitations for a 15 minute timeframe:
15 requests to get the follow count of any given twitter users (1000 follows = 1 request)
900 requests to query the public data of any twitter account (this call is made once per 
user input and once per each mutual follow).

This means you cannot compare any people with a total combined follow count of
15,000 or greater as of now. There would also be an issue if there are many mutual follows
(> 900) and the script will fail. Workaround to this is possible through storing
local results and having the user re run the script in 15 more minutes (may work on this
in the future)

## FAQS

## Future Development

Feel free to request features using Github Issues or raise issues 
with the scripts. The filter can change to any of the public information 
provided by the [twitter API](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)

I have some ideas of different filter types but can work based on user requests

## Contact
Please contact me on twitter with any questions or use Github features
@PunOkoBuffett

## Extra
For the example I laid out here are who path + cobie follow with less than 10,000 followers.
```
Python3 Influencer.py follower_count_lt 10000 CryptoCobain Cryptopathic
```

Output
```
['@eliquinox', '@pepenaut', '@DSNR_1', '@piggydeveloper', '@db125db', '@0x4C756B65', '@MozaInfinite', '@UpsUpsAndDowns', '@heat', '@zoidbergbtc', '@Shillexed', '@philipplgh', '@CoinNomad'
, '@BTC_kahir', '@MTX_dd', '@BryptoBelz', '@CryptoHunterGon', '@GhxstNFT', '@T3naciousC', '@kenzboard', '@rdtajj', '@MEKhoko', '@_jasonss', '@Techemist', '@0xElm0', '@AltMinerD', '@setani
mals', '@arbedout', '@tommyXBT', '@comfytrades', '@getderb', '@fishxbt', '@The_Endoryan', '@0xNietzsche', '@lidcoin', '@Trekgirl7of9', '@CryptoGabba', '@BlockchainDenim', '@Hardwood_', '@
Seranged', '@VeyBtc']
```