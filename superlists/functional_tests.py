from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retriever_it_later(self):
        # Edith ouviu falar de uma nova aplicacao online interresante para
        # lista de tarefas. Ela decide verificar sua homepage
        self.browser.get('http://localhost:8000')

        # Ela percebe que o titulo da pagina é o cabeçalho mencionam listas de 
        # tarefas (to-do)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Ela é convidada a inserir um item de tarefa imediatamente
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        # Ela digita "Buy peacock feathers" (Comprar apenas de pavão) em uma caixa
        # de texto (o hobby de Edith é fazer iscas para pesca com fly)
        inputbox.send_keys('Buy peacock feathers')

        # Quando ela tecla enter, a pagina é atualizada, e agora a pagina lista
        # "1: Buy peacock feathers como um item a sua lista de tarefas"
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = self.browser.find_elements_by_tag_name('tr')
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])

        # Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
        # item. Ela insere "Use peacock feathers to make a fly" (Usar penas de pavão
        # para fazer um fly-Edith é bem metodica)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # A pagina é atualizada novamente e agora mostra os dois itens em sua lista
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly',
            [row.text for row in rows]
        )

        # Edith se pergunta se o site lembrará de sua lista. Então ela nota
        # que o site gerou um URL unico para ela -- há um pequeno
        # texto explicativo para isso.
        self.fail('Finish the test!')

        # Ela acessa esse URL - sua lista de tarefas continua lá.

        # Satisfeita ela volta a dormir

if __name__ == '__main__':
    unittest.main(warnings='ignore')