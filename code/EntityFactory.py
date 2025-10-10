#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Background import Background
from code.Const import WINDOW_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for i in range(6):
                    list_bg.append(Background(f'Level1BG{i}', (0, 0)))
                    list_bg.append(Background(f'Level1BG{i}', (WINDOW_WIDTH, 0)))
                return list_bg