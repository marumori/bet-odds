# bet-odds

allpool.py allows you to parse all pooltypes at once, the data would be stored in fileInitial.txt
HDC.py would only parse Handicap pooltype when run, the data would be stored in fileInitialHDC.txt

Below is a snapshot of the data extraction.
</MATCH><MATCH ID='108754' MATCH_STARTED='False' MATCH_STAGE='InPlayESST_nobr' STATUS='1' VOID='False' HASRESULT='False' INPLAY_POOLS='' HT_POOLS=''><POOL TYPE='HDC' IN='1' MATCH_POOL_STATUS='start-sell' INPLAY ='False' HT_SELL='False' A='100@1.93' H='100@1.91' SELL='True' ISINITIAL_ODDS='False' HG='-0.5/-1' AG='+0.5/+1' />

Glossary:
1.Match ID is an unique ID and could be used for cross checking in attached URL.
#www.hkjcodds.com/match_board/108115#
2.Pool Type ' HDC' refers to Handicap
3.H='100@1.91 refers to Handicap_Home with 1.91
4.A='100@1.93' refers to Handicap_Away with 1.93
5.HG='-0.5/-1' refers to Handicap_Home is set to be (-0.5/-1)
6.AG='+0.5/+1' refers to Handicap_Away is set to be (+0.5/+1)
