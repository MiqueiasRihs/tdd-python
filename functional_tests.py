from selenium import webdriver

browser = webdriver.Firefox()

# Edith ouviu falar de uma nova aplicacao online interresante para
# lista de tarefas. Ela decide verificar sua homepage
browser.get('http://localhost:8000')

# Ela percebe que o titulo da pagina é o cabeçalho mencionam listas de 
# tarefas (to-do)
assert 'To-Do' in browser.title

# Ela é convidada a inserir um item de tarefa imediatamente
# Ela digita "Buy peacock feathers" (Comprar apenas de pavão) em uma caixa
# de texto (o hobby de Edith é fazer iscas para pesca com fly)

# Quando ela tecla enter, a pagina é atualizada, e agora a pagina lista
# "1: Buy peacock feathers como um item a sua lista de tarefas"

# Ainda continua havendo uma caixa de texto convidando-a a acrescentar outro
# item. Ela insere "Use peacock feathers to make a fly" (Usar penas de pavão
# para fazer um fly-Edith é bem metodica)

# A pagina é atualizada novamente e agora mostra os dois itens em sua lista

# Edith se pergunta se o site lembrará de sua lista. Então ela nota
# que o site gerou um URL unico para ela -- há um pequeno
# texto explicativo para isso.

# Ela acessa esse URL - sua lista de tarefas continua lá.

# Satisfeita ela volta a dormir

browser.quit()