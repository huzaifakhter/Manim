from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.kokkro import KokoroService

# configurations
config.disable_caching = True
config.background_color = "#0D1117"
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 14.2
config.frame_width = 8

# colors
text_color = "RED"
sec_color = "GREEN"
acccent_color = "WHITE"
Hilight_color = "YELLOW"

# voices
voice_artist = "bm_lewis"

VOICE_NAME = [
    'af',
    'af_bella', 'af_sarah', 'am_adam', 'am_michael',
    'bf_emma', 'bf_isabella', 'bm_george', 'bm_lewis',
    'af_nicole', 'af_sky',
]