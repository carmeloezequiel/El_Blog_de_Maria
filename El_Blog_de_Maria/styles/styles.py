from enum import Enum
import reflex as rx

#Constantes
MAX_WIDTH='600px'


#Tamaños 
class Spacer(Enum):
    SMALL = '0.5em'
    MEDIUM = '0.8em'
    DEFAULT = '1em'
    MEDIUM_BIG = '1.5em'
    BIG = '2em'
    
    
    
BASE_STYLE = {
    rx.button: {
        'width':'100%',
        'height':'100%',
        'display':'block',
        'padding': Spacer.SMALL,
        'border_radius':Spacer.DEFAULT
    },
    rx.link:{
        'text_decoration':'none',
        '_hover':{}
    }
}

button_title_style = dict(
    font_size= Spacer.DEFAULT.value
)

button_body_style = dict(
    font_size= Spacer.MEDIUM.value
)

title_style = dict(
        #size='5',
        width='100%',
        padding_top=Spacer.DEFAULT.value
)