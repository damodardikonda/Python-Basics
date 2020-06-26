url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'

dfs = pd.read_html(url) # it onluy takes table as a input

print(dfs[0])
