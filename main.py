import config
import logging
from telegram import ParseMode
from telegram.ext import Updater, Filters, CommandHandler
from telegram import *
from telegram.ext import *
import responses as R 
import requests

#import json

print("bot started...")
CHAT_APPROVED = [-1001575007199]

name = 'SaFuTrendz'
symbol = 'SAFU'
address2 = '0x1CD316d3882E8Dd36C7B096eE362F018d6b9795d' #Safutrendz contract address
chartA = "โก https://poocoin.app/tokens/" + address2
# chartB = "https://bscscan.com/token/" + address2
buyPadSwap = "๐ฐ https://padswap.exchange/#/swap?outputCurrency=" + address2

telegramGP = "t.me/safu_trendz"
telegramANS = "t.me/safu_trendz"
twitter = "https://twitter.com/safu_trendz"
socials = f"\n\n๐ Twitter: {twitter}\n\n๐ Telegram Group: {telegramGP}\n\n๐ Telegram Anncouncement: {telegramANS}"

whitepaperInfo = "๐ Our WhitePaper is coming soon! \nStay Tuned!"
announcement = "๐ฃ https://t.me/safu_trendzans"
contract = address2
taxInfo = "8% BUY & SELL \n - 6% Marketing \n - 2% Reflections"
slippageInfo = "๐งพ 8% to 12% Slippage"
website = "๐ https://www.safutrendz.com"
audit = "๐ Audit Report Coming Soon!"
presale = "๐ค Presale Coming Soon!"
doxxed = "\nPlease visit ๐ \n\n ๐ฉ๐จ https://www.safutrendz.com/#our-team"
team = "\nPlease visit ๐ \n\n ๐ฉ๐จ https://www.safutrendz.com/#our-team"

helpcommands = " Type : /whitepaper, /tax, /announcements, /doxxed, /socials, /website, /shill, /chart, /presale, /team, /buy, /contract or /helpSAFUTRENDZ to see this message again"


def start_command(update, context):
    update.message.reply_text('start shilling on {username}')


def help_command(update, context):
    update.message.reply_text(helpcommands)


def get_tokenInfo(update, context):
   
    def run_query(query):  # A simple function to use requests.post to make the API call.
        headers = {'X-API-KEY': config.api}
        request = requests.post('https://graphql.bitquery.io/',
                                json={'query': query}, headers=headers)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                            query))


    # The GraphQL query to get the latest token price

    query = """
            {
            ethereum(network: bsc) {
                dexTrades(
                options: {desc: ["block.height","tradeIndex"], limit: 1}
                exchangeName: {in: ["Pancake", "Pancake v2"]}
                baseCurrency: {is: "0x1CD316d3882E8Dd36C7B096eE362F018d6b9795d"}
                ) {
                transaction {
                    hash
                }
                tradeIndex
                smartContract {
                    address {
                    address
                    }
                    contractType
                    currency {
                    name
                    }
                }
                tradeIndex
                block {
                    height
                }
                baseCurrency {
                    symbol
                    address
                }
                quoteCurrency {
                    symbol
                    address
                }
                quotePrice
            
                }
            }
            }
        """
    result = run_query(query)  # Execute the query

    url = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd').json()

    binance = url['binancecoin']['usd']

    priceBnb = format(result['data']['ethereum']['dexTrades'][0]['quotePrice'], ".5f")
    SAFUusd = format(float(priceBnb) * float(binance), ".4f")
        
    websitedomain = "www.safutrendz.com"
    website = "https://" + websitedomain
    buyNow = "https://padswap.exchange/#/swap?outputCurrency=" + address2
    charts = "https://poocoin.app/tokens/" + address2

    message = f"TokenName: {name}\nTokenSymbol: {symbol}\nTokenAddress: {address2}\n๐๐ PriceUSD: {SAFUusd} USD\n๐๐ PriceBNB: {priceBnb} BNB\n\nWebsite: {website}\n\n๐ฐ Buy here: {buyNow}\n๐ Charts: {charts}"

    update.message.reply_text(message)



def hello(update,context):
    update.message.reply_text("Only when you hold, we will SAFU-moon together")

def chart(update, context):
    update.message.reply_text("SaFuTrendz Charts on Poocoin\n " + chartA)

def buy(update,context):
    update.message.reply_text("Buy SaFuTrendz on \n" + buyPadSwap)

def teamInfo2(update,context):
    update.message.reply_text(team)

def doxxedInfo2(update,context):
    update.message.reply_text(doxxed)

def presaleInfo2(update,context):
    update.message.reply_text(presale)

def auditInfo2(update,context):
    update.message.reply_text(audit)

def slippageInfo2(update,context):
    update.message.reply_text(slippageInfo)

def websitelink2(update,context):
    update.message.reply_text("๐ Visit SaFuTrendz Website \n" + website)

def announcementlink2(update,context):
    update.message.reply_text("๐ ๐ ๐ ๐ ๐ ๐ ๐ ๐  \nHere is a link to our Announcement Channel: \n" + announcement)

def taxInfo2(update,context):
    update.message.reply_text(taxInfo)

def whitepaperInfo2(update,context):
    update.message.reply_text(whitepaperInfo)

def contract2(update,context):
    update.message.reply_text(contract)

def sociallinks2(update,context):
    update.message.reply_text("Links Below ๐ \n " + socials)


