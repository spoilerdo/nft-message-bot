from nft import Nft

QUERY = 'Drop your #NFT (#NFT OR #NFTDrop) min_faves:100'
MAX_RESULT = 100
MESSAGE = 'These NFTs are drawings from a traveler going to a strange land ${{SHORT_LINK}}'
SLEEP_TIME = 1000
NFTS = [Nft('poison-dart-frog', 'https://t.co/NofFrvapjR',
            'https://opensea.io/assets/ethereum/0x495f947276749ce646f68ac8c248420045cb7b5e/63183652208636733101667429356210867848452384428365490779331335740317323231233'),
        Nft('bumblebee', 'https://t.co/PNmnoWE5PU',
            'https://opensea.io/assets/ethereum/0x495f947276749ce646f68ac8c248420045cb7b5e/63183652208636733101667429356210867848452384428365490779331335739217811603457')]
