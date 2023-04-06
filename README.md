# TwitterFollows.py
A script to find mutual follows meeting certain criteria on Twitter.
The purpose of this script is to compare two or more Twitter profiles and see
if they have any mutual follows in common. Additionally, you can put a criteria
for the mutual follower's followers count. So you can find as an example
all people that both Cobie and Path follow that have less than 10,000 followers
These accounts may be under the radar traders, what you do with the information
is up to you.

You can use also this script in a limit capacity to analyze a single twitter users 
following base and see if anyone they follow have a lower follower count (in a more limited capacity
due to twitter api limits).

To use this script you need the following installed or set up:
Python 3

Python Requests Library

Access to the Twitter API  library

You view the [SETUP.md](./SETUP.md) file for how to set the project up.

Once you have set the project up the very thing you have to do to it is run the
following command in a terminal window or set it up as an environment variable in the 
IDE you are using

`export 'BEARER_TOKEN'=<bearer token value>`

If you are using windows or windows shell the following command will work as well

`set BEARER_TOKEN=<bearer token value>`

This will allow you to access the Twitter api using your key.

With all of this set up you can run the program with the following commands

`Python3 Influencer.py <filter> <number> <name1> <name1>`

The arguments for the program are as follows:

Filter - What to filter the mutual followers by
         Options -
            "follower_count_lt" - Follower Count Less Than
            "follower_count_gt" - Follow Count Greater Than
  
Number - Input for the filter criteria (follower count greater than or less if you are filtering on follower count)

<name1> - Twitter handle of the first person you want to compare against followed by
any number of other twitter handles

Once ran the program will go through all API calls and output a list of twitter handles
that met the criteria.

Example Input
Some of these inputs/outputs will change over time/be invalid as people gain and lose followers
on twitter or deactivate accounts.
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
In the below example I am checking my own account for people with follower count less than 100. When diffing
two people the list of common followers to analyze will be much smaller "bypassing" this free tier restriction
Though you may still 429 errors for too many requests and have to wait for the cooldown to reset (15 minutes).

Input
```
python3 Influencer.py follower_count_lt 200 PunOkoBuffett
```
Output
```
['@JamesBr66723091', '@OscoXR']
```

## Twitter API Limitations
The Twitter API standard plan has the following limitations for a 15 minute timeframe:
15 requests to get the follow count of any given Twitter users (1000 follows = 1 request)
900 requests to query the public data of any Twitter account (this call is made once per 
user input and once per each mutual follow).

This means you cannot compare any people with a total combined follow count of
15,000 or greater as of now. There would also be an issue if there are many mutual follows
(> 900) and the script will fail. Workaround to this is possible through storing
local results and having the user rerun the script in 15 more minutes (may work on this
in the future)

## FAQS

## Use Case
Many accounts follow smaller accounts that are not in the public eyes of twitter as much and may have 
"hidden" alpha. If a person or project is a mutual follower of many big accounts that could be a sign
that the account being followed is important or a new project going to launch. Finding
mutual followed is also useful though you may need to use the paid twitter API access to fully utilize this tool.

## Future Development

Feel free to request features using Github Issues or raise issues 
with the scripts. The filter can change to any of the public information 
provided by the [twitter API](https://developer.twitter.com/en/docs/twitter-api/getting-started/about-twitter-api)

I have some ideas of different filter types but can work based on user requests

## Contact
Please contact me on twitter with any questions or use Github features
@PunOkoBuffett

## Extra
This is the result for the example I said earlier -  who cobie and path follow with 
less than 10,000 followers, this is the result (as of May 2021). As of April 2023 cobie's account is locked and
the get public followers call will fail. I also tried this with degen spartan and got rate limited with the free tier.
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