def telegramShillGroup(update,context):
    message2 = """ 
    
Here guys some shilling out list where you wonโt get banned for shilling our Million Token so letโs spread the word
 

@CRYPTOMOONGEMs 

@dexgemschat 

@uniswapgemspumpz 

@defisearch 

@gemcollectors 

@moonhunters 

@supergemhunter 

@themoonboyschat 

@UniswapGemGroup 

@jumpsquad 

@BitSquad 

@uniswapresearch 

@shitcoincz 

@DeFiRaccoons 

@CryptoFamilyGroup 

@CryproPriceTalks 

@TheSelectiveApe 

@BSCStreetBetsCaptain 

@BSCApe 

@bscgemz 

@RedRoomTG 

@moonshotcartel 

@uniswaptalk 

@uniswaprektplebs 

@tehmoonwalkers 

@cryptodakurobinhooders 

@wolfonairechatbox 

@SmartChainApes 

 

@BitSquad (31,353 members) 

@Satoshi_club (49,083 members) 

@CryptoFamilyGroup (32,193 members) 

@elliotradescrypto (40,166 members) 

@TradeCoinUnderGround (25,706 members) 

@cryptodakurobinhooders (24,025 members) 

 

10,000 - 20,000 members: 

@moonhunters (15,325 members) 

@tehMoonwalkeRs (14,557 members) 

@DeFiRaccoons (12,306 members) 

@uniswapgemsv2 (14,990  members) 

@de_fi (11,011 members) 

 

5,000 - 10,000 members: 

@gemcollectors (5,213 members) 

@cryptoM00NShots (5,506 members) 

@dexgemschat (5,619 members) 

@uniswapresearch (6,830 members) 

@infinitygainzz (8,481 members) 

@uniswaplegit (9,699 members) 

@acmecrypto (8,290 members) 

@oddgemsfamilia (7,843 members) 

@thegemhunterstg (9,943 members) 

@uniswapgemspumpz (7,149 members) 

@WhalersClub101 (9,967 members) 

@Uniswapchina (5,088 members) 

@Cryptosupportservices (6,120 members) 

@uniswapgem123 (7,004 members) 

@UniswapEarlyCalls (8,029 members) 

@crypto_revolution1 (6,549 members) 

@overdose_gems_group (5,218 members) 

@GemSnipers (5,422 members) 

@InfinityGainzz (8,487 members) 

@unigemchatz (6,387 members) 

@supergemhunter (6,820 members) 

@The_Trading_Pit (8,566 members) 

@deficrew (6,640  members) 

 

1,000 - 5,000 members: 

@Farmingroom (1,182 members) 

@Pumpchads (1,713 members) 

@uniswapone (4,933 members) 

@shitcoincz (3,054 members) 

@uniswap_gem_alerts (4,801 members) 

@binancedextrading (2,173 members) 

@uniswapunofficial (4,631 members) 

@CryproPriceTalks (3,302 members) 

@gemsfordegensgroup (2,333 members) 

@gemdiscussion (2,385  members) 

@gemtalkc (1,196 members) 

@InfinityBotz (1,225 members) 

@cryptomindsgroup (3,977 members) 

@themoonboyschat (3,503 members) 

@sgdefi (1,806 members) 

@UniswapGemGroup (3,728 members) 

@Uniswap_Gem_Dicuss (4,675 members) 

@defisearch (4,142 members) 

@SuicidalPumpGroup (3,877 members) 

@illuminatiGem (3,338 members) 

 

LIST OF FACEBOOK GROUPS TO SHILL 

1. https://www.facebook.com/groups/pancakeswapstackclub/ 

2. https://www.facebook.com/groups/926271128137829 

3. https://www.facebook.com/groups/4102359016497837 

4. https://www.facebook.com/groups/711685075844219 

5. https://www.facebook.com/groups/4011682428922832/ 

6. https://www.facebook.com/groups/255394996243602/
    
     """
    update.message.reply_text(message2)


def handle_message(update, context):
    text = str(update.message.text).lower()

    response = R.sample_responses(text)
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(config.API_KEY, use_context=True)
    dp = updater.dispatcher


    dp.add_handler(CommandHandler("hello", hello))
    # dp.add_handler(CommandHandler("startSAFU", start_command))
    # dp.add_handler(CommandHandler("helpSAFUTRENDZ", help_command))
    # dp.add_handler(CommandHandler("price", get_price))
    dp.add_handler(CommandHandler("SAFUInfo", get_tokenInfo))
    dp.add_handler(CommandHandler("shill", telegramShillGroup))
    dp.add_handler(CommandHandler("chart", chart))
    dp.add_handler(CommandHandler("buy", buy))
    dp.add_handler(CommandHandler("socials", sociallinks2))
    dp.add_handler(CommandHandler("announcement", announcementlink2))
    dp.add_handler(CommandHandler("tax", taxInfo2))
    dp.add_handler(CommandHandler("doxxed", doxxedInfo2))
    dp.add_handler(CommandHandler("audit", auditInfo2))
    dp.add_handler(CommandHandler("presale", presaleInfo2))
    dp.add_handler(CommandHandler("team", teamInfo2))
    # dp.add_handler(CommandHandler("vote", votingInfo2))
    dp.add_handler(CommandHandler("slippage", slippageInfo2))
    dp.add_handler(CommandHandler("website", websitelink2))
    dp.add_handler(CommandHandler("whitepaper", whitepaperInfo2))
    dp.add_handler(CommandHandler("contract", contract2))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
    updater.start_polling()   
    updater.idle()

main()
