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
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Se invita al usuario a ingresar un ítem para hacer inmediatamente
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # El usuario escribe "Practicar canto en inglés" en la caja de texto
        inputbox.send_keys('Practicar canto en inglés')

        # Cuando el usuario presiona enter la página se actualiza, y ahora la página lista
        # "1. Practicar canto en inglés"
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Practicar canto en inglés', [row.text for row in rows])

        #Hay todavía una caja y luego agrega 'jugar pinpong'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Jugar pinpong')
        inputbox.send_keys(Keys.ENTER)

        #La página se vuelve a actualizar y ahora muestra los dos ítems
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Practicar canto en inglés', [row.text for row in rows])
        self.assertIn('2: Jugar pinpong', [row.text for row in rows])

        # El usuario quisiera saber que el sitio web recordará la lista, ella nota
        # un letrero que dice que el sitio generó una URL única -- Allí hay un texto
        # que explica ello
        self.fail('Finish the test!')

        #Ella visita esa URL y su lista continúa allí
if __name__ == '__main__':
    unittest.main(warnings='ignore')
