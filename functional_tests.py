#!/usr/bin/python
# -*- coding: utf-8 -*-
#     Developed by Julian Camilo Marin Sanchez - marin.julian@gmail.com - @juliancms
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
from selenium import webdriver
import unittest
class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Chequeo de la página principal de la aplicación To-Do
        self.browser.get("http://localhost:8000")

        # El título de la página menciona la palabra 'To-Do'
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the text!')
        # Se invita al usuario a ingresar un ítem para hacer inmediatamente

        # El usuario escribe "Practicar canto en inglés" en la caja de texto

        # Cuando el usuario presiona enter la página se actualiza, y ahora la página lista
        # "1. Practicar canto en inglés"

        # La página continúa mostrando una caja de texto para añadir más ítems al "To-Do".
        # El usuario ingresa "Estudiar Python"

        # La página se actualiza de nuevo y ahora muestra ambos ítems en la lista

        # El usuario quisiera saber que el sitio web recordará la lista, ella nota
        # un letrero que dice que el sitio generó una URL única -- Allí hay un texto
        # que explica ello

        #Ella visita esa URL y su lista continúa allí
if __name__ == '__main__':
    unittest.main(warnings='ignore')
