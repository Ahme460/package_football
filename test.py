from page_filter_data_apifootball.leagues.utils import Top_goall_and_assist


op=Top_goall_and_assist()
x=op.get_top_goal(
    "https://v3.football.api-sports.io/players/topscorers",
    
    {
     "x-apisports-key": "2be8169e016e5c7cc5379ec0405defb6"

    },

    {
          
     "league": "39",  
     "season": "2024"

    }
)

print(x)



