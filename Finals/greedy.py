#trained HMM A matrix using Zodiac Writing as sequence of speed tag
#see tags.py
A = {
0: [0.013286, 0.000000, 0.000000, 0.034510, 0.000000, 0.026178, 0.000000, 0.000000, 0.000000, 0.000000, 0.138792, 0.076813, 0.027595, 0.000000, 0.041617, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.033594, 0.015621, 0.000000, 0.000000, 0.177003, 0.040358, 0.017513, 0.092146, 0.264975, ],
1: [0.000000, 0.000000, 0.181006, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.340203, 0.000000, 0.000000, 0.000000, 0.000000, 0.007307, 0.075989, 0.000000, 0.000000, 0.065504, 0.276527, 0.000000, 0.053464, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
2: [0.000000, 0.000000, 0.044213, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.014741, 0.000000, 0.187752, 0.018894, 0.000000, 0.176831, 0.076565, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.063961, 0.000000, 0.118166, 0.298877, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
3: [0.000000, 0.000000, 0.000000, 0.089451, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.171321, 0.000000, 0.000000, 0.000000, 0.460511, 0.000000, 0.000000, 0.184837, 0.000000, 0.033356, 0.000000, 0.000000, 0.060523, ],
4: [0.050973, 0.000000, 0.550740, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.038099, 0.000000, 0.062515, 0.000000, 0.019063, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.278610, 0.000000, 0.000000, 0.000000, ],
5: [0.000000, 0.000000, 0.189977, 0.000000, 0.000000, 0.000000, 0.000000, 0.296471, 0.000000, 0.376741, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.079706, 0.035808, 0.021297, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
6: [0.240380, 0.031830, 0.041289, 0.000000, 0.000000, 0.063817, 0.000000, 0.006654, 0.000000, 0.011287, 0.000000, 0.110907, 0.000000, 0.021488, 0.054623, 0.024799, 0.000000, 0.000000, 0.000003, 0.000000, 0.009381, 0.006514, 0.000000, 0.025372, 0.207034, 0.014111, 0.039861, 0.090648, 0.000000, ],
7: [0.000000, 0.000000, 0.000000, 0.017065, 0.000000, 0.000000, 0.000000, 0.000000, 0.031248, 0.000000, 0.282422, 0.000000, 0.050829, 0.000000, 0.043894, 0.000000, 0.000000, 0.056447, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.080747, 0.236122, 0.000000, 0.000000, 0.201225, ],
8: [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.719436, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.119708, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.160857, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
9: [0.000000, 0.041692, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.017097, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.183789, 0.085390, 0.000000, 0.672032, ],
10: [0.074967, 0.273014, 0.000000, 0.219643, 0.070221, 0.131279, 0.000000, 0.000000, 0.000000, 0.230875, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
11: [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.079789, 0.000000, 0.000000, 0.353756, 0.441869, 0.000000, 0.000000, 0.124586, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
12: [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.006912, 0.213781, 0.165595, 0.344648, 0.000000, 0.000000, 0.269064, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
13: [0.000000, 0.000000, 0.000000, 0.077342, 0.083640, 0.075087, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.310582, 0.000000, 0.109098, 0.000000, 0.000000, 0.167948, 0.000000, 0.000000, 0.000000, 0.000000, 0.154641, 0.021661, ],
14: [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.887316, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.112684, 0.000000, ],
15: [0.000000, 0.000000, 0.000000, 0.008569, 0.018942, 0.000000, 0.000000, 0.063823, 0.000000, 0.375549, 0.055240, 0.000000, 0.028907, 0.000000, 0.000000, 0.027527, 0.000000, 0.000000, 0.000000, 0.421445, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
16: [0.000000, 0.000000, 0.000001, 0.000000, 0.000000, 0.000000, 0.017513, 0.000000, 0.026922, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.092823, 0.000000, 0.045789, 0.051275, 0.147210, 0.000000, 0.000000, 0.000000, 0.021076, 0.135959, 0.086995, 0.000000, 0.000000, 0.000000, 0.374437, ],
17: [0.053566, 0.000000, 0.000000, 0.000000, 0.033593, 0.068394, 0.000000, 0.050956, 0.154290, 0.000000, 0.000000, 0.187652, 0.000000, 0.029969, 0.000000, 0.087072, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.152060, 0.046286, 0.000000, 0.000000, 0.136160, ],
18: [0.060031, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.236871, 0.000000, 0.000000, 0.689428, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.013670, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
19: [0.000000, 0.000000, 0.399460, 0.000000, 0.023530, 0.000000, 0.000000, 0.077757, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.108234, 0.000000, 0.000000, 0.036501, 0.000000, 0.080961, 0.000000, 0.000000, 0.112228, 0.040358, 0.000000, 0.120972, 0.000000, 0.000000, 0.000000, ],
20: [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.163395, 0.000000, 0.000000, 0.000000, 0.131954, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.051244, 0.653407, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
21: [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.034693, 0.000000, 0.280825, 0.344906, 0.000000, 0.000000, 0.000000, 0.000000, 0.064327, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.034890, 0.000000, 0.240358, ],
22: [0.069377, 0.000000, 0.000000, 0.000000, 0.401402, 0.000000, 0.067292, 0.000000, 0.000000, 0.000000, 0.078789, 0.000000, 0.212317, 0.000000, 0.055390, 0.000000, 0.000000, 0.115432, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
23: [0.231902, 0.000000, 0.016303, 0.000000, 0.016744, 0.000000, 0.000175, 0.000000, 0.000000, 0.000000, 0.000000, 0.124903, 0.000000, 0.006544, 0.029703, 0.007083, 0.000000, 0.095102, 0.000000, 0.008824, 0.000000, 0.032318, 0.028830, 0.013090, 0.050906, 0.039134, 0.000000, 0.202590, 0.095849, ],
24: [0.000000, 0.201464, 0.136405, 0.046405, 0.175421, 0.034021, 0.000000, 0.000000, 0.015947, 0.000000, 0.000000, 0.087660, 0.012621, 0.000000, 0.033409, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.019264, 0.000000, 0.097297, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.140087, ],
25: [0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.273674, 0.022771, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.636010, 0.000000, 0.033608, 0.000000, 0.000000, 0.033936, ],
26: [0.000000, 0.000000, 0.000000, 0.000000, 0.204077, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.227733, 0.000000, 0.000000, 0.412180, 0.000000, 0.000000, 0.156010, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, ],
27: [0.073875, 0.000000, 0.000000, 0.011398, 0.000000, 0.000000, 0.478146, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.005788, 0.000000, 0.017536, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.289061, 0.065748, 0.000000, 0.000000, 0.014097, 0.000000, 0.044351, 0.000000, ],
28: [0.014845, 0.419082, 0.085183, 0.000000, 0.000000, 0.133520, 0.000000, 0.030536, 0.017711, 0.000004, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.062644, 0.015196, 0.000000, 0.000000, 0.008043, 0.031222, 0.000000, 0.002288, 0.000000, 0.000000, 0.166255, 0.013471, 0.000000, 0.000000, ],
}


#list of words for each tag
tags = {0: ['here', 'so', 'now', 'only', 'also', 'not', 'then', 'again', 'even', 'very', 'already', 'originally', 'thus', 'back', 'violently', 'away', 'quite', 'slowly', 'rather', 'shabbily', 'openly', 'well', 'exactly', 'properly', 'instead', 'just', 'quietly', 'i', 'yet', 'awfully', 'lonely', 'up', 'no', 'longer', 'never', 'too', 'entirely', 'apart', 'positively', 'enough', 'aproximately', 'continually', 'extremely', 'possibly', 'right', 'long', 'completely', 'mildly', 'else', 'etc', 'considerably', 'laugh', 'singularly', 'abnormally', 'nevermind', 'really'], 1: ['it', 'them', 'her', 'you', 'me', 'they', 'he', 'him', 'we', 'she'], 2: ['is', 'gives', 'lies', 'consists', 'pigs', 'checks', 'ask', 'requires', 'i', 'elses', 'has', 'theres', 'praises', 'doesnt', 'radians', 'isnt'], 3: ['i', 'quit', 'angry', 'chang', 'last', 'lake', 'ammo', 'super', 'right', 'patterned', 'other', 'front', 'kill', 'friday', 'lone', 'much', 'fun', 'wild', 'dangerous', 'thrilling', 'zodiac', 'good', 'happy', 'material', 'first', 'same', 'back', 'vallejo', 'negro', 'damn', 'lit', 'high', 'small', 'light', 'black', 'dark', 'north', 'bay', 'cover', 'nice', 'bad', 'new', 'lonely', 'routine', 'few', 'fake', 'clever', 'different', 'contrary', 'transparent', 'unnoticeable', 'effective', 'busy', 'hey', 'south', 'west', 'suspicious', 'strange', 'nose', 'stove', 'top', 'ready', 'nasty', 'open', 'future', 'messy', 'sure', 'electric', 'wont', 'difficult', 'afraid', 'ninth', 'tenth', 'safe', 'massive', 'curious', 'blue', 'ten', 'early', 'upset', 'san', 'francisco', 'full', 'parked', 'next', 'unhappy', 'little', 'interesting', 'ant', 'salt', 'deep', 'alive', 'darkened', 'crooked', 'great', 'delicious', 'ive', 'petulant', 'third', 'unspoiling', 'enthusiastic', 'own', 'im', 'rife', 'judicial', 'funny', 'comic', 'private', 'such', 'tut', 'doesnt', 'big', 'horrible', 'fk'], 4: ['kill', 'i', 'live', 'wrist', 'wont', 'know', 'are', 'examiner', 'want', 'do', 'end', 'die', 'have', 'shot', 'episode', 'notice', 'aim', 'am', 'noise', 'make', 'think', 'come', 'hear', 'get', 'commit', 'etc', 'look', 'say', 'wear', 'wonder', 'enjoy', 'pig', 'up', 'cops', 'deserve', 'take', 'try', 'wish', 'hold', 'hope', 'dont', 'tell', 'blubber', 'thank', 'fed', 'yes', 'write', 'shake', 'insist', 'eat', 'dress', 'leave', 'place', 'youll'], 5: ['both', 'the', 'any', 'this', 'some', 'The', 'a', 'all', 'that', 'no', 'these', 'another', 'those', 'every'], 6: ['night', 'day', 'gun', 'barel', 'aim', 'i', 'game', 'ig', 'dangeros', 'gam', 'murderer', 'christmas', 'herman', 'girl', 'th', 'july', 'golf', 'course', 'vallejo', 'state', 'police', 'brand', 'name', 'boy', 'back', 'car', 'side', 'west', 'knee', 'part', 'cipher', 'page', 'paper', 'identity', 'afternoon', 'friday', 'rampage', 'weekend', 'dozen', 'fun', 'forest', 'man', 'anamal', 'something', 'experience', 'paradise', 'collecting', 'afterlife', 'speaking', 'answer', 'way', 'time', 'code', 'door', 'window', 'seat', 'shot', 'head', 'floor', 'scene', 'engine', 'attention', 'phone', 'booth', 'cops', 'thing', 'dark', 'horizon', 'area', 'tape', 'pencil', 'flash', 'light', 'barrel', 'center', 'beam', 'wall', 'spot', 'circle', 'bullet', 'dot', 'water', 'hose', 'need', 'coverage', 'taxi', 'driver', 'washington', 'st', 'maple', 'blood', 'piece', 'shirt', 'zodiac', 'park', 'road', 'school', 'bus', 'morning', 'front', 'tire', 'laugh', 'news', 'while', 'end', 'october', 'telling', 'anyone', 'anger', 'description', 'rest', 'disguise', 'fingertip', 'airplane', 'cement', 'killing', 'mail', 'order', 'ban', 'effect', 'dont', 'cab', 'town', 'one', 'work', 'blue', 'pig', 'fire', 'sound', 'prowl', 'ft', 'goof', 'min', 'hill', 'cop', 'rubber', 'corner', 'block', 'half', 'hey', 'doesnt', 'booboos', 'im', 'bag', 'ammonium', 'nitrate', 'fertilizer', 'gallon', 'oil', 'dump', 'gravel', 'shit', 'anything', 'blast', 'death', 'machine', 'masterpiece', 'market', 'battery', 'clock', 'year', 'system', 'site', 'basement', 'use', 'schedule', 'bomb', 'ask', 'please', 'help', 'check', 'control', 'victim', 'moment', 'trigger', 'mechanism', 'number', 'self', 'money', 'hope', 'meanie', 'station', 'someone', 'territory', 'glory', 'kid', 'date', 'lot', 'dud', 'rain', 'sunlight', 'cloudy', 'accident', 'everyone', 'peace', 'power', 'melvin', 'button', 'bay', 'killer', 'summer', 'map', 'fall', 'list', 'woman', 'baby', 'ride', 'couple', 'burning', 'type', 'top', 'everything', 'torture', 'twitch', 'squirm', 'pine', 'beef', 'burn', 'sun', 'heat', 'billiard', 'dungeon', 'cell', 'pain', 'society', 'autographs', 'implore', 'none', 'banjo', 'serenader', 'race', 'piano', 'organist', 'peppermint', 'vomit', 'face', 'idiot', 'tone', 'country', 'lady', 'guy', 'cry', 'think', 'priest', 'humorist', 'life', 'kind', 'wachmacallit', 'thingmebob', 'wise', 'tut', 'whashisname', 'task', 'matter', 'mt', 'diablo', 'pace', 'fact', 'thirteenth', 'city', 'crackproof', 'price', 'tag', 'knife', 'rope'], 7: ['and', 'or', 'but', 'paradise'], 8: ['by', 'for', 'over', 'ni', 'of', 'at', 'on', 'near', 'in', 'with', 'if', 'around', 'until', 'like', 'because', 'than', 'that', 'about', 'as', 'across', 'barrel', 'out', 'though', 'before', 'so', 'behind', 'through', 'into', 'except', 'blue', 'within', 'from', 'after', 'rile', 'whether', 'up', 'under', 'theyd', 'upon', 'along'], 9: ['wishing', 'wearing', 'being', 'killing', 'getting', 'asking', 'having', 'sitting', 'firing', 'spoiling', 'thrashing', 'squealing', 'racing', 'walking', 'ring', 'wondering', 'saying', 'celling', 'speaking', 'holding', 'seeing', 'waiting', 'bouncing', 'wiping', 'leaving', 'needling', 'using', 'cruising', 'parking', 'going', 'acting', 'running', 'waving', 'searching', 'looking', 'finding', 'drowning', 'trying', 'wandering', 'annihilating', 'starting', 'evening', 'wating', 'screaming', 'inflicting', 'irritating', 'shaking', 'uncompromising', 'filling', 'closing'], 10: ['to'], 11: ['be', 'die', 'prove', 'i', 'print', 'go', 'cruse', 'move', 'kill', 'become', 'give', 'try', 'slow', 'stop', 'supply', 'tell', 'cheer', 'crack', 'have', 'open', 'thats', 'leave', 'draw', 'shoot', 'hit', 'see', 'strike', 'do', 'spray', 'use', 'get', 'make', 'come', 'wipe', 'pick', 'need', 'change', 'announce', 'look', 'catch', 'work', 'run', 'say', 'keep', 'mask', 'min', 'think', 'take', 'ventilate', 'trace', 'developer', 'describe', 'know', 'reroute', 'bluff', 'start', 'help', 'reach', 'let', 'hold', 'lose', 'dig', 'loose', 'remain', 'wouldnt', 'disconnect', 'figure', 'want', 'like', 'wear', 'punish', 'comply', 'tie', 'watch', 'scream', 'listen', 'hang', 'rub', 'warm', 'skin', 'play', 'happen', 'tut', 'hate'], 12: ['mi', 'locks', 'bates', 'teenagers', 'facts', 'shots', 'feet', 'slacks', 'parts', 'editors', 'times', 'people', 'rocks', 'slaves', 'details', 'backwards', 'legs', 'tires', 'victims', 'silhouettes', 'hills', 'trees', 'inches', 'sights', 'races', 'motorcycles', 'drivers', 'cars', 'children', 'targets', 'kiddies', 'i', 'murders', 'robberies', 'killings', 'accidents', 'fingerprints', 'guards', 'coats', 'fingertips', 'tools', 'outfits', 'clues', 'cops', 'trucks', 'dogs', 'blocks', 'groups', 'min', 'holes', 'heads', 'bags', 'pictures', 'questions', 'tests', 'roadsides', 'busses', 'conditions', 'yourselves', 'things', 'buttons', 'eats', 'ones', 'melvins', 'wishes', 'buss', 'hours', 'months', 'others', 'splinters', 'nails', 'cages', 'pleas', 'thumbs', 'players', 'cues', 'offenders', 'nucances', 'hands', 'laughs', 'dates', 'persons', 'centuries', 'provinces', 'fellows', 'men', 'clowns', 'blanks', 'concerns', 'radians', 'reports'], 13: ['had', 'killed', 'were', 'was', 'did', 'began', 'fired', 'leaped', 'ended', 'drove', 'told', 'hung', 'drew', 'implied', 'bullshit', 'sat', 'passed', 'went', 'gave', 'came', 'pulled', 'left', 'called', 'saw', 'said', 'peeled', 'directed', 'disappeared', 'stated', 'set', 'asked', 'marked', 'sight', 'used', 'adjusted', 'sent', 'wiped', 'talked', 'wont', 'punished', 'found', 'burned', 'got', 'kissed', 'wouldnt', 'fought'], 14: ['there'], 15: ['will', 'shall', 'could', 'should', 'would', 'can', 'might', 'must', 'may'], 16: ['more'], 17: ['which', 'that', 'wont'], 18: ['fired', 'shot', 'mailed', 'reborn', 'killed', 'had', 'rolled', 'described', 'brown', 'dressed', 'surrounded', 'taped', 'stained', 'caught', 'searched', 'parked', 'shoot', 'ignored', 'grown', 'been', 'i', 'left', 'coated', 'bought', 'much', 'asked', 'seen', 'rubbed', 'made', 'sent', 'powered', 'stored', 'adapted', 'fun', 'set', 'cracked', 'swamped', 'become', 'complied', 'promised', 'coupled', 'driven', 'placed', 'gorged', 'found', 'underground', 'missed', 'flabby', 'doomed'], 19: ['his', 'your', 'my', 'their', 'her', 'its'], 20: ['up', 'off', 'down', 'out', 'over'], 21: ['most'], 22: ['better', 'more', 'manpower', 'longer', 'slower'], 23: ['best', 'most'], 24: ['when', 'how', 'why', 'where'], 25: ['all'], 26: ['who', 'what', 'whom'], 27: ['one', 'nine', 'two'], 28: ['yes']}

tagName = ['RB', 'PRP', 'VBZ', 'JJ', 'VBP', 'DT', 'NN', 'CC', 'IN', 'VBG', 'TO', 'VB', 'NNS', 'VBD', 'EX', 'MD', 'RBR', 'WDT', 'VBN', 'PRP$', 'RP', 'RBS', 'JJR', 'JJS', 'WRB', 'PDT', 'WP', 'CD', 'UH']


#imports
from constraints import numConstraintsMet 
import random
import numpy as np

def getText(words):
   txt = ""
   for word in words: txt += word 
   return txt.lower()

def getTag(word):
   for tag in tags:
      if word in tags[tag]: return tag
   return None

#greedy algorithm
def greedy():
   words = [random.choice(tags[tagName.index('NN')]),] #start with a random Noun/Noun Plural??
   #words = ['i']
   while True:
      txt = getText(words)
      if len(txt) >= 136: return words
      lastTag = getTag(words[-1])
      if lastTag is None: raise Exception("Word has no tag! something seriously wrong!!")
      
      #find the highest probability for the next tag given the last tag
      prob = A[lastTag] #prob list may not always sum to 1 due to rounding in HMM

      #1.
      #s = sum(prob)
      #prob = [p/s for p in prob] #re-normalize so that they sum to 1
      #nextTag = np.random.choice(np.arange(len(prob)), p=prob) #pick the next tag based on the transition probability

      #2.
      nextTag = prob.index(max(prob))

      #loop through the words in the next tag and use the one that gives most constraints satistified
      #TODO: should we favior the longest word first?? and use threshold instead of the minimum constraints??
      word_choice = []
      missed = None
      for word in tags[nextTag]:
         txt = getText(words + [word,])
         meet, total = numConstraintsMet(txt[:136])
         _m = total - meet
         if missed == None or _m <= missed : 
            if missed != None and _m < missed:
               word_choice = [word]
               missed = _m
            else: #same miss, keep all words, later random select one
               word_choice.append(word)

      #pick one word that gives us most constraints satistified
      if len(word_choice) == 0: word_choice = tags[nextTag]
      _w = max(word_choice, key=lambda p: len(p)) #choose the longer one?? handle ties?
      #words.append(random.choice(word_choice))
      words.append(_w)
      

if __name__ == "__main__":
   words = greedy()
   txt = getText(words)
   meet, total = numConstraintsMet(txt[:136])
   print("for words %s" % words)
   print("or txt %s" % txt[:136])
   print("%d out of %d constraints met" % (meet, total))


