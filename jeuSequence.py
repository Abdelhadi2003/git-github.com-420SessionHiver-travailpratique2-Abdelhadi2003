from machine import Pin
from time import sleep
from moduleTP2 import Partie

led_bleu = Pin(13, Pin.OUT)
led_rouge = Pin(12, Pin.OUT)
led_vert = Pin(10, Pin.OUT)

btn_bleu = Pin(16, Pin.IN, Pin.PULL_UP)
btn_rouge = Pin(17, Pin.IN, Pin.PULL_UP)
btn_vert = Pin(18, Pin.IN, Pin.PULL_UP)

btn_bleu_prev = btn_bleu.value()
btn_rouge_prev = btn_rouge.value()
btn_vert_prev = btn_vert.value()

ctr_bleu = 0
ctr_rouge = 0
ctr_vert = 0

