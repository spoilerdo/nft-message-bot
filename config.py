from nft import Nft

QUERY = 'Drop your #NFT (#NFT OR #NFTDrop)'
MAX_RESULT = 100
SLEEP_TIME = 1000
NFTS = [Nft('poison-dart-frog', 'https://t.co/NofFrvapjR',
            'https://opensea.io/assets/ethereum/0x495f947276749ce646f68ac8c248420045cb7b5e/63183652208636733101667429356210867848452384428365490779331335740317323231233'),
        Nft('bumblebee', 'https://t.co/PNmnoWE5PU',
            'https://opensea.io/assets/ethereum/0x495f947276749ce646f68ac8c248420045cb7b5e/63183652208636733101667429356210867848452384428365490779331335739217811603457')]
MESSAGES = [
    'These NFTs are drawings from a traveler going to a strange land ${{SHORT_LINK}}',
    'Collectors, have you seen this amazing NFT on #OpenSea? Get it now and own this digital masterpiece! ${{SHORT_LINK}}',
    'Be the proud owner of this unique and one-of-a-kind NFT #OpenSea #NFTs ${{SHORT_LINK}}',
    'Unlock the potential of this rare NFT - a must-have for digital art connoisseurs! #NFTs #OpenSea ${{SHORT_LINK}}',
    'Invest in this incredible NFT - make it yours today! #OpenSea #NFTs ${{SHORT_LINK}}',
    'Get your hands on this one-of-a-kind NFT now! #OpenSea #NFTs ${{SHORT_LINK}}',
    'Dont miss out on this rare NFT! Get it now on #OpenSea #NFTs ${{SHORT_LINK}}']
DAYS = 0
INDEX = 0
MAX_DAYS = 60