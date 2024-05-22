# Multilogin X
MLX_USERNAME = 'username'
MLX_PASSWORD_FIELD = 'password'
MLX_PASSWORD = 'PASSWORD'
MLX_EMAIL_FIELD = 'email'
MLX_EMAIL = 'EMAIL'
MLX_TOKEN = 'token'
MLX_HEADERS = 'headers'
MLX_DATA = 'data'

LOG_FOLDER = 'logs'

# Multilogin-X URLs
MLX_BASE = "https://api.multilogin.com"
MLX_LAUNCHER = "https://launcher.mlx.yt:45001/api/v1"
LOCALHOST = "http://127.0.0.1"
MLX_FOLDER_ID = 'MLX_FOLDER_ID'

MLX_SIGNIN_URL = "{mlx_base}/user/signin"
MLX_CREATE_PROFILE_URL = "/profile/create"
MLX_START_PROFILE_URL = "/profile/f/{folder_id}/p/{profile_id}/start?automation_type=selenium"
MLX_REMOVE_PROFILE_URL = "/profile/remove"
MLX_STOP_PROFILE_URL = "/profile/stop/p/{profile_id}"
MLX_PROFILE_SCREEN_RESOLUTION_URL = "/fpb/resolutions"


# Multilogin X profile data
MLX_PROFILE_ID = "MLX_PROFILE_ID"
MLX_PROFILE_DATA_OS_TYPE_WINDOWS = "windows"
MLX_PROFILE_DATA_BROWSER_TYPE = "browser_type"
MLX_PROFILE_DATA_FOLDER_ID = "folder_id"
MLX_PROFILE_DATA_NAME = "name"
MLX_PROFILE_DATA_OS_TYPE = "os_type"
MLX_PROFILE_DATA_PROXY = "proxy"
MLX_PROFILE_DATA_PARAMETERS = "parameters"
MLX_PROFILE_DATA_FINGERPRINT = "fingerprint"
MLX_PROFILE_DATA_NAVIGATOR = "navigator"
MLX_PROFILE_DATA_HARDWARE_CONCURRENCY = "hardware_concurrency"
MLX_PROFILE_DATA_PLATFORM = "platform"
MLX_PROFILE_DATA_USER_AGENT = "user_agent"
MLX_PROFILE_DATA_OS_CPU = "os_cpu"
MLX_PROFILE_DATA_LOCALIZATION = "localization"
MLX_PROFILE_DATA_LANGUAGE = "languages"
MLX_PROFILE_DATA_LOCALE = "locale"
MLX_PROFILE_DATA_ACCEPT_LANGUAGE = "accept_languages"
MLX_PROFILE_DATA_TIMEZONE = "timezone"
MLX_PROFILE_DATA_ZONE = "zone"
MLX_PROFILE_DATA_GRAPHIC = "graphic"
MLX_PROFILE_DATA_RENDERED = "renderer"
MLX_PROFILE_DATA_VENDOR = "vendor"
MLX_PROFILE_DATA_WEBRTC = "webrtc"
MLX_PROFILE_DATA_PUBLIC_IP = "public_ip"
MLX_PROFILE_DATA_MEDIA_DEVICES = "media_devices"
MLX_PROFILE_DATA_AUDIO_INPUTS = "audio_inputs"
MLX_PROFILE_DATA_AUDIO_OUTPUTS = "audio_outputs"
MLX_PROFILE_DATA_VIDEO_INPUTS = "video_inputs"
MLX_PROFILE_DATA_SCREEN = "screen"
MLX_PROFILE_DATA_HEIGHT = "height"
MLX_PROFILE_DATA_PIXEL_RATIO = "pixel_ratio"
MLX_PROFILE_DATA_WIDTH = "width"
MLX_PROFILE_DATA_GEOLOCATION = "geolocation"
MLX_PROFILE_DATA_ACCURACY = "accuracy"
MLX_PROFILE_DATA_ALTITUDE = "altitude"
MLX_PROFILE_DATA_LATITUDE = "latitude"
MLX_PROFILE_DATA_LONGITUDE = "longitude"
MLX_PROFILE_DATA_PORTS = "ports"
MLX_PROFILE_DATA_CMD_PARAMS = "cmd_params"
MLX_PROFILE_DATA_PARAMS = "params"
MLX_PROFILE_DATA_FLAG = "flag"
MLX_PROFILE_DATA_VALUE = "value"
MLX_PROFILE_DATA_FLAGS = "flags"
MLX_PROFILE_DATA_AUDIO_MASKING = "audio_masking"
MLX_PROFILE_DATA_FONTS_MASKING = "fonts_masking"
MLX_PROFILE_DATA_GEOLOCATION_MASKING = "geolocation_masking"
MLX_PROFILE_DATA_GEOLOCATION_POPUP = "geolocation_popup"
MLX_PROFILE_DATA_GRAPHICS_MASKING = "graphics_masking"
MLX_PROFILE_DATA_GRAPHICS_NOISE = "graphics_noise"
MLX_PROFILE_DATA_LOCALIZATION_MASKING = "localization_masking"
MLX_PROFILE_DATA_MEDIA_DEVICES_MASKING = "media_devices_masking"
MLX_PROFILE_DATA_NAVIGATOR_MASKING = "navigator_masking"
MLX_PROFILE_DATA_PORTS_MASKING = "ports_masking"
MLX_PROFILE_DATA_PROXY_MASKING = "proxy_masking"
MLX_PROFILE_DATA_SCREEN_MASKING = "screen_masking"
MLX_PROFILE_DATA_TIMEZONE_MASKING = "timezone_masking"
MLX_PROFILE_DATA_WEBRTC_MASKING = "webrtc_masking"
MLX_PROFILE_DATA_STORAGE = "storage"
MLX_PROFILE_DATA_IS_LOCAL = "is_local"
MLX_PROFILE_DATA_SAVE_SERVICE_WORKER = "save_service_worker"
MLX_PERMANENTLY = "permanently"

URL_GOOGLE_SEARCH = "https://www.google.com/"


TRENDING_COINS_KEYWORDS = [
    "Bitcoin price",
    "Ethereum updates",
    "Solana news",
    "Cardano developments",
    "Ripple XRP market",
    "Polkadot DOT analysis",
    "Dogecoin DOGE meme",
    "Shiba Inu token",
    "Binance Coin BNB",
    "Litecoin LTC latest",
    "Chainlink LINK forecast",
    "Uniswap UNI swap",
    "Avalanche AVAX trends",
    "Algorand ALGO",
    "Cosmos ATOM staking"
]


REFERRAL_URLS = [
    "https://www.coinbase.com/price/bitcoin",
    "https://www.binance.com/en/trade/BTC_USDT",
    "https://www.kraken.com/prices/btc-bitcoin-price-chart/usd-us-dollar",
    "https://www.coindesk.com/price/ethereum/",
    "https://www.tradingview.com/symbols/ETHBTC/",
    "https://www.cryptocompare.com/coins/sol/overview/USD",
    "https://www.blockchain.com/explorer/assets/btc",
    "https://www.nasdaq.com/market-activity/cryptocurrency",
    "https://www.reddit.com/r/cryptocurrency/",
    "https://techcrunch.com/",
    "https://www.wired.com/",
    "https://www.theverge.com/",
    "https://www.bloomberg.com/crypto",
    "https://www.ted.com/talks",
    "https://www.netflix.com/browse",
    "https://www.amazon.com/",
    "https://www.ebay.com/",
    "https://www.alibaba.com/"
]

WAIT_TIMEOUT = 30
MIN_COUNT = 1
MAX_COUNT = 3

WILDCARD_STRING = "//a[starts-with(@href,'{0}') or starts-with(@href,'https://{0}') or starts-with(@href,'http://{0}') or starts-with(@href,'https://www.{0}') or starts-with(@href,'http://www.{0}') or contains(@href,'http%3A%2F%2Fwww.{0}') or contains(@href,'http%3A%2F%2F{0}') or contains(@href,'https%3A%2F%2Fwww.{0}') or contains(@href,'https%3A%2F%2F{0}') or contains(text(), '{0}')]"
WILDCARD_STRING_SEARCH = "//*[@id='search']//a[starts-with(@href,'{0}') or starts-with(@href,'https://{0}') or starts-with(@href,'http://{0}') or starts-with(@href,'https://www.{0}') or starts-with(@href,'http://www.{0}') or contains(@href,'http%3A%2F%2Fwww.{0}') or contains(@href,'http%3A%2F%2F{0}') or contains(@href,'https%3A%2F%2Fwww.{0}') or contains(@href,'https%3A%2F%2F{0}') or contains(text(), '{0}')]"
WILDCARD_STRING_BOTSTUFF = "//*[@id='botstuff']//a[starts-with(@href,'{0}') or starts-with(@href,'https://{0}') or starts-with(@href,'http://{0}') or starts-with(@href,'https://www.{0}') or starts-with(@href,'http://www.{0}') or contains(@href,'http%3A%2F%2Fwww.{0}') or contains(@href,'http%3A%2F%2F{0}') or contains(@href,'https%3A%2F%2Fwww.{0}') or contains(@href,'https%3A%2F%2F{0}') or contains(text(), '{0}')]"


PROFILE_ID_DEFAULT = "idssdkflj-ad-fdf-a-43-45-d-f"
FOLDER_ID_DEFAULT = "a45cb43e-5d7c-4b77-9cbd-3382a2e4424e"
MLX_EMAIL_DEFAULT = 'mlxemail@aito.com'
MLX_PASSWORD_DEFAULT = 'Kvdg_SMD*_^'