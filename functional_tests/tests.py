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
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Chequeo de la página principal de la aplicación To-Do
        self.browser.get(self.live_server_url)

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
        # "1. Practicar canto en inglés" (el usuario se llama Edith)
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Practicar canto en inglés')

        #Hay todavía una caja y luego agrega 'jugar pinpong'
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Jugar pinpong')
        inputbox.send_keys(Keys.ENTER)

        #La página se vuelve a actualizar y ahora muestra los dos ítems
        self.check_for_row_in_list_table('1: Practicar canto en inglés')
        self.check_for_row_in_list_table('2: Jugar pinpong')

        # Ahora un nuevo usuario ingresa al sitio

        ## Se utiliza una nueva sesión del navegador para estar seguros de que
        ## ninguna información del otro usuario viene a través de cookies, etc
        self.browser.quit()
        self.browser.webdriver.Firefox()

        # El nuevo usuario visita la página de inicio. No hay ninguna información
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Practicar canto en inglés', page_text)
        self.assertNotIn('Jugar pinpong', page_text)

        # El nuevo usuario comienza una nueva lista escribiendo un nuevo item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # El nuevo usuario obtiene su propia URL única (se llama francis)
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # De nuevo, no hay ninguna información del usuario anterior
        page_text = self.brwoser.find_element_by_tag_name('body').text
        self.assertNotIn('Practicar canto en inglés', page_text)
        self.assertIn('Buy milk', page_text)

        #Satisfied, they both go back to sleep
        self.fail('Finish the test!')

        #Ella visita esa URL y su lista continúa allí
