import pytest
import pygame
from ..controller import Controller
from ..model import Model


class TestModel:
    def test_mixer_init(self):
        Model.__init__(Controller())
        assert pygame.mixer.init() == (44100,-16,2)

    def test_ini_file(self):
        pass



    

    