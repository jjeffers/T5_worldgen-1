'''star unit tests'''
from __future__ import print_function

import unittest
from T5_worldgen.star import _Star, Primary

SAMPLE_SIZE = 1000


class TestStarTables(unittest.TestCase):
    '''Confirm contents of star generation tables'''
    def check_table_contents(self, table_data, table):
        '''Generic table contents checker'''
        for (ctr, size) in enumerate(table_data):
            table_contents = table.lookup(ctr - 6)
            print(ctr, ctr - 6, size, table_contents)
            self.assertTrue(
                size == table_contents)

    def test_spectral_type_table(self):
        '''Confirm contents of spectral type table'''
        star = _Star()
        table_data = [
            'OB', 'A', 'A', 'F', 'F',
            'G', 'G', 'K', 'K', 'M',
            'M', 'M', 'BD', 'BD', 'BD']
        self.check_table_contents(table_data, star.spectral_type_table)

    def test_size_o(self):
        '''Confirm contents of size table type O'''
        star = _Star()
        table_data = [
            'Ia', 'Ia', 'Ib', 'II', 'III',
            'III', 'III', 'V', 'V', 'V',
            'IV', 'D', 'IV', 'IV', 'IV']
        self.check_table_contents(table_data, star.size_o_table)

    def test_size_b(self):
        ''' Confirm contents of size table type B'''
        star = _Star()
        table_data = [
            'Ia', 'Ia', 'Ib', 'II', 'III',
            'III', 'III', 'III', 'V', 'V',
            'IV', 'D', 'IV', 'IV', 'IV']
        self.check_table_contents(table_data, star.size_b_table)

    def test_size_a(self):
        ''' Confirm contents of size table type A'''
        star = _Star()
        table_data = [
            'Ia', 'Ia', 'Ib', 'II', 'III',
            'IV', 'V', 'V', 'V', 'V',
            'V', 'D', 'V', 'V', 'V']
        self.check_table_contents(table_data, star.size_a_table)

    def test_size_f(self):
        ''' Confirm contents of size table type F'''
        star = _Star()
        table_data = [
            'II', 'II', 'III', 'IV', 'V',
            'V', 'V', 'V', 'V', 'V',
            'VI', 'D', 'VI', 'VI', 'VI']
        self.check_table_contents(table_data, star.size_f_table)

    def test_size_g(self):
        ''' Confirm contents of size table type G'''
        star = _Star()
        table_data = [
            'II', 'II', 'III', 'IV', 'V',
            'V', 'V', 'V', 'V', 'V',
            'VI', 'D', 'VI', 'VI', 'VI']
        self.check_table_contents(table_data, star.size_g_table)

    def test_size_k(self):
        ''' Confirm contents of size table type K'''
        star = _Star()
        table_data = [
            'II', 'II', 'III', 'IV', 'V',
            'V', 'V', 'V', 'V', 'V',
            'VI', 'D', 'VI', 'VI', 'VI']
        self.check_table_contents(table_data, star.size_k_table)

    def test_size_m(self):
        ''' Confirm contents of size table type M'''
        star = _Star()
        table_data = [
            'II', 'II', 'II', 'II', 'III',
            'V', 'V', 'V', 'V', 'V',
            'VI', 'D', 'VI', 'VI', 'VI']
        self.check_table_contents(table_data, star.size_m_table)


class TestFVIDecimals(unittest.TestCase):
    '''FVi edge case'''
    def test_f_vi_decimal(self):
        '''Confirm F VI has decimals in range 0-4'''
        for _ in range(0, SAMPLE_SIZE):
            star = _Star()
            star.spectral_type = 'F'
            star.size = 'VI'
            star.set_decimal()
            print(star.decimal)
            self.assertTrue(star.decimal <= 4)

class TestHZTables(unittest.TestCase):
    '''Check HZ orbit tables'''
    def check_hz_orbits(self):
        '''Test HZ orbits'''

        hz_table = {
            'O': {'Ia': 15, 'Ib': 15, 'II': 14, 'III': 13, 'IV': 12, 'V': 11, 'VI': None, 'D': 1},
            'B': {'Ia': 13, 'Ib': 13, 'II': 12, 'III': 11, 'IV': 10, 'V': 9, 'VI': None, 'D': 0},
            'A': {'Ia': 12, 'Ib': 11, 'II': 9, 'III': 7, 'IV': 7, 'V': 7, 'VI': None, 'D': 0},
            'F': {'Ia': 11, 'Ib': 10, 'II': 9, 'III': 6, 'IV': 6, 'V': 5, 'VI': 3, 'D': 0},
            'G': {'Ia': 12, 'Ib': 10, 'II': 9, 'III': 7, 'IV': 5, 'V': 3, 'VI': 2, 'D': 0},
            'K': {'Ia': 12, 'Ib': 10, 'II': 9, 'III': 8, 'IV': 5, 'V': 2, 'VI': 1, 'D': 0},
            'M': {'Ia': 12, 'Ib': 11, 'II': 10, 'III': 9, 'IV': None, 'V': 0, 'VI': 0, 'D': 0}
        }

        for st in [OBAFGKM]:
            for sz in ['Ia', 'Ia', 'II', 'III', 'IV', 'V', 'VI', 'D']:
                star = _Star()
                star.spectral_type = st
                star.size = sz
                star.set_hz()
                print('st = {} sz = {} hz_table = {} star.habitable_zone = {}'.format(
                    st, sz, hz_table[st][sz], star.habitable_zone))
                self.assertTrue(star.habitable_zone == hz_table[st][sz])